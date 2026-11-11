# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import inspect
import json
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import Mock, patch
from urllib.error import URLError

from app.dosya.depremler import Depremler


class TestDepremler(unittest.TestCase):
    @staticmethod
    def _afad_yaniti():
        return [{
            "date": "2026-11-10T10:33:00",
            "location": "Örnek (İzmir)",
            "magnitude": "2.0",
            "latitude": "38.0",
            "longitude": "27.0",
            "depth": "7",
        }]

    def _depremler(self):
        return patch(
            "app.internet.baglanti.Baglanti.json_indir",
            return_value=json.dumps(self._afad_yaniti()).encode("utf-8"),
        )

    @staticmethod
    def _olay(tarih, buyukluk, konum):
        return {
            "date": tarih,
            "location": konum,
            "magnitude": str(buyukluk),
            "latitude": "38.0",
            "longitude": "27.0",
            "depth": "7",
        }

    def _yanitla(self, olaylar):
        return patch(
            "app.internet.baglanti.Baglanti.json_indir",
            return_value=json.dumps(olaylar).encode("utf-8"),
        )

    def test_tum_veriler_afad_alanlarini_dondurur(self):
        with self._depremler():
            sonuc = Depremler().tum_veriler()

        self.assertEqual(
            sonuc,
            [["2026-11-10 13:33:00",
                "Örnek (İzmir)", "2.0", "38.0", "27.0", "7"]],
        )

    def test_tablo_veriler_baslik_ve_depremi_gosterir(self):
        with self._depremler():
            sonuc = Depremler().tablo_veriler()

        self.assertIn("Tarih ve Saat (UTC+03:00)", sonuc)
        satir = next(line for line in sonuc.splitlines()
                     if "Örnek (İzmir)" in line)
        hucreler = [hucre.strip() for hucre in satir.split("|")[1:-1]]
        self.assertEqual(
            hucreler,
            ["2026-11-10 13:33:00",
                "Örnek (İzmir)", "2.0", "38.0", "27.0", "7"],
        )

    def test_duzenli_veriler_satiri_dondurur_ve_basligi_yazdirir(self):
        stdout = StringIO()
        with self._depremler(), redirect_stdout(stdout):
            sonuc = Depremler().duzenli_veriler()

        self.assertEqual(
            sonuc,
            "2026-11-10 13:33:00 - Örnek (İzmir) - 2.0 - 38.0 - 27.0 - 7",
        )
        self.assertIn("Tarih ve Saat (UTC+03:00) - Konum", stdout.getvalue())

    def test_json_nesnesi_liste_bekleniyor_mesaji_doner(self):
        with patch(
            "app.internet.baglanti.Baglanti.json_indir",
            return_value=json.dumps({"eventID": "598758"}).encode("utf-8"),
        ):
            sonuc = Depremler().tum_veriler()

        self.assertEqual(
            sonuc,
            "JSON formatı beklenen yapıda değil: Deprem listesi bekleniyordu.",
        )

    def test_readme_hizli_baslangic_ornegi_kutuphane_kullanimiyla_eslesir(self):
        readme = Path(__file__).resolve().parents[1] / "README.md"
        metin = readme.read_text(encoding="utf-8")
        bolum = metin.split("## Hızlı başlangıç", 1)[
            1].split("## Çıktı biçimleri", 1)[0]
        kod = bolum.split("```python", 1)[1].split("```", 1)[0]
        self.assertIn("from app.dosya.depremler import Depremler", kod)
        self.assertIn("print(depremler.duzenli_veriler())", kod)
        self.assertIn("başlık satırını kendisi ekrana yazar", metin)
        self.assertIn("depremler.tum_veriler(6, 3)", metin)
        self.assertIn("3.0 dahil", metin)
        stdout = StringIO()

        with self._depremler(), redirect_stdout(stdout):
            depremler = Depremler()
            print(depremler.duzenli_veriler())

        self.assertIn("Örnek (İzmir)", stdout.getvalue())

    def test_depremler_en_yeniden_eskiye_siralanir(self):
        cevap = [
            {**self._afad_yaniti()
             [0], "date": "2026-11-09T10:00:00", "location": "Eski"},
            {**self._afad_yaniti()
             [0], "date": "2026-11-10T10:00:00", "location": "Yeni"},
        ]
        with patch(
            "app.internet.baglanti.Baglanti.json_indir",
            return_value=json.dumps(cevap).encode("utf-8"),
        ):
            sonuc = Depremler().tum_veriler()

        self.assertEqual(
            [deprem[0] for deprem in sonuc],
            ["2026-11-10 13:00:00", "2026-11-09 13:00:00"],
        )

    def test_tum_veriler_limit_ile_en_yeni_n_kaydi_doner(self):
        olaylar = [
            self._olay(f"2026-11-10T10:{dakika:02}:00", 2, f"Olay {dakika}")
            for dakika in range(1, 9)
        ]

        with self._yanitla(olaylar):
            sonuc = Depremler().tum_veriler(limit=6)

        self.assertEqual(len(sonuc), 6)
        self.assertEqual(sonuc[0][1], "Olay 8")
        self.assertEqual(sonuc[-1][1], "Olay 3")

    def test_sunum_metotlari_limit_ve_varsayilanlarini_korur(self):
        olaylar = [
            self._olay(f"2026-11-10T10:{dakika:02}:00", 2, f"Olay {dakika}")
            for dakika in range(1, 13)
        ]
        with self._yanitla(olaylar), redirect_stdout(StringIO()):
            duzenli = Depremler().duzenli_veriler(6)
        with self._yanitla(olaylar):
            tablo = Depremler().tablo_veriler(6)
            tumu = Depremler().tablo_veriler()

        self.assertEqual(len(duzenli.splitlines()), 6)
        self.assertEqual(tablo.count("Olay "), 6)
        self.assertEqual(tumu.count("Olay "), 10)

    def test_minimum_buyukluk_filtre_esik_degerini_dahil_tutar(self):
        olaylar = [
            self._olay("2026-11-10T10:01:00", 2.9, "Altında"),
            self._olay("2026-11-10T10:02:00", 3.0, "Eşit"),
            self._olay("2026-11-10T10:03:00", 3.1, "Üstünde"),
        ]

        with self._yanitla(olaylar):
            sonuc = Depremler().tum_veriler(minimum_buyukluk=3)

        self.assertEqual([deprem[1] for deprem in sonuc], ["Üstünde", "Eşit"])

    def test_sozluk_olmayan_kayit_nazikce_hata_doner(self):
        with self._yanitla(["a", "b"]):
            sonuc = Depremler().tum_veriler()

        self.assertEqual(
            sonuc,
            "JSON formatı beklenen yapıda değil: Her deprem kaydı nesne olmalı.",
        )

    def test_buyukluk_filtresi_limitten_once_uygulanir(self):
        olaylar = [
            self._olay("2026-11-10T10:01:00", 4, "Eski uygun"),
            self._olay("2026-11-10T10:02:00", 1, "Uygun değil"),
            self._olay("2026-11-10T10:03:00", 3.5, "Yeni uygun"),
        ]

        with self._yanitla(olaylar):
            sonuc = Depremler().tum_veriler(limit=1, minimum_buyukluk=3)

        self.assertEqual([deprem[1] for deprem in sonuc], ["Yeni uygun"])

    def test_filtre_parametreleri_gecersizse_kisisellestirilmis_metin_doner(self):
        with self._depremler():
            hatali_limit = Depremler().tum_veriler(limit=0)
        with self._depremler():
            hatali_buyukluk = Depremler().tum_veriler(minimum_buyukluk=float("nan"))

        self.assertIn("limit", hatali_limit)
        self.assertIn("minimum_buyukluk", hatali_buyukluk)

    def test_parametre_aciklamalari_intellisense_icin_mevcuttur(self):
        for metot in (
            Depremler.tum_veriler,
            Depremler.duzenli_veriler,
            Depremler.tablo_veriler,
        ):
            imza = inspect.signature(metot)
            self.assertIn("limit", imza.parameters)
            self.assertIn("minimum_buyukluk", imza.parameters)
            self.assertIn("limit:", metot.__doc__)
            self.assertIn("minimum_buyukluk:", metot.__doc__)

    def test_internet_yokken_baglanti_hatasi_mesaji(self):
        with patch("app.internet.baglanti.request.urlopen", side_effect=URLError("offline")):
            sonuc = Depremler().tum_veriler()

        self.assertEqual(
            sonuc, "İnternet bağlantısı yok veya sayfa indirilemedi.")

    def test_bos_cevapta_durum_kodu_mesaji(self):
        yanit = Mock()
        yanit.__enter__ = Mock(return_value=yanit)
        yanit.__exit__ = Mock(return_value=False)
        yanit.getcode.return_value = 204

        with patch("app.internet.baglanti.request.urlopen", return_value=yanit):
            sonuc = Depremler().tum_veriler()

        self.assertEqual(sonuc, "Sunucudan beklenmeyen durum kodu: 204.")

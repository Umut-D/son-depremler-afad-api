# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import json
import os
import unittest
from urllib.parse import parse_qs, urlparse
from unittest.mock import Mock, patch
from urllib.error import URLError

from app.internet.baglanti import Baglanti


class TestIndir(unittest.TestCase):
    def setUp(self):
        self.baglanti = Baglanti()

    @staticmethod
    def _yanit(durum_kodu=200, icerik=b"[]"):
        yanit = Mock()
        yanit.__enter__ = Mock(return_value=yanit)
        yanit.__exit__ = Mock(return_value=False)
        yanit.getcode.return_value = durum_kodu
        yanit.read.return_value = icerik
        return yanit

    @unittest.skipUnless(
        os.getenv("RUN_AFAD_INTEGRATION") == "1",
        "Canlı AFAD deneyi için RUN_AFAD_INTEGRATION=1 ayarla.",
    )
    def test_afad_canli_yanit_json_listesidir(self):
        sonuc = self.baglanti.json_indir()

        self.assertIsInstance(sonuc, bytes)
        self.assertIsInstance(json.loads(sonuc), list)

    def test_200_yanitinda_json_bytes_doner(self):
        yanit = self._yanit(icerik=b"[]")

        with patch("app.internet.baglanti.request.urlopen", return_value=yanit) as ac:
            sonuc = self.baglanti.json_indir()

        self.assertEqual(sonuc, b"[]")
        ac.assert_called_once_with(self.baglanti.url, timeout=10)

    def test_url_tarih_parametrelerini_bicimlendirir(self):
        sorgu = parse_qs(urlparse(self.baglanti.url).query)

        self.assertEqual(set(sorgu), {"start", "end", "format"})
        self.assertEqual(sorgu["format"], ["json"])
        self.assertRegex(sorgu["start"][0], r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$")

    def test_baglanti_zaman_asiminda_dogru_mesaj_doner(self):
        with patch(
            "app.internet.baglanti.request.urlopen",
            side_effect=URLError(TimeoutError()),
        ):
            sonuc = self.baglanti.json_indir()

        self.assertEqual(sonuc, "Sunucuya bağlanma zaman aşımına uğradı.")

    def test_yanit_okuma_zaman_asiminda_dogru_mesaj_doner(self):
        yanit = self._yanit()
        yanit.read.side_effect = TimeoutError()

        with patch("app.internet.baglanti.request.urlopen", return_value=yanit):
            sonuc = self.baglanti.json_indir()

        self.assertEqual(
            sonuc, "Sunucudan yanıt verisi okuma zaman aşımına uğradı.")

    def test_internet_yokken_baglanti_hatasi_mesaji_doner(self):
        with patch(
            "app.internet.baglanti.request.urlopen",
            side_effect=URLError("offline"),
        ):
            sonuc = self.baglanti.json_indir()

        self.assertEqual(
            sonuc, "İnternet bağlantısı yok veya sayfa indirilemedi.")

    def test_200_disindaki_durum_kodu_mesaji_doner(self):
        yanit = self._yanit(durum_kodu=204)

        with patch("app.internet.baglanti.request.urlopen", return_value=yanit):
            sonuc = self.baglanti.json_indir()

        self.assertEqual(sonuc, "Sunucudan beklenmeyen durum kodu: 204.")

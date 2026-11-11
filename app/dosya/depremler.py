# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=import-error

import json
import math
import tabulate

from app.internet.baglanti import Baglanti
from app.dosya.tarih import Tarih


class Depremler:
    def __init__(self):
        self._json = Baglanti()

    def _json_veri_yukle(self) -> list | str:
        veri = self._json.json_indir()

        # Bağlantı katmanının hata mesajını JSON sanıp ayrıştırmaya çalışma.
        if isinstance(veri, str):
            return veri

        veriler = json.loads(veri)
        if not isinstance(veriler, list):
            return "JSON formatı beklenen yapıda değil: Deprem listesi bekleniyordu."

        return veriler

    def tum_veriler(
        self,
        limit: int | None = None,
        minimum_buyukluk: float | None = None,
    ) -> list | str:
        """Depremleri yenilerden eskilere sıralayıp isteğe göre süzer.

        Args:
            limit: Döndürülecek en yeni deprem sayısı. None ise tüm kayıtlar döner.
            minimum_buyukluk: Bu değer ve üzerindeki depremleri döndürür.
        """
        hata = self._parametre_hatasi(limit, minimum_buyukluk)
        if hata:
            return hata

        try:
            depremler = []
            veriler = self._json_veri_yukle()
            if isinstance(veriler, str):
                return veriler
            if any(not isinstance(event, dict) for event in veriler):
                return "JSON formatı beklenen yapıda değil: Her deprem kaydı nesne olmalı."

            for event in veriler:
                depremler.append(
                    [
                        Tarih.afad_utc_turkiye_saatine(event["date"]),
                        f"{event['location']}",
                        f"{event['magnitude']}",
                        f"{event['latitude']}",
                        f"{event['longitude']}",
                        f"{event['depth']}",
                    ])

            depremler = sorted(depremler, reverse=True)
            if minimum_buyukluk is not None:
                depremler = [
                    deprem for deprem in depremler
                    if float(deprem[2]) >= minimum_buyukluk
                ]
            if limit is not None:
                depremler = depremler[:limit]

            return depremler

        except json.JSONDecodeError:
            return "JSON verisi okunamadı"
        except KeyError:
            return "JSON formatı beklenen yapıda değil: Eksik anahtar var."
        except TypeError:
            return "JSON formatı beklenen yapıda değil: Alan türleri uygun değil."
        except ValueError:
            return "Değer hatası oldu. Bilemedim."

    @staticmethod
    def _parametre_hatasi(
        limit: int | None,
        minimum_buyukluk: float | None,
    ) -> str | None:
        if limit is not None and (
            isinstance(limit, bool) or not isinstance(limit, int) or limit < 1
        ):
            return "Hata: 'limit' pozitif bir tam sayı olmalı."

        if minimum_buyukluk is not None and (
            isinstance(minimum_buyukluk, bool)
            or not isinstance(minimum_buyukluk, (int, float))
            or not math.isfinite(minimum_buyukluk)
            or minimum_buyukluk < 0
        ):
            return "Hata: 'minimum_buyukluk' sıfır veya daha büyük, sonlu bir sayı olmalı."

        return None

    def duzenli_veriler(
        self,
        limit: int = 7,
        minimum_buyukluk: float | None = None,
    ) -> str:
        """Depremleri satır satır verir; isteğe göre sayı ve büyüklükle süzer.

        Args:
            limit: Gösterilecek en yeni deprem sayısı (varsayılan 7).
            minimum_buyukluk: Bu değer ve üzerindeki depremleri gösterir.
        """
        veriler = self.tum_veriler(limit, minimum_buyukluk)
        if isinstance(veriler, str):
            return veriler

        print("Tarih ve Saat (UTC+03:00)", "Konum", "Şiddet",
              "Enlem", "Boylam", "Derinlik", sep=" - ")

        tum_veriler = [" - ".join(veri) for veri in veriler]

        return "\n".join(tum_veriler)

    def tablo_veriler(
        self,
        limit: int = 10,
        minimum_buyukluk: float | None = None,
    ) -> str:
        """Depremleri tablo olarak verir; isteğe göre sayı ve büyüklükle süzer.

        Args:
            limit: Gösterilecek en yeni deprem sayısı (varsayılan 10).
            minimum_buyukluk: Bu değer ve üzerindeki depremleri gösterir.
        """
        veriler = self.tum_veriler(limit, minimum_buyukluk)

        if isinstance(veriler, str):
            return veriler

        basliklar = ["Tarih ve Saat (UTC+03:00)", "Konum",
                     "Şiddet", "Enlem", "Boylam", "Derinlik"]
        tablo = tabulate.tabulate(
            veriler,
            headers=basliklar,
            tablefmt="grid",
            colalign=("left", "left", "left", "left", "left", "left"),
            disable_numparse=True,
        )
        return tablo

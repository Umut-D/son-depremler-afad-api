# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=import-error

import json
import tabulate

from app.internet.baglanti import Baglanti


class Depremler:
    def __init__(self):
        self._json = Baglanti()

    def _json_veri_yukle(self):
        veri = self._json.json_indir()

        return json.loads(veri)

    def tum_veriler(self) -> list | str:
        try:
            depremler = []
            for event in self._json_veri_yukle():
                depremler.append(
                    [
                        f"{event['date'].replace('T', ' ')}",
                        f"{event['location']}",
                        f"{event['magnitude']}",
                        f"{event['latitude']}",
                        f"{event['longitude']}",
                        f"{event['depth']}",
                    ])

            return sorted(depremler, reverse=True)

        except json.JSONDecodeError:
            return "JSON verisi okunamadı"
        except KeyError:
            return "JSON formatı beklenen yapıda değil: Eksik anahtar var."
        except ValueError:
            return "Değer hatası oldu. Bilemedim."

    def duzenli_veriler(self, limit=7) -> str:
        veriler = self.tum_veriler()
        if isinstance(veriler, str):
            return veriler

        print("Tarih ve Saat", "Konum", "Şiddet", "Enlem", "Boylam", "Derinlik", sep=" - ")

        tum_veriler = [" - ".join(veri) for veri in veriler[:limit]]

        return "\n".join(tum_veriler)

    def tablo_veriler(self, limit=7) -> str:
        veriler = self.tum_veriler()
        if isinstance(veriler, str):
            return veriler

        basliklar = ["Tarih ve Saat", "Konum", "Şiddet", "Enlem", "Boylam", "Derinlik"]
        tablo = tabulate.tabulate(
            veriler[:limit],
            headers=basliklar,
            tablefmt="grid",
            colalign=("left", "left", "left", "left", "left", "left")
        )
        return tablo

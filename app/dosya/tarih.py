# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-few-public-methods

from datetime import datetime, timedelta


class Tarih:
    def son_24_saat(self) -> str:
        try:
            bitis = datetime.today()
            baslangic = bitis - timedelta(days=1)

            bitis = self._donustur(bitis)
            baslangic = self._donustur(baslangic)

            return f"start={baslangic}&end={bitis}"

        except ValueError:
            return "Hata: Son 24 saat tarihini alırken bir hata oldu."

    @staticmethod
    def _donustur(zaman) -> (str | None):
        try:
            return f"{zaman.strftime('%x').replace('/', '-')}%20{zaman.strftime('%X')}"
        except ValueError:
            return None

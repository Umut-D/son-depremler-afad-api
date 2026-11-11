# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-few-public-methods

from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo


class Tarih:
    @staticmethod
    def afad_utc_turkiye_saatine(zaman: str) -> str:
        """AFAD'ın UTC tarihini cihazdan bağımsız olarak Türkiye saatine çevirir."""
        utc_zamani = datetime.fromisoformat(zaman)
        if utc_zamani.tzinfo is None:
            utc_zamani = utc_zamani.replace(tzinfo=timezone.utc)
        turkiye_zamani = utc_zamani.astimezone(ZoneInfo("Europe/Istanbul"))
        return turkiye_zamani.strftime("%Y-%m-%d %H:%M:%S")

    def son_24_saat(self) -> str:
        # AFAD tarihleri UTC; bilgisayarın yerel saati filtreyi kaydırmasın.
        bitis = datetime.now(timezone.utc)
        baslangic = bitis - timedelta(days=1)

        bitis = self._donustur(bitis)
        baslangic = self._donustur(baslangic)

        return f"start={baslangic}&end={bitis}"

    @staticmethod
    def _donustur(zaman) -> str:
        # AFAD biçimini kullan; %x bilgisayarın dil ayarına göre değişir.
        return zaman.strftime("%Y-%m-%dT%H:%M:%S")

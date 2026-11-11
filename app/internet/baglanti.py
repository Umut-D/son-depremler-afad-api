# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=line-too-long

from urllib import request
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode

from app.dosya.tarih import Tarih


class Baglanti:
    def __init__(self):
        tarih = Tarih()
        parametreler = dict(
            parametre.split("=", 1)
            for parametre in tarih.son_24_saat().split("&")
        )
        parametreler["format"] = "json"
        self.url = (
            "https://deprem.afad.gov.tr/apiv2/event/filter?"
            f"{urlencode(parametreler)}"
        )

    def json_indir(self) -> bytes | str:
        try:
            # Sabit HTTPS AFAD adresi kullanıcı girdisi almadığından B310 yanlış alarm verir.
            with request.urlopen(self.url, timeout=10) as response:  # nosec B310
                durum_kodu = response.getcode()
                if durum_kodu == 200:
                    return response.read()
                # Başarılı olmayan cevapta boş veri yerine gerçek nedeni bildir.
                return f"Sunucudan beklenmeyen durum kodu: {durum_kodu}."
        except HTTPError:
            return "Sunucudan HTTP hatası alındı."
        except URLError as hata:
            if isinstance(hata.reason, TimeoutError):
                return "Sunucuya bağlanma zaman aşımına uğradı."
            return "İnternet bağlantısı yok veya sayfa indirilemedi."
        except TimeoutError:
            return "Sunucudan yanıt verisi okuma zaman aşımına uğradı."

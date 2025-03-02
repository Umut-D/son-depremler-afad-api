# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=line-too-long

from urllib import request
from urllib.error import URLError
from urllib3.exceptions import HTTPError

from app.dosya.tarih import Tarih


class Baglanti:
    def __init__(self):
        tarih = Tarih()
        self.url = f"https://deprem.afad.gov.tr/apiv2/event/filter?&{tarih.son_24_saat()}&format=json"

    def json_indir(self) -> (str | None):
        try:
            with request.urlopen(self.url, timeout=10) as response:
                if response.getcode() == 200:
                    return response.read()
        except URLError:
            return "İnternet bağlantısı yok veya sayfa indirilemedi."
        except TimeoutError:
            return "Bağlantı zaman aşımına uğradı."
        except HTTPError:
            return "Sunucudan HTTP hatası alındı."

        return None

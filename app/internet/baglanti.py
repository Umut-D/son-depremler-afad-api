"""
Baglanti Sınıfı

Bu sınıf, belirtilen URL'den veri indirmek için gerekli yöntemi sağlar.

Attributes:
    url (str): Verinin indirileceği URL adresi.

Methods:
    __init__: Baglanti sınıfının başlatıcı yöntemi, URL oluşturur.
    indir: Belirtilen URL'den veri indirir.
"""
from urllib import request
from urllib.error import URLError
from app.dosya.tarih import Tarih


class Baglanti:
    """
    Baglanti Sınıfı

    Bu sınıf, belirtilen URL'den veri indirmek için gerekli yöntemi sağlar.
    """

    def __init__(self):
        """
        Baglanti sınıfının başlatıcı yöntemi, URL oluşturur.

        """
        tarih = Tarih()
        self.url = f"https://deprem.afad.gov.tr/apiv2/event/filter?&{tarih.son_24_saat()}&format=json"

    def indir(self) -> str | None:
        """
        Belirtilen URL'den veri indirir.

        Returns:
            str | None: İndirilen veri veya hata mesajı
        """
        try:
            with request.urlopen(self.url, timeout=10) as response:
                if response.getcode() == 200:
                    return response.read()
        except URLError:
            return "Web sayfası indirilerken bir veya birkaç hata oldu."

        return None

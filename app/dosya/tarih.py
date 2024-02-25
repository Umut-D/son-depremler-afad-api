"""
Tarih Sınıfı

Bu sınıf, tarih ve zamanla ilgili işlemleri gerçekleştirmek için gerekli yöntemleri sağlar.

Methods:
    son_24_saat: Son 24 saatlik zaman aralığını hesaplar ve formatlar.
    _donustur: Verilen zaman nesnesini belirli bir formata dönüştürür.
"""
from datetime import datetime, timedelta


class Tarih:
    """
    Tarih Sınıfı

    Bu sınıf, tarih ve zamanla ilgili işlemleri gerçekleştirmek için gerekli yöntemleri sağlar.
    """

    def son_24_saat(self) -> str:
        """
        Son 24 saatlik zaman aralığını hesaplar ve formatlar.

        Returns:
            str: Son 24 saatlik zaman aralığını içeren formatlanmış metin.
        """
        bitis = datetime.today()
        baslangic = bitis - timedelta(days=1)

        bitis = self._donustur(bitis)
        baslangic = self._donustur(baslangic)

        return f"start={baslangic}&end={bitis}"

    @staticmethod
    def _donustur(zaman):
        """
        Verilen zaman nesnesini belirli bir formata dönüştürür.

        Args:
            zaman (datetime): Dönüştürülecek zaman nesnesi.

        Returns:
            str: Belirli (AFAD'ın istem stiline uygun) formata dönüştürülmüş zaman metni.
        """
        return f"{zaman.strftime('%x').replace('/', '-')}%20{zaman.strftime('%X')}"

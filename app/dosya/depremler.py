"""
Depremler Modülü

Bu modül, deprem verilerini işlemek için gerekli sınıf ve fonksiyonları içerir.

Classes:
    Depremler: Depremler verilerini işlemek için bir sınıf.
"""
import json
from app.internet.baglanti import Baglanti


class Depremler:
    """
    Depremler Sınıfı

    Bu sınıf, deprem verilerini işlemek için gerekli yöntemleri sağlar.

    Methods:
        __init__: Depremler sınıfının başlatıcı yöntemi.
        json_veriler: JSON formatındaki deprem verilerini işler.
        duzenli_veriler: İşlenmiş deprem verilerini düzenli bir şekilde yazdırır.
    """

    def __init__(self):
        """
        Depremler sınıfının başlatıcı yöntemi.
        """
        self._json = Baglanti()

    def __json_veri_yukle(self):
        """
        JSON veri yükleme yöntemi.

        Returns:
            dict: Yüklü JSON verileri
        """
        return json.loads(self._json.indir())

    def json_veriler(self) -> list | str:
        """
        JSON formatındaki deprem verilerini işler.

        Returns:
            list | str: İşlenmiş deprem verileri veya hata mesajı
        """
        try:
            depremler = []
            for event in self.__json_veri_yukle():
                depremler.append([
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

    def duzenli_veriler(self, limit=7):
        """
        İşlenmiş deprem verilerini düzenli ve sıralı şekilde yazdırır.

        Args:
            limit (int): Yazdırılacak maksimum veri sayısı. Varsayılan değer 7.

        Returns:
            None
        """
        print("Tarih ve Saat", "Konum", "Şiddet", "Enlem", "Boylam", "Derinlik", sep=" - ")

        veriler = self.json_veriler()[:limit]
        for veri in veriler:
            print(*veri, sep=" - ")

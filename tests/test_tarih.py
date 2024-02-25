"""
TestSon24Saat Sınıfı

Bu sınıf, Tarih sınıfının son_24_saat metodu için unittest'lerini içerir.

Methods:
    test_baslangic_ve_bitis_tarihi_dondur: Tarih sınıfının son_24_saat metodu için doğrulama yapar.
"""
import unittest
from app.dosya.tarih import Tarih


class TestSon24Saat(unittest.TestCase):
    """
    TestSon24Saat Sınıfı

    Bu sınıf, Tarih sınıfının son_24_saat metodu için unittest'lerini içerir.
    """

    def test_baslangic_ve_bitis_tarihi_dondur(self):
        """
        Tarih sınıfının son_24_saat metodu için doğrulama yapar.

        Returns:
            None
        """
        sonuc = Tarih().son_24_saat()

        hedef_regex = (r'start=\d{2}-\d{2}-\d{2}%20\d{2}:\d{2}:\d{2}'
                       r'&end=\d{2}-\d{2}-\d{2}%20\d{2}:\d{2}:\d{2}')

        self.assertIsInstance(sonuc, str)
        self.assertRegex(sonuc, hedef_regex)

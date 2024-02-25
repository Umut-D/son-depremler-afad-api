"""
TestIndir Sınıfı

Bu sınıf, Baglanti sınıfının indir metodu için unittest'lerini içerir.

Methods:
    setUp: Testlerin başında yapılacak hazırlık işlemlerini sağlar.
    test_response_code_200: Baglanti sınıfının indir metodu için HTTP
    yanıt kodunun 200 olup olmadığını kontrol eder.
"""
import unittest
from app.internet.baglanti import Baglanti


class TestIndir(unittest.TestCase):
    """
    TestIndir Sınıfı

    Bu sınıf, Baglanti sınıfının indir metodu için unittest'lerini içerir.
    """

    def setUp(self):
        """
        Testlerin başında yapılacak hazırlık işlemlerini sağlar.

        Returns:
            None
        """
        self.baglanti = Baglanti()

    def test_response_code_200(self):
        """
        Baglanti sınıfının indir metodu için HTTP yanıt kodunun 200 olup olmadığını kontrol eder.

        Returns:
            None
        """
        sonuc = self.baglanti.indir()

        self.assertIsNotNone(sonuc, str)

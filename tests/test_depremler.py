"""
TestDepremler Sınıfı

Bu sınıf, Depremler sınıfının unittest'lerini içerir.

Methods:
    test_json_veri: Depremler sınıfının json_veriler metodu için doğrulama yapar.
"""

import unittest
from app.dosya.depremler import Depremler


class TestDepremler(unittest.TestCase):
    """
    TestDepremler Sınıfı

    Bu sınıf, Depremler sınıfının unittest'lerini içerir.
    """

    def test_json_veri(self):
        """
        Depremler sınıfının json_veriler metodu için doğrulama yapar.

        Returns:
            None
        """
        depremler = Depremler()

        json_veriler = depremler.json_veriler()

        self.assertIsInstance(json_veriler, list)

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import unittest
from app.dosya.tarih import Tarih


class TestSon24Saat(unittest.TestCase):
    def test_baslangic_ve_bitis_tarihi_dondur(self):
        sonuc = Tarih().son_24_saat()

        hedef_regex = (
            r'start=\d{2}-\d{2}-\d{2}%20\d{2}:\d{2}:\d{2}'
            r'&end=\d{2}-\d{2}-\d{2}%20\d{2}:\d{2}:\d{2}')

        self.assertIsInstance(sonuc, str)
        self.assertRegex(sonuc, hedef_regex)

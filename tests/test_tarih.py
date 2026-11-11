# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import unittest
from app.dosya.tarih import Tarih


class TestSon24Saat(unittest.TestCase):
    def test_baslangic_ve_bitis_tarihi_dondur(self):
        sonuc = Tarih().son_24_saat()

        hedef_regex = (
            r'start=\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}'
            r'&end=\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}')

        self.assertIsInstance(sonuc, str)
        self.assertRegex(sonuc, hedef_regex)


class TestAfadSaatDonusumu(unittest.TestCase):
    def test_utc_tarihini_turkiye_saatine_cevirir(self):
        sonuc = Tarih.afad_utc_turkiye_saatine("2026-11-10T12:36:18")

        self.assertEqual(sonuc, "2026-11-10 15:36:18")

    def test_saat_dilimli_girdiyi_turkiye_saatine_cevirir(self):
        sonuc = Tarih.afad_utc_turkiye_saatine("2026-11-10T13:36:18+01:00")

        self.assertEqual(sonuc, "2026-11-10 15:36:18")

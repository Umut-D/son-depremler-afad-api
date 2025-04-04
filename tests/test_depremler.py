# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import unittest
from app.dosya.depremler import Depremler


class TestDepremler(unittest.TestCase):

    def test_json_veri(self):
        depremler = Depremler()

        json_veriler = depremler.tum_veriler()

        self.assertIsInstance(json_veriler, list)

    def test_tablo_veri(self):
        depremler = Depremler()

        tablo_veriler = depremler.tablo_veriler()

        self.assertIsInstance(tablo_veriler, str)

    def test_duzenli_veri(self):
        depremler = Depremler()

        duzenli_veriler = depremler.duzenli_veriler()

        self.assertIsInstance(duzenli_veriler, str)

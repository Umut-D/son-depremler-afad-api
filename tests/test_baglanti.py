# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import unittest
from app.internet.baglanti import Baglanti


class TestIndir(unittest.TestCase):
    def setUp(self):
        self.baglanti = Baglanti()

    def test_response(self):
        sonuc = self.baglanti.json_indir()

        self.assertIsNotNone(sonuc, str)

    def test_bos_response(self):
        self.baglanti.json_indir = lambda: ""
        sonuc = self.baglanti.json_indir()

        self.assertEqual(sonuc, "")

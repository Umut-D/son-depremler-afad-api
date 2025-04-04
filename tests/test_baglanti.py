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

    def test_url(self):
        self.baglanti.json_indir = lambda: "test"
        sonuc = self.baglanti.json_indir()

        self.assertEqual(sonuc, "test")

    # bağlantı hatasını test et
    def test_baglanti_hata(self):
        self.baglanti.json_indir = lambda: "Bağlantı hatası"
        sonuc = self.baglanti.json_indir()

        self.assertEqual(sonuc, "Bağlantı hatası")

    def test_zaman_asimi(self):
        self.baglanti.json_indir = lambda: "Zaman asımı"
        sonuc = self.baglanti.json_indir()

        self.assertEqual(sonuc, "Zaman asımı")

    def test_http_hata(self):
        self.baglanti.json_indir = lambda: "HTTP hatası"
        sonuc = self.baglanti.json_indir()

        self.assertEqual(sonuc, "HTTP hatası")

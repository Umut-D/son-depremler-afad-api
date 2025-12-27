## Son Depremler AFAD API (1.12)
AFAD'ın resmi web sayfasından son 24 saatte Türkiye'de olan depremleri çeken API.

### ✨ Özellikler

* **Güncel Veri:** AFAD'ın [Ulusal Deprem Gözlem Merkezi](https://deprem.afad.gov.tr/last-earthquakes.html) tarafından yayınlanan en son deprem verilerini kullanır.
* **Detaylı Bilgi:** Her deprem için tarih, saat, enlem, boylam, derinlik, büyüklük (tipiyle birlikte - örn. ML, Mw) ve meydana geldiği yer (ilçe, il) bilgilerini içerir.
* **Basit Kullanım:** Kolay kurulum ve çalıştırma adımları.
* **Esnek Çıktı:** Verileri doğrudan konsola yazdırabilir [veya JSON formatında bir API endpoint'i üzerinden sunabilir - eğer API özelliği varsa bu kısmı ekleyin].
* **Açık Kaynak:** MIT Lisansı ile lisanslanmıştır, katkılarınıza açıktır.


### 🚀 Nasıl kullanılır:
_Paketi kurduktan sonra aşağıdaki import işlemini yapınız:_ <br>

```python
from app.dosya.depremler import Depremler
```
**"Tarih ve Saat, Konum, Şiddet, Enlem, Boylam, Derinlik"** şeklinde olan verileri;<br>

_dizi olarak göstermek için -> [['2025-03-02 01:35:45', 'Dulkadiroğlu (Kahramanmaraş)', '1.8', '37.44472', '37.1425', '7']]..._<br>

```python
depremler = Depremler()
print(depremler.tum_veriler())
```

_satır satır ve istenen sayıda yazdırmak için -> 2025-03-02 01:35:45 - Dulkadiroğlu (Kahramanmaraş) - 1.8 - 37.44472 - 37.1425 - 7_<br>

```python
depremler = Depremler()
print(depremler.duzenli_veriler()())
```

tablo halinde ve istenen sayıda yazdırmak için:
<div style="overflow-x: auto; margin: -10px 0;">
<pre style="background-color: #f6f8fa; padding: 16px; border-radius: 6px; border: 1px solid #d0d7de;">
+---------------------+------------------------------+--------+----------+-----------+-----------+
| Tarih ve Saat       | Konum                        | Şiddet | Enlem    | Boylam    | Derinlik  |
+=====================+==============================+========+==========+===========+===========+
| 2025-03-02 01:35:45 | Dulkadiroğlu (Kahramanmaraş) | 1.8    | 37.4447  | 37.1425   | 7         |
+---------------------+------------------------------+--------+----------+-----------+-----------+
</pre>
</div>

```python
depremler = Depremler()
print(depremler.tablo_veriler())
```

### ⚙️ Bağımlılıklar
Projenin çalışması için gereken ana Python kütüphaneleri;

* **urllib3**: HTTP istemleri yapmak için.
* **tabulate**: Tablo olarak görüntüleme yapmak için.

### PyPI.org Link:
https://pypi.org/project/son-depremler-afad-api/1.1.2/

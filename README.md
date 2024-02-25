## Son Depremler AFAD API
AFAD'ın resmi web sayfasından son 24 saatte Türkiye'de olan depremleri çeken API.

### Nasıl kullanılır:
_Paketi kurduktan sonra aşağıdaki import işlemini yapınız:_ <br>

```python
from app.dosya.depremler import Depremler
```
**"Tarih ve Saat, Konum, Şiddet, Enlem, Boylam, Derinlik"** şeklinde olan verileri;<br>

_dizi olarak göstermek için -> [['2024-02-25 08:56:38', 'Serik (Antalya)', '2.6', '37.24139', '30.95028', '21.78']]..._<br>

```python
depremler = Depremler()
json_veriler = depremler.json_veriler()
```

_satır satır yazdırmak için -> 2024-02-25 08:56:38 - Serik (Antalya) - 2.6 - 37.24139 - 30.95028 - 21.78_<br>

```python
depremler = Depremler()
depremler.duzenli_veriler()
```

### PyPI.org Link:
https://pypi.org/project/son-depremler-afad-api/1.0.0/

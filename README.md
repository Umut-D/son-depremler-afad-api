## Son Depremler AFAD API
AFAD'ın resmi web sayfasından son 24 saatte Türkiye'de olan depremleri çeken API.

### Nasıl kullanılır:
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

_tablo halinde ve istenen sayıda yazdırmak için (Tablo hali buradan çok daha güzel görünüyor) ->
+---------------------+---------------------------+--------+--------+---------+-----------+
| Tarih ve Saat       | Konum                        | Şiddet   | Enlem   | Boylam   | Derinlik   |
+=====================+===========================+========+========+=========+===========+
| 2025-03-02 01:35:45 | Dulkadiroğlu (Kahramanmaraş) | 1.8      | 37.4447 | 37.1425  | 7          |
<br>

```python
depremler = Depremler()
print(depremler.tablo_veriler())
```

### PyPI.org Link:
https://pypi.org/project/son-depremler-afad-api/1.1.0/

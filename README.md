# Son Depremler AFAD API

AFAD'ın resmi web sayfasında yayımlanan son 24 saatlik Türkiye deprem verilerini Python ile almanızı sağlar.

## Özellikler

- Depremin tarihini, saatini, konumunu, büyüklüğünü, enlem ve boylamını, derinliğini sunar.
- Verileri liste, satır satır metin veya tablo olarak döndürür.
- Son N depremi ve minimum büyüklük eşiğine göre sonuçları süzer.
- AFAD'ın yayımladığı verileri kullanır; deprem verisini kendisi üretmez.

## Kurulum

```bash
python -m pip install son-depremler-afad-api
```

Paket, tablo çıktısı için gereken `tabulate` bağımlılığını otomatik kurar.

## Hızlı başlangıç

```python
from app.dosya.depremler import Depremler

depremler = Depremler()
print(depremler.duzenli_veriler())
```

## Çıktı biçimleri

### Liste

```python
depremler = Depremler()
print(depremler.tum_veriler())
```

### Tablo

```python
depremler = Depremler()
print(depremler.tablo_veriler())
```

### Satır satır metin

```python
depremler = Depremler()
print(depremler.duzenli_veriler())
```

Not: `duzenli_veriler()` başlık satırını kendisi ekrana yazar, döndürdüğü metin yalnızca deprem satırlarını içerir. Yukarıdaki `print` örneği ikisini birlikte gösterir.

## Sonuçları sınırlandırma

`limit`, en yeni kaç depremin alınacağını belirtir. `minimum_buyukluk`, bu değer **ve üzerindeki** depremleri tutar. Önce büyüklük filtresi, sonra sonuç sayısı uygulanır. Parametre adları ve açıklamaları editörün IntelliSense yardımında da görünür.

```python
# Son 6 deprem
depremler.tum_veriler(6)

# Büyüklüğü en az 3.0 olan en yeni 6 deprem (3.0 dahil)
depremler.tum_veriler(6, 3)

# Aynı seçenekler metin ve tablo çıktısında da kullanılabilir
print(depremler.duzenli_veriler(6, 3))
print(depremler.tablo_veriler(6, 3))
```

`3` eşiğine eşit depremler dahildir; yalnızca 3.0'ın altındakiler elenir. `duzenli_veriler()` varsayılan olarak 7, `tablo_veriler()` 10 kayıt gösterir. `tum_veriler()` varsayılan olarak tüm kayıtları döndürür. Tablo sayısal değerleri yuvarlamadan, kaynak verideki basamakları koruyarak gösterir.

## Saat dilimi

AFAD API tarihleri UTC olarak verir. Kütüphane bunları cihazın saat diliminden bağımsız biçimde Türkiye saatine (UTC+03:00) çevirerek gösterir. Örneğin API'deki `2026-11-10 12:36:18` değeri çıktıda `2026-11-10 15:36:18` olur. Liste, düzenli metin ve tablo başlıklarında saat dilimi `UTC+03:00` olarak belirtilir.

## Gereksinimler

- Python 3.10 veya üzeri
- `tabulate` (paket kurulurken otomatik yüklenir)
- `tzdata` (Türkiye saat dilimi verisi; tüm işletim sistemlerinde otomatik yüklenir)
- `urllib` (Python standart kütüphanesi; ayrıca yüklenmez)

## 1.3.0 sürümündeki değişiklikler

- Son N deprem ve minimum büyüklük filtreleri liste, metin ve tablo metotlarına eklendi.
- API parametreleri tür ipuçları ve IntelliSense açıklamalarıyla belgelendi.
- Kurulum, tablo çıktısı için `tabulate` bağımlılığını otomatik yükler.
- Python 3.10 ve üzeri desteklenir.
- AFAD sorgu aralığı UTC ile hesaplanır; dönen deprem saatleri Türkiye saati (UTC+03:00) olarak gösterilir. Bağlantı, boş cevap ve beklenmeyen HTTP durumları daha anlaşılır biçimde ele alınır.
- Kullanılmayan `urllib3` bağımlılığı kaldırıldı; HTTP isteklerinde Python'ın standart `urllib` kütüphanesi kullanılır.
- README'deki kullanım örneği düzeltildi.

## Bağlantılar

- [PyPI paket sayfası](https://pypi.org/project/son-depremler-afad-api/)
- [GitHub deposu](https://github.com/umut-d/son-depremler-afad-api)
- [AFAD son depremler sayfası](https://deprem.afad.gov.tr/last-earthquakes.html)

## Lisans

MIT lisansı. Ayrıntılar için depodaki `LICENCE` dosyasına bakın.

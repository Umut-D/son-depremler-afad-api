# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from app.dosya.depremler import Depremler

depremler = Depremler()

print(depremler.tum_veriler())
print(depremler.duzenli_veriler())
print(depremler.tablo_veriler())

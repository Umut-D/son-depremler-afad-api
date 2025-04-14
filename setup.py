# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

"""
son-depremler-afad-api paketi için kurulum betiği.

Bu betik, setuptools kullanarak paketi dağıtım için hazırlar. Paketin adı, sürümü, açıklaması,
yazar bilgisi ve lisans gibi meta verileri sağlar. Ayrıca paket içeriğini, bağımlılıkları ve diğer
yapılandırma seçeneklerini belirtir.

Fonksiyonlar:
    readme: README.md dosyasının içeriğini okur ve bir dize olarak döndürür.
"""
from setuptools import find_packages, setup


def readme() -> str:
    with open("README.md", "r", encoding="utf-8") as oku:
        return oku.read()


setup(
    name="son-depremler-afad-api",
    version="1.1.2",
    description="AFAD'ın resmi web sayfasından son 24 saatte Türkiye'de olan depremleri çeken API",
    packages=find_packages(exclude=["tests"]),
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/umut-d/son-depremler-afad-api",
    author="Umut D.",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    extras_require={
        "dev": ["twine>=4.0.2"],
    },
    python_requires=">=3",
)

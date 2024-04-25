#!/usr/bin/env python3

from setuptools import setup

setup(
    name='testpython',
    version='0.1.0',
    packages=['testpython'],  # Paketinizin içerdiği modülleri listeleyin
    url='https://github.com/AbdulmelikKalkan/testpython',  # GitHub deponuzun URL'sini girin
    license='MIT',
    author='Abdulmelik Kalkan',
    author_email='abdulmelikkalkan@gmail.com',
    description='Örnek Python paketi',
    long_description='Bu paket, Python paket geliştirmeye başlamak için bir örnektir.',
    install_requires=[],  # Gerekli bağımlılıkları listeleyin
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

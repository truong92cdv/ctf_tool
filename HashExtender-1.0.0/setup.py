#!/usr/bin/python
from distutils.core import setup
from distutils.extension import Extension
module = Extension(name = "hashext", sources = ['hashext.c', ])
setup(name = 'HashExtender', 
		version = '1.0.0',
		description = 'Module implements hash length extension attack against MD5 algorithm',
		author = 'Daniel Sadyrin',
		author_email = 'cyberguru007@yandex.ru',
		ext_modules = [module]
)

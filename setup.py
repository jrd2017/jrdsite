# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in stockmarket/__init__.py
from linefood import __version__ as version

setup(
	name='jrdsite',
	version=version,
	description='jrdsite application ',
	author='jeffreyramirez',
	author_email='admin@jeffreyramirez.net',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

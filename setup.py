#!/usr/bin/env python

from distutils.core import setup

setup(name='crunchbox',
	author='lyrae',
	version='0.0.1',
	py_modules=['dialog_save', 'layout', 'base'],
	packages=['apps'],
	package_dir={'': 'src'},
)


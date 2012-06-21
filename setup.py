Ignore this file.
To run crunchbox, just do
$ python /path/to/crunchbox/src/crunchbox.py
(you might have to do $ python2 if your system loads python3 by default)
"""
#!/usr/bin/env python
from distutils.core import setup

setup(name='crunchbox',
	author='lyrae',
	version='0.0.1',
	py_modules=['dialog_save', 'layout', 'base'],
	packages=['apps'],
	package_dir={'': 'src'},
)
"""

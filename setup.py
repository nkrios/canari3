#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages

# sys.path.insert(0, 'src')
#
# import canari

scripts = [
    'src/scripts/canari',
    'src/scripts/dispatcher',
]

if os.name == 'posix':
    scripts.extend(
        [
            'src/scripts/pysudo'
        ]
    )

extras = [
    'readline'
]

requires = [
    'mr.bob',
    'argparse',
    'flask',
    'Twisted',
    'safedexml'
]

if os.name == 'nt':
    scripts += ['%s.bat' % s for s in scripts]

setup(
    name='canari',
    author='Nadeem Douba',
    version='3.0',
    author_email='ndouba@gmail.com',
    description='Rapid transform development and transform execution framework for Maltego.',
    license='GPL',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    scripts=scripts,
    zip_safe=False,
    install_requires=requires,
    dependency_links=[]
)

#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='py3algorithm',
    version='0.0.1',
    author='Priyank Chheda',
    author_email='p.chheda29@gmail.com',
    description='Python Algorithm Library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://www.github.com/x899/py3algorithm',
    packages=find_packages('src'),
    package_dir={'': 'src'},
)

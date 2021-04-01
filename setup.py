# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='restframework-serializer-permissions',
    version='0.0.0',
    author='Manfred Kaiser',
    author_email='manfred.kaiser@ssh-mitm.at',
    description='permissions for django restframework serializers and fields',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    url="https://github.com/manfred-kaiser/restframework-serializer-permissions",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ]
)

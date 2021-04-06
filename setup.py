# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='restframework-serializer-permissions',
    version='0.0.1',
    author='Manfred Kaiser',
    author_email='manfred.kaiser@ssh-mitm.at',
    description='permission based serializing for django restframework',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    url="https://github.com/manfred-kaiser/restframework-serializer-permissions",
    install_requires=[
        'django>=2.1',
        'djangorestframework>=3.12',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ]
)

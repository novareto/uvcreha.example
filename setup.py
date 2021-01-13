#!/usr/bin/env python

"""The setup script."""

import codecs
import os
import re

from setuptools import setup, find_packages

requirements=['docmanager']

setup(
    name="uvcreha.example",
    author="Christian Klinger",
    author_email="ck@novareto.de",
    version="0.0.1",
    description="",
    long_description="",
    long_description_content_type="text/x-rst",
    license="GPL",
    url="http://www.novareto.de",
    entry_points={
        'docmanager.plugins': [
            'example = uvcreha.example'
        ],
    },
    install_requires=requirements,
    include_package_data=True,
    packages=find_packages(include=['uvcreha.example']),
    setup_requires=[],
    test_suite='tests',
    zip_safe=False,
)

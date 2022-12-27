# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 15 Feb 2020
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""
from setuptools import setup

setup(
    name='docapi',
    author='S.M. Sabbir Amin',
    author_email='<sabbiramin.cse11ruet@gmail.com>',
    version='0.7.0',
    description='A Pythonic API Documentation and Mock Server Generation Utility',
    packages=["docapi" ],
    license='GNU GPL v3 or later',
    install_requires=[
        'setuptools == 65.5.1',
    ],
    package_data={
    },
    data_files=[
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)

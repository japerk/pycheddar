#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='pycheddar',
    version='0.9.3',
    description='A Python wrapper for CheddarGetter.',
    author='FeedMagnet',
    url='http://www.feedmagnet.com/blog/cheddargetter-for-python-and-django/',
    requires=['httplib2',],
    packages=['pycheddar'],
)

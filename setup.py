#!/usr/bin/python -u
#
# Consistent hashing
#
# Copyright (c) 2010 by Joachim Bauch, mail@joachim-bauch.de
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# $Id$
#
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

    from setuptools import setup

import version

descr = "Consistent hashing for Python"
long_descr = open('README.txt').read().strip()

setup(
    name = "python-continuum",
    version = version.get_git_version(),
    description = descr,
    author = "Joachim Bauch",
    author_email = "mail@joachim-bauch.de",
    url = "http://www.joachim-bauch.de/projects/python-continuum/",
    download_url = "http://pypi.python.org/pypi/python-continuum/",
    license = 'LGPL',
    keywords = "consistent hashing",
    long_description = long_descr,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
    ],
    py_modules = ['continuum'],
    test_suite = 'tests.suite',
)

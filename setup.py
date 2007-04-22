##############################################################################
#
# Copyright (c) 2006 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for zope.app.renderer package

$Id$
"""

import os

from setuptools import setup, find_packages, Extension

setup(name='zope.app.renderer',
      version = '3.4.0a1',
      url='http://svn.zope.org/zope.app.renderer',
      license='ZPL 2.1',
      description='Zope renderer',
      author='Zope Corporation and Contributors',
      author_email='zope3-dev@zope.org',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['zope', 'zope.app'],
      extras_require = dict(test=['zope.app.testing']),
      install_requires=['setuptools',
                        'docutils',
                        'zope.component',
                        'zope.configuration',
                        'zope.i18nmessageid',
                        'zope.interface',
                        'zope.publisher',
                        'zope.schema',
                        'zope.structuredtext',
                        ],
      include_package_data = True,
      zip_safe = False,
      )

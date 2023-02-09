##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
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
# This package is developed by the Zope Toolkit project, documented here:
# https://zopetoolkit.readthedocs.io/
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.app.renderer package
"""
import os

from setuptools import find_packages
from setuptools import setup


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(name='zope.renderer',
      version='4.0.0.dev0',
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.dev',
      description='Text Renderer Framework',
      long_description=(
          read('README.txt')
          + '\n\n' +
          read('CHANGES.txt')
      ),
      keywords="zope3 renderer text rest rst stx",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: Implementation :: CPython',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: Zope :: 3',
      ],
      url='https://github.com/zopefoundation/zope.renderer',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['zope'],
      python_requires='>=3.7',
      extras_require=dict(
          test=[
              'zope.testing',
              'zope.testrunner',
          ]
      ),
      install_requires=[
          'setuptools',
          'docutils>=0.5',
          'roman',
          'zope.component',
          'zope.configuration',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.publisher',
          'zope.schema',
          'zope.structuredtext',
      ],
      tests_require=[
          'zope.testing',
      ],
      test_suite='zope.renderer.tests.test_suite',
      include_package_data=True,
      zip_safe=False,
      )

##############################################################################
#
# Copyright (c) 2003 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Tests for Global Wiki Source Type Service.

$Id$
"""
import unittest

from zope.app import zapi
from zope.app.tests import ztapi
from zope.app.renderer import SourceFactory
from zope.app.renderer.interfaces import ISource
from zope.app.renderer.vocabulary import SourceTypeVocabulary
from zope.component.interfaces import IFactory
from zope.component.tests.placelesssetup import PlacelessSetup
from zope.schema.interfaces import \
     ITokenizedTerm, IVocabulary, IVocabularyTokenized


class IFoo(ISource):
    """Source marker interface"""

FooFactory = SourceFactory(IFoo, 'Foo', 'Foo Source')

class IFoo2(ISource):
    """Source marker interface"""

Foo2Factory = SourceFactory(IFoo2, 'Foo2', 'Foo2 Source')

# XXX the vocabulary uses SimpleVocabulary now, so these tests are a bit 
# redundant.  Leaving them in as confirmation that the replacement function 
# works identically to the old custom vocabulary.
class SourceTypeVocabularyTest(PlacelessSetup, unittest.TestCase):

    def setUp(self):
        super(SourceTypeVocabularyTest, self).setUp()
        ztapi.provideUtility(IFactory, FooFactory, 'zope.source.Foo')
        ztapi.provideUtility(IFactory, Foo2Factory, 'zope.source.Foo2')
        self.vocab = SourceTypeVocabulary(None)

    def test_Interface(self):
        self.failUnless(IVocabulary.providedBy(self.vocab))
        self.failUnless(IVocabularyTokenized.providedBy(self.vocab))

    def test_contains(self):
        self.failUnless('zope.source.Foo' in self.vocab)
        self.failIf('zope.source.Foo3' in self.vocab)

    def test_iter(self):
        self.failUnless(
            'zope.source.Foo' in [term.value for term in self.vocab])
        self.failIf(
            'zope.source.Foo3' in [term.value for term in iter(self.vocab)])

    def test_len(self):
        self.assertEqual(len(self.vocab), 2)

    def test_getQuery(self):
        self.assertEqual(self.vocab.getQuery(), None)

    def test_getTerm(self):
        self.assertEqual(self.vocab.getTerm('zope.source.Foo').title, 'Foo')
        self.assertRaises(
            LookupError, self.vocab.getTerm, ('zope.source.Foo3',))

    def test_getTermByToken(self):
        vocab = self.vocab
        self.assertEqual(vocab.getTermByToken('zope.source.Foo').title, 'Foo')
        self.assertRaises(
            LookupError, vocab.getTermByToken, ('zope.source.Foo3',))

def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(SourceTypeVocabularyTest),
        ))

if __name__ == '__main__':
    unittest.main()

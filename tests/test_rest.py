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
"""Structured Text Tests - StructuredText Source, HTML Renderer

$Id: test_rest.py,v 1.1 2003/07/31 17:59:41 srichter Exp $
"""
import unittest

from zope.publisher.browser import TestRequest

from zope.app.interfaces.renderer import \
     IReStructuredTextSource, IHTMLRenderer
from zope.app.renderer.rest import \
     ReStructuredTextSource, ReStructuredTextToHTMLRenderer


class ReStructuredTextTest(unittest.TestCase):

    def setUp(self):
        self._source = ReStructuredTextSource(u'This\n is source.')

    def test_Interface(self):
        self.failUnless(IReStructuredTextSource.isImplementedBy(self._source))

    def test_createComment(self):
        self.assertEqual(comment,
                         self._source.createComment('This is a Comment.', 2,
                                                    'srichter',
                                                    '04/12/2003 12:00:00'))
        self.assertEqual(first_comment,
                         self._source.createComment('This is a Comment.', 1,
                                                    'srichter',
                                                    '04/12/2003 12:00:00'))


class HTMLRendererTest(unittest.TestCase):

    def setUp(self):
        self._source = ReStructuredTextSource(u'This is source.\n')
        self._renderer = ReStructuredTextToHTMLRenderer(self._source,
                                                        TestRequest())

    def test_Interface(self):
        self.failUnless(IHTMLRenderer.isImplementedBy(self._renderer))

    def test_render(self):
        self.assertEqual('<div class="document">\nThis is source.</div>\n',
                         self._renderer.render(None))
        comment = self._source.createComment('This is a Comment.', 1,
                                             'srichter',
                                             '04/12/2003 12:00:00')
        self._renderer.context = ReStructuredTextSource(self._source+comment)

        self.assertEqual(rendered_source_comment, self._renderer.render(None))


comment = '''

Comment #2 by **srichter** (04/12/2003 12:00:00)

This is a Comment.'''

first_comment = '''
----------

Comment #1 by **srichter** (04/12/2003 12:00:00)

This is a Comment.'''

rendered_source_comment = '''<div class="document">\n<p>This is source.</p>
<hr />
<p>Comment #1 by <strong>srichter</strong> (04/12/2003 12:00:00)</p>
<p>This is a Comment.</p>
</div>
'''


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(ReStructuredTextTest),
        unittest.makeSuite(HTMLRendererTest),
        ))

if __name__ == '__main__':
    unittest.main()

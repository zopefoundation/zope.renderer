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
"""Structured Text Renderer Classes

$Id: stx.py,v 1.5 2004/03/19 20:26:32 srichter Exp $
"""
import re

from zope.interface import implements
from zope.app.publisher.browser import BrowserView
from zope.structuredtext.document import Document
from zope.structuredtext.html import HTML

from zope.app.renderer.interfaces import ISource, IHTMLRenderer
from zope.app.renderer import SourceFactory


class IStructuredTextSource(ISource):
    """Marker interface for a structured text source. Note that an
    implementation of this interface should always derive from unicode or
    behave like a unicode class."""

StructuredTextSourceFactory = SourceFactory(IStructuredTextSource)


class StructuredTextToHTMLRenderer(BrowserView):
    r"""A view to convert from Plain Text to HTML.

    Example::

      >>> from zope.publisher.browser import TestRequest
      >>> source = StructuredTextSourceFactory(u'This is source.')
      >>> renderer = StructuredTextToHTMLRenderer(source, TestRequest())
      >>> renderer.render()
      '<p>This is source.</p>\n'

    """ 
    implements(IHTMLRenderer)
    __used_for__ = IStructuredTextSource

    def render(self):
        "See zope.app.interfaces.renderer.IHTMLRenderer"
        doc = Document()(str(self.context))
        html = HTML()(doc)

        # strip html & body added by some zope versions
        html = re.sub(
            r'(?sm)^<html.*<body.*?>\n(.*)</body>\n</html>\n',r'\1', html)

        return html

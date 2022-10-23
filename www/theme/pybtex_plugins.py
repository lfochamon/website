#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from pybtex.database import Person
from pybtex.style.formatting import unsrt
from pybtex.style.template import tag, words, href, field, optional, join

class PelicanStyle(unsrt.Style):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.site_author = Person('L. F. O. Chamon')
        self.site_author_star = Person('L. F. O. Chamon*')

        # Allows to apply special formatting to a specific author.
        def format_name(person, abbr=False):
            if person == self.site_author:
                return tag('strong') [self.name_style.format(person, abbr)]
            elif person == self.site_author_star:
                return join [ tag('strong') [self.name_style.format(self.site_author, abbr)], '*' ]
            else:
                return self.name_style.format(person, abbr)

        self.format_name = format_name

        def format_web_refs(e):
            pass

        self.format_web_refs = format_web_refs

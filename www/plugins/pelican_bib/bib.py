# -*- coding: utf-8 -*-

import sys, logging
from io import StringIO

from pybtex.database.input.bibtex import Parser
from pybtex.database.output.bibtex import Writer
from pybtex.database import BibliographyData, PybtexError
from pybtex.backends import html

from pybtex.database import Person
from pybtex.style.formatting import BaseStyle, unsrt
from pybtex.style.template import tag, words, href, field, optional, join

from pelican import signals

logger = logging.getLogger(__name__)


class PelicanStyle(unsrt.Style):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.site_author = Person("L. F. O. Chamon")
        self.site_author_star = Person("L. F. O. Chamon*")

        # Allows to apply special formatting to a specific author.
        def format_name(person, abbr=False):
            if person == self.site_author:
                return tag("strong")[self.name_style.format(person, abbr)]
            elif person == self.site_author_star:
                return join[tag("strong")[self.name_style.format(self.site_author, abbr)], "*"]
            else:
                return self.name_style.format(person, abbr)

        if kwargs["highlight"]:
            self.format_name = format_name

        # Skip URL
        def format_web_refs(e):
            pass

        self.format_web_refs = format_web_refs


def parse_pubs(generator, refs_file, highlight=True):
    kwargs = generator.settings.get("PUBLICATIONS_STYLE_ARGS", {})
    style = PelicanStyle(highlight=highlight, **kwargs)

    bibdata_all = Parser().parse_file(refs_file)

    publications = []
    publications_lists = {}
    publications_untagged = []

    split_by = generator.settings.get("PUBLICATIONS_SPLIT_BY", None)
    untagged_title = generator.settings.get("PUBLICATIONS_UNTAGGED_TITLE", None)

    # format entries
    html_backend = html.Backend()
    formatted_entries = style.format_entries(bibdata_all.entries.values())

    for formatted_entry in formatted_entries:
        key = formatted_entry.key
        entry = bibdata_all.entries[key]

        tags = []
        if split_by:
            tags = entry.fields.get(split_by, [])

            # parse to list, and trim each string
            if tags:
                tags = [tag.strip() for tag in tags.split(",")]

                # create keys in publications_lists if at least one
                # tag is given
                for tag in tags:
                    publications_lists[tag] = publications_lists.get(tag, [])

        # render the bibtex string for the entry
        bib_buf = StringIO()
        bibdata_this = BibliographyData(entries={key: entry})
        Writer().write_stream(bibdata_this, bib_buf)
        text = formatted_entry.text.render(html_backend)

        entry_tuple = {}
        entry_tuple["key"] = key
        entry_tuple["text"] = text
        entry_tuple["bibtex"] = bib_buf.getvalue()

        for key, value in entry.fields.items():
            if type(value) is str and value.startswith("\\url"):
                entry_tuple[key] = value[5:-1]
            else:
                entry_tuple[key] = value

        publications.append(entry_tuple)

        for tag in tags:
            publications_lists[tag].append(entry_tuple)

        if not tags and untagged_title:
            publications_untagged.append(entry_tuple)

    # append untagged list if title is given
    if untagged_title and publications_untagged:
        publications_lists[untagged_title] = publications_untagged

    return publications, publications_lists


def global_publications(generator):
    if "PUBLICATIONS_SRC" in generator.settings:
        refs_file = generator.settings["PUBLICATIONS_SRC"]

        try:
            publications, publications_lists = parse_pubs(generator, refs_file, highlight=True)
        except ImportError as e:
            logger.warn(f"`pelican_bib` failed to load {str(e)}")
            return
        except PybtexError as e:
            logger.warn("`pelican_bib` failed to parse file %s: %s" % (refs_file, str(e)))
            return
        except TypeError as e:
            logger.warn(
                f"PelicanStyle must be a subclass of pybtex.style.formatting.BaseStyle {str(e)}"
            )
            return

        # output
        generator.context["publications"] = publications
        generator.context["publications_lists"] = publications_lists


def tutorial_publications(generator, content):
    # read metadata
    if "bibtex" in content.metadata:
        refs_file = content.metadata["bibtex"]

        try:
            publications, publications_lists = parse_pubs(generator, refs_file, highlight=False)
        except ImportError as e:
            logger.warn(f"`pelican_bib` failed to load {str(e)}")
            return
        except PybtexError as e:
            logger.warn("`pelican_bib` failed to parse file %s: %s" % (refs_file, str(e)))
            return
        except TypeError as e:
            logger.warn(
                f"PelicanStyle must be a subclass of pybtex.style.formatting.BaseStyle {str(e)}"
            )
            return

        # output
        content.publications = publications
        content.publications_lists = publications_lists


def register():
    signals.generator_init.connect(global_publications)
    signals.page_generator_write_page.connect(tutorial_publications)

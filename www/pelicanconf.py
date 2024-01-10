#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from datetime import date, datetime
import os

AUTHOR = 'Luiz Chamon'
SITENAME = 'Luiz Chamon'
SITETITLE = 'Luiz Chamon'
SITEEMAIL = 'l%75%&#54;9&#37;7&#65;&#46;c&#37;6&#56;&#97;&#37;6Don&#64;si%6D&#37;&#55;&#52;&#101;ch&#46;u&#37;6E&#37;69-stutt&#103;art&#46;&#100;%&#54;5'
CURRENTYEAR = date.today().year
SITEURL = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'output')

PATH = 'content'

TIMEZONE = 'EST'

GOOGLE_ANALYTICS = False

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%b %d, %Y'

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
PAGE_ORDER_BY = 'date'

OUTPUT_RETENTION = ['.git']
DELETE_OUTPUT_DIRECTORY = False
LOAD_CONTENT_CACHE = False

STATIC_PATHS=['pdf', 'images', 'CNAME']

THEME = './theme'
PROFILE_IMAGE = 'images/lfochamon_thumb.jpg'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican_bib', 'render_math', 'jinja2content', 'image_process']
PUBLICATIONS_SRC = 'content/publications.bib'
PUBLICATIONS_SPLIT_BY = 'keywords'
PUBLICATIONS_CUSTOM_STYLE = True
PUBLICATIONS_PLUGIN_PATH = 'theme'

MATH_JAX = {
    # align: [string] 'left', 'right' or 'center'. Default Value: 'center'.
    # auto_insert: [boolean] will insert the MathJax script into content that it is detected to have math in it. Default Value: True
    # indent: [string] if align not set to 'center', then this controls the indent level. Default Value: '0em'.
    'show_menu': False,
    'equation_numbering': 'AMS',
    # process_escapes: [boolean] controls whether MathJax processes escape sequences. Default Value: True
    # mathjax_font: [string] sanserif, typewriter or fraktur. If this is not set, it will use the default font settings.
    # latex_preview: [string] controls the preview message users are shown while MathJax is rendering LaTex. Default Value: 'Tex'
    # color: [string] controls the color of the MathJax rendered font. Default Value: 'inherit'
    # linebreak_automatic: [boolean] If set, MathJax will try to intelligently break up displayed math. Default Value: False
    # tex_extensions: [list] a list of latex extensions accepted by MathJax. Default Value: [] (empty list)
    'tex_extensions': ['color.js'],
    # responsive: [boolean] tries to make displayed math render responsively. Default Value: False (defaults to False for backward compatibility)
    # responsive_break: [integer] a number (in pixels) representing the width breakpoint that is used when setting responsive_align to True. Default Value: 768
    'process_summary': False
    # message_style: [string] This value controls the verbosity of the messages in the lower left-hand corner. Set it to None to eliminate all messages. Default Value: normal
}


MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.toc': {},
        'markdown.extensions.md_in_html': {},
        'markdown.extensions.tables': {},
        'markdown.extensions.footnotes': {},
        'markdown.extensions.attr_list': {},
        'markdown.extensions.sane_lists': {},
        'markdown.extensions.codehilite': {'css_class': 'code-highlight'},
        'markdown.extensions.fenced_code': {},
    },
    'output_format': 'html5',
}


ARTICLE_PATHS = ['posts']
ARTICLE_URL = ARTICLE_SAVE_AS = "blog/posts/{date:%Y}-{date:%m}-{date:%d}_{slug}.html"
INDEX_SAVE_AS = 'blog/index.html'
ARTICLE_ORDER_BY = 'reversed-date'
SLUGIFY_SOURCE = 'title'

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/{number}/','{base_name}/{number}/index.html'),
)
PAGINATED_TEMPLATES =  {'index': None, 'tag': None, 'category': None, 'archives': None}

AUTHORS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

CATEGORIES_SAVE_AS = ''
CATEGORY_SAVE_AS = ''

TAGS_SAVE_AS = 'blog/tags.html'
TAG_SAVE_AS = 'blog/tag/{slug}.html'

PAGE_LANG_SAVE_AS = ''
ARTICLE_LANG_SAVE_AS = ''

SUMMARY_MAX_LENGTH = 50
SUMMARY_END_SUFFIX = '...'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False


def crop_from_center(width, height):
    def _crop(image):
        w, h = image.size

        top = max(h//2 - height//2, 0)
        left = max(w//2 - width//2, 0)
        bottom = min(top + height, h)
        right = min(left + width, w)

        return image.crop((left, top, right, bottom))

    return _crop

def crop_to_ratio(width, height):
    def _crop(image):
        w, h = image.size
        new_h = int(round(w/width*height))

        top = max(h//2 - new_h//2, 0)
        left = 0
        bottom = top + new_h
        right = w

        return image.crop((left, top, right, bottom))

    return _crop

IMAGE_PROCESS_FORCE = True
IMAGE_PROCESS = {
    "largest": ["scale_in 800 800 False"],
    "large": ["scale_in 600 600 False"],
    "normal": ["scale_in 400 400 False"],
    "small": ["scale_in 300 300 False"],

    "largest-16-9": ["scale_out 800 800 False", crop_to_ratio(16,9)],
    "large-16-9": ["scale_out 600 600 False", crop_to_ratio(16,9)],
    "normal-16-9": ["scale_out 400 400 False", crop_to_ratio(16,9)],
    "small-16-9": ["scale_out 300 300 False", crop_to_ratio(16,9)],

    "largest-4-3": ["scale_out 800 800 False", crop_to_ratio(4,3)],
    "large-4-3": ["scale_out 600 600 False", crop_to_ratio(4,3)],
    "normal-4-3": ["scale_out 400 400 False", crop_to_ratio(4,3)],
    "small-4-3": ["scale_out 300 300 False", crop_to_ratio(4,3)],

    "largest-square": ["scale_out 800 800 False", crop_from_center(730,730)],
    "large-square": ["scale_out 600 600 False", crop_from_center(500,500)],
    "normal-square": ["scale_out 400 400 False", crop_from_center(400,400)],
    "small-square": ["scale_out 300 300 False", crop_from_center(200,200)],
}


def throw_error(msg):
    raise Exception(f'[ERROR]: {msg}')

def pelican_expand_links(text, content):
    return content._update_content(text, content.get_siteurl())

def js_timestamp(date):
    # 2022-01-31 23:00:00 GMT-0300
    return '{:d}'.format(round(datetime.strptime(date, '%Y-%m-%d %H:%M:%S %Z%z').timestamp()*1000))

def basename(path):
    return os.path.basename(path)

JINJA_FILTERS = {'expand_links': pelican_expand_links,
                 'js_timestamp': js_timestamp,
                 'basename': basename,
                 'error': throw_error}
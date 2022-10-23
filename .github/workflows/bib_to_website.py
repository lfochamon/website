# -*- coding: utf-8 -*-

import os, re, sys

PATH = os.path.dirname(os.path.realpath(__file__))
print(PATH)
BIB_PATH = os.path.join(PATH,'../../../publications-list')
WEB_PATH = os.path.join(PATH,'../../www')

sys.path.append(WEB_PATH)
from publishconf import SITEURL


# Replace SITEURL
with open(os.path.join(BIB_PATH, 'publications.bib'), 'r') as input_file, open(os.path.join(BIB_PATH, 'temp.bib'), 'w') as output_file:
    for line in input_file:
        str = line.replace('SITEURL', SITEURL)
        output_file.write(str)

os.rename(os.path.join(BIB_PATH, "temp.bib"), os.path.join(BIB_PATH, "publications.bib"))

# Prepare bib file for CV
author_regex = re.compile(r'L\. F\. O\. Chamon(\*?)')
arxiv_regex = re.compile(r'arxiv\s*=.*')
pdf_regex = re.compile(r'pdf\s*=.*')
poster_regex = re.compile(r'poster\s*=.*')
slides_regex = re.compile(r'slides\s*=.*')
url_regex = re.compile(r'url\s*=.*')
with open(os.path.join(BIB_PATH, 'publications.bib'), 'r') as input_file, open(os.path.join(BIB_PATH, 'cv.bib'), 'w') as output_file:
    for line in input_file:
        str = re.sub(author_regex, r'\\textbf{L. F. O. Chamon}\1', line)
        str = re.sub(arxiv_regex, '', str)
        str = re.sub(pdf_regex, '', str)
        str = re.sub(poster_regex, '', str)
        str = re.sub(slides_regex, '', str)
        str = re.sub(url_regex, '', str)
        output_file.write(str)

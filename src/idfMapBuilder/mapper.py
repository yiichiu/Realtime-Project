#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET
import nltk
from nltk.tokenize import RegexpTokenizer
from collections import Counter
from sets import Set
#read xml from stdin
NS = '{http://www.mediawiki.org/xml/export-0.10/}'
tree = ET.parse(sys.stdin)
root = tree.getroot()

#parse
tokenizer = RegexpTokenizer(r'\w+')
for page in root.findall(NS + 'page'):
  try:
    title = page.find(NS + 'title')
    text = page.find(NS + 'revision').find(NS+'text').text.lower()
    docid = page.get('docid')
    tokens = tokenizer.tokenize('%s %s %s' % (text, title, title))
    #count distinct terms
    terms = Set(tokens)
    #output pairs
    for term in terms:
      print '%s\t%s' % (term.encode('utf8'), docid)
  except:
    pass

#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET
import nltk
from nltk.tokenize import RegexpTokenizer
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
    #count tf
    cnt = {}
    for word in tokens:
      try:
        cnt[word] += 1
      except:
        cnt[word] = 1
    #output pairs
    for word in cnt:
      word = word.encode('utf8')
      print '%s\t%s,%s' % (docid, word, cnt[word])
  except:
    pass

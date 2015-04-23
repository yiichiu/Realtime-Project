#!/usr/bin/env python
#from lxml import html
#from nltk.tokenize import RegexpTokenizer
import sys

for line in sys.stdin:
  #key: docid
  #value: data
  [docid, data] = line.strip().split('\t', 1)
  #tokenize
  #tokenizer = RegexpTokenizer(r'\w+')
  for word in data.split(' '):
    try:
      print '%s\t%s' % (word, docid)
    except:
      pass

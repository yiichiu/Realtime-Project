#!/usr/bin/env python

import sys
import pickle
import urllib

docStore = {}
for line in sys.stdin:
  kvPair = line.strip().split('\t')
  docid = kvPair[0]
  [title, text, url] = kvPair[1].split(',')
  #decode title and 
  title = urllib.unquote(title)
  text =  urllib.unquote(text)
  url =  urllib.unquote(url)
  docStore[int(docid)] = {'title':title, 'text':text, 'url':url}
for docid in docStore:
  print '%s\t%s' % (str(docid), str(docStore[docid]))
#print pickle.dumps(docStore)

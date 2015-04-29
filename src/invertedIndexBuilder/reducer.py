#!/usr/bin/env python

import sys
import pickle


dic = {}
for line in sys.stdin:
  kvPair = line.strip().split('\t')
  docId = int(kvPair[0])
  wordtfPair = kvPair[1].split(',')
  term = wordtfPair[0]
  tf = int(wordtfPair[1])
  try:
    dic[term][docId] = tf
  except:
    dic[term] = {docId:tf}

  #print '%s %s' % (term, str(dic[term]))
for word in dic:
  print '%s\t%s' % ( word, dic[word] )

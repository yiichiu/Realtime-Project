#!/usr/bin/env python

import sys
import pickle
import math

cnt = {}
idf = {}
for line in sys.stdin:
  kvPair = line.strip().split('\t')
  term = kvPair[0]
  docid = kvPair[1]
  #count document freq
  try:
    cnt[term] += 1
  except:
    cnt[term] = 1
#calculate idf
for term in cnt:
  idf[term] = math.log(len(cnt) / float(cnt[term]))
  print '%s\t%f' % ( term, idf[term])
#print pickle.dumps(idf)

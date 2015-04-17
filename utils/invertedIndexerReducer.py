#!/usr/bin/env python
# Yu-Chih Yu
# A reducer program for wiki indexing.
import sys
import math
from sets import Set

# input comes from STDIN
for line in sys.stdin:
  # remove leading and trailing whitespace
  line = line.strip()
  
  # parse the input we got from mapper.py
  word, docs = line.split('\t', 1)
  lists = {}
  for doc in docs:
    try:
		  lists[doc] += 1
    except:
      lists[doc] = 1
  
  invlist = []
  
  #N
  N = len(Set(docs))
  
  # build inverted lists
  for doc in lists:
    #a:5 b:10
    data = doc + '\t' +str(lists[doc] * math.log(N/len(lists)))
    invlist.append(data)
  print '%s\t%s' % (word, invlist)

#!/usr/bin/env python
# Yu-Chih Yu
# A reducer program for wiki indexing.
import sys
import math

pre_word = None

# input comes from STDIN
lists = {}
for line in sys.stdin:
  # remove leading and trailing whitespace
  line = line.strip()
  # parse the input we got from mapper.py
  word, docid = line.split('\t', 1)
  #output 
  if pre_word != None and word != pre_word:
    invlist = []
    #N
    N = 5
    
    # build inverted lists
    for doc in lists:
      #a:5 b:10
      data = doc + '\t' +str(float(lists[doc]) * math.log(float(N)/len(lists)))
      invlist.append(data)
    print '%s\t%s' % (pre_word, invlist)
    lists = {}

  try:
     lists[docid] += 1
  except:
     lists[docid] = 1
  pre_word = word

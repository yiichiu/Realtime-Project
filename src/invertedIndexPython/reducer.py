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
  word, doc = line.split('\t', 1)
  if pre_word == None or word == pre_word:
    try:
      lists[doc] += 1
    except:
      lists[doc] = 1
  else:
    invlist = []
    #N
    N = len(lists)

    # build inverted lists
    for doc in lists:
      #a:5 b:10
      data = doc + '\t' +str(float(lists[doc]) * math.log(N/lists[doc]))
      invlist.append(data)
    print '%s\t%s' % (word, invlist)
    list = {}
  pre_word = word

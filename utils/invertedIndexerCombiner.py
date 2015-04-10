#!/usr/bin/env python
# Yu-Chih Yu
# A reducer program for wiki indexing.
import sys
import math


preWord = None
value = ''
# input comes from STDIN
for line in sys.stdin:
  # remove leading and trailing whitespace
  line = line.strip()
  
  # parse the input we got from mapper.py
  word, doc = line.split('\t')
  if preWord == word:
    value += ',' + doc
  else:
    if preWord:
      print '%s\t%s' % (preWord, value)
    value = doc

  preWord = word

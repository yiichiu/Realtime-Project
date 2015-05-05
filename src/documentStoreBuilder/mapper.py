#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import pickle
import json
import urllib
#read xml from file
NS = '{http://www.mediawiki.org/xml/export-0.10/}'
tree = ET.parse(sys.stdin)
root = tree.getroot()

#parse
tokenizer = RegexpTokenizer(r'\w+')
for page in root.findall(NS + 'page'):
  try:
    title = page.find(NS + 'title').text
    url = 'http://en.wikipedia.org/wiki/%s' % title
    text = page.find(NS + 'revision').find(NS+'text').text
    docid = page.get('docid')
  
    #encode title and body
    #text = urllib.quote(text.encode('utf8'))
    tokens = tokenizer.tokenize(text)
    #remove stopwords
    stopwords = nltk.corpus.stopwords.words('english')
    moreSW = ['wwww', 'web', 'ref', 'cite', 'http', 'br', 'url', 'com']
    stopwords += moreSW
    content = [w for w in tokens if w.lower() not in stopwords]
    newText = ''
    for token in content:
      newText += ' ' + token
    text = urllib.quote(newText.encode('utf-8'))
    title = urllib.quote(title.encode('utf8'))
    url = urllib.quote(url.encode('utf8'))
    #output pairs
    print "%s\t%s,%s,%s" % ( docid, title, text, url)
    #print "%s\t%s,%s,%s" % ( docid, title, newText, url)
  except:
    pass

from HTMLParser import HTMLParser
import urlparse
import sys

with open('../wiki/Google', 'r') as infile:
    data = infile.read().replace('\n', ' ')


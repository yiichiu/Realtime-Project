import sys
import hashlib
import getpass
import socket
import json
import urllib
from sets import Set
import cPickle as pickle
from math import log10
import subprocess
#import argparse
import os
from  xml.etree import ElementTree

class Arguments():
    def __init__(self):
        self.jobPath = ''
        self.xmlFileName = ''
        self.numPartitions = 1

fileNames = []
mapTaskIds = []
args = Arguments()

'''
def parseParams():
  parser = argparse.ArgumentParser(description='mapreduce framework')
  requiredArgs = ['--jobPath', '--numPartitions'] 
  parser.add_argument('xmlFileName')
  for arg in requiredArgs:
    parser.add_argument('%s' % arg, required=True)
  return parser.parse_args()
'''

def readXML():
  f = open('%s' % args.xmlFileName, 'r')
  result = f.read()
  print '-----finish reading %s-----' % args.xmlFileName
  return result

def partition():
  tree = ElementTree.parse('%s' % args.xmlFileName)
  root = tree.getroot()
  NS = '{http://www.mediawiki.org/xml/export-0.10/}'
  numPartitions = int(args.numPartitions)
  trees = []
  for i in xrange(numPartitions):
    elem = ElementTree.Element('xml')
    trees.append(elem)
  cnt =0
  for page in root.findall(NS + 'page'):
    page.set('docid', str(cnt))
    trees[cnt%numPartitions].append(page)
    cnt += 1
  for i in xrange(numPartitions):
    filename = '%s/%d.in' % (args.jobPath, i)
    print 'writing %s' % filename
    ElementTree.ElementTree(trees[i]).write(filename,encoding="UTF-8")
    print 'finish writing %s' % filename

if __name__ == "__main__":
  #args = parseParams()
  args.jobPath = '../data/input'
  args.numPartitions = 4
  args.xmlFileName = '../data/strategywiki_current.xml'
  print '\n-----reading files from %s-----' % args.xmlFileName
  readXML()
  print '\n-----partitioning files to %s .in files-----' % \
        args.numPartitions
  partition()
  print '\n-----JOB SUCCESS-----'


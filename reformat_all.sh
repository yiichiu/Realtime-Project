#!/bin/sh
python utils/reformatter.py data/enwiki8.xml \
  --jobPath=data/input \
  --numPartitions=$1

#!/bin/sh
python utils/reformatter.py data/enwiki1.xml \
  --jobPath=data/input \
  --numPartitions=$1

#!/bin/sh
python utils/reformatter.py data/enwiki*.xml \
  --jobPath=data/input \
  --numPartitions=$1

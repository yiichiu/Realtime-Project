#!/bin/bash
mkdir input
for i in {0..19}
do
  python utils/dataProcessing.py wiki/ $i > input/$i.out
done

mkdir data/localResult
dir=$(echo $1 | cut -d/ -f2)
echo $dir
mkdir data/localResult/$dir
cat $2 | python $1/mapper.py | python $1/reducer.py > data/localResult/$dir/part-00000

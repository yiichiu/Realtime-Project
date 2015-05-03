dir=$(echo $1 | cut -d/ -f2)
mkdir data/$dir
# The first argument should be the path to mapper and reducer
hdfs dfs -rm -r project/output
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -file $1/mapper.py -mapper $1/mapper.py -file $1/reducer.py -reducer $1/reducer.py -input project/input -output project/output
rm data/$dir/part-00000
hdfs dfs -get project/output/part-00000 data/$dir/

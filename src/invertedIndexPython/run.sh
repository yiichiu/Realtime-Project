hdfs dfs -rm -r output*
hadoop jar /usr/hdp/2.2.0.0-2041/hadoop-mapreduce/hadoop-streaming-2.6.0.2.2.0.0-2041.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input project/input -output output

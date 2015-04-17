hdfs dfs -rmdir project_output
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -file utils/invertedIndexerMapper.py -mapper utils/invertedIndexerMapper.py -file utils/invertedIndexerReducer.py -reducer utils/invertedIndexerReducer.py -input final_input -output project_output

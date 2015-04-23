javac *.java
rm -f $1.jar
jar cvf $1.jar *.class
rm -f *.class
hdfs dfs -mkdir project/$1
hdfs dfs -mkdir project/$1/input
hdfs dfs -put $2 project/$1/input/
hdfs dfs -rm -r project/$1/output*
hadoop jar $1.jar $1 project/$1/input project/$1/output
rm -fr output*
hdfs dfs -get project/$1/output .
cat output/part-r-00000

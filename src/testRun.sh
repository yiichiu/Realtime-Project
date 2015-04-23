javac *.java
rm -f $1.jar
jar cvf $1.jar *.class
rm -f *.class
hdfs dfs -rm -r project/output*
hadoop jar $1.jar $1 project/input $1/output
rm -fr output*
hdfs dfs -get $1/output .
cat output/part-r-00000

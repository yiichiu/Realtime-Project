import java.io.*;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.StringTokenizer;
import java.util.HashMap;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;


public class PageRankMapper
    extends Mapper<LongWritable, Text, Text, Text> {

    @Override
    public void map(LongWritable key, Text value, Context context)
        throws IOException, InterruptedException {

        String line = value.toString();
        String[] key_and_value = line.split("\t");
        String target = key_and_value[0];
        String[] tokens = key_and_value[1].split(" ");
        int total_neighbors = tokens.length - 1;
        double weight = Double.parseDouble(tokens[tokens.length-1]);

        String s = "";
        for(int i = 0; i < tokens.length-1; i++){
            s += tokens[i];
            s += " ";
            context.write(new Text(tokens[i]), new Text(target+","+String.valueOf(weight/total_neighbors)));
        }
        context.write(new Text(target), new Text(s));

    }

}

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class PageRankReducer
    extends Reducer<Text, Text, Text, Text> {

    public void reduce(Text key, Iterable<Text> values,
        Context context) throws IOException, InterruptedException {        

        double sum = 0;
        String s = "";
        for (Text value : values) {
            String line = value.toString();
            String[] token_and_val = line.split(",");
            if(token_and_val.length == 2){
                double val = Double.parseDouble(token_and_val[1]); 
                sum += val;
            }
            else{
                s = token_and_val[0];
            }
        }

        context.write(key, new Text(s+String.valueOf(sum)));
    }

}


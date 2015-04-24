import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class PageRank {

    public static void main(String[] args) throws Exception {
        // what should be input as args
        //

        String input = args[0];
        String output = args[1];

        for(int i = 0; i < 10; i++){
            Job job = new Job();
            job.setJarByClass(PageRank.class);
            job.setJobName("Page Rank");

            FileInputFormat.addInputPath(job, new Path(input));
            FileOutputFormat.setOutputPath(job, new Path(output));

            job.setMapperClass(PageRankMapper.class);
            job.setReducerClass(PageRankReducer.class);

            job.setOutputKeyClass(Text.class);
            job.setOutputValueClass(Text.class);
    
            input = output + "/part-r-00000";
            output = "output" + String.valueOf(i);

            job.waitForCompletion(true);
        }
    }
}

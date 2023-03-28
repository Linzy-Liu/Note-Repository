package sort;

import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.FileInputFormat;
import org.apache.hadoop.mapred.FileOutputFormat;
import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;

import java.io.IOException;

public class RecordSort
{
    public static class SortMapper extends Mapper<Object, Text, IntWritable, Text>
    {
        public void map(Object key, Text value, Context context) throws IOException, InterruptedException
        {
            String tmp = value.toString();
            String[] words = tmp.split(" ");
            int val = Integer.parseInt(words[1]);
            context.write(new IntWritable(val), new Text(words[0]));
        }
    }

    public static class SortReducer extends Reducer<IntWritable, Text, Text, IntWritable>
    {
        public void reduce(IntWritable key, Iterable<Text> values, Context context) throws IOException, InterruptedException
        {
            for (Text val : values)
            {
                context.write(val, key);
            }
        }
    }

    public static void main(String[] args) throws IOException, InterruptedException, ClassNotFoundException
    {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "RecordSort");
        job.setJarByClass(RecordSort.class);
        job.setMapperClass(SortMapper.class);
        job.setReducerClass(SortReducer.class);
        job.setCombinerClass(SortReducer.class);
        job.setMapOutputKeyClass(IntWritable.class);
        job.setMapOutputValueClass(Text.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        JobConf jobconf = (JobConf) job.getConfiguration();
        for (int i = 0; i < args.length - 1; i++)
        {
            FileInputFormat.addInputPath(jobconf, new Path(args[i]));
        }
        FileOutputFormat.setOutputPath(jobconf, new Path(args[args.length - 1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}

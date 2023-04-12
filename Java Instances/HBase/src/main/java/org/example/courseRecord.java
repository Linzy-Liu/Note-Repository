package org.example;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.HColumnDescriptor;
import org.apache.hadoop.hbase.HTableDescriptor;
import org.apache.hadoop.hbase.TableName;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.util.Bytes;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Hashtable;
import java.util.List;

public class courseRecord
{
    private static final String fileName1 = "/data/sc_course_.csv";
    private static final String fileName2 = "/data/sc_scs_.csv";
    private static final String fileName3 = "/data/sc_student_.csv";
    private static final String tableName = "course";
    private static final String[] Families = {"info", "student"};
    private static final byte[][] regions = {
            Bytes.toBytes("20"),
            Bytes.toBytes("50"),
            Bytes.toBytes("80")
    };

    public static Connection getConn() throws IOException
    {
        Configuration conf = HBaseConfiguration.create();
        conf.set("hbase.rootdir", "hdfs://master:8020/hbase");// 指定HBase在HDFS上存储路径
        conf.set("hbase.zookeeper.quorum", "master,slave1,slave2");// 指定使用的Zookeeper集群
        conf.set("hbase.zookeeper.property.clientPort", "2181");// 指定使用Zookeeper集群的端口
        return ConnectionFactory.createConnection(conf);// 获取连接
    }

    public static void createTable(@org.jetbrains.annotations.NotNull Connection conn, String table_name, String[] families) throws IOException
    {
        Admin admin = conn.getAdmin();
        TableName tableName = TableName.valueOf(table_name);
        HTableDescriptor ht = new HTableDescriptor(tableName);
        for (String i : families)
        {
            ht.addFamily(new HColumnDescriptor(i));
        }
        if (admin.tableExists(tableName))
        {
            if (admin.isTableEnabled(tableName))
            {
                admin.disableTable(tableName);
            }
            admin.deleteTable(tableName);
        }
        admin.createTable(ht, regions);
    }

    public static Put putData(String row, String family, String col, String value)
    {
        Put put = new Put(Bytes.toBytes(row));
        put.addColumn(Bytes.toBytes(family), Bytes.toBytes(col), System.currentTimeMillis(), Bytes.toBytes(value));
        return put;
    }

    public static void putToTable(Connection conn, String tableName) throws IOException
    {
        InputStreamReader in = new FileReader(fileName1);
        BufferedReader temp = new BufferedReader(in);
        String line = null;
        String[] cols = temp.readLine().split(",", -1);
        Hashtable<String, String> hash = new Hashtable<>(10);
        for (line = temp.readLine(); line != null; line = temp.readLine())
        {
            String[] val = line.split(",", -1);
            hash.put(val[0], val[1]);
        }
        temp.close();
        in.close();
        in = new FileReader(fileName2);
        temp = new BufferedReader(in);
        cols = temp.readLine().split(",", -1);
        List<Put> puts = new ArrayList<>();
        for (line = temp.readLine(); line != null; line = temp.readLine())
        {
            String[] content = line.split(",", -1);
            if (content[0] != null)
            {
                puts.add(putData(content[0], Families[0], cols[1], content[1]));
                puts.add(putData(content[0], Families[0], "course_name", hash.get(content[1])));
            }
        }
        temp.close();
        in.close();
        in = new FileReader(fileName3);
        temp = new BufferedReader(in);
        cols = temp.readLine().split(",", -1);
        for (line = temp.readLine(); line != null; line = temp.readLine())
        {
            String[] content = line.split(",", -1);
            if (content[0] != null)
            {
                puts.add(putData(content[0], Families[1], cols[1], content[1]));
            }
        }
        temp.close();
        in.close();
        Table tb = conn.getTable(TableName.valueOf(tableName));
        tb.put(puts);
    }

    public static void main(String[] args) throws IOException
    {
        Connection conn = getConn();
        createTable(conn, tableName, Families);
        putToTable(conn, tableName);
        conn.close();
    }
}

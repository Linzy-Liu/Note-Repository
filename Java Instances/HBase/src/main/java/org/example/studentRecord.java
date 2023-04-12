package org.example;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.*;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.util.*;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class studentRecord
{
    private static final String fileName = "/data/sc_student_.csv";
    private static final String tableName = "student";
    private static final String[] Family = {"info"};
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
        InputStreamReader in = new FileReader(fileName);
        BufferedReader temp = new BufferedReader(in);
        String line = null;
        String[] cols = temp.readLine().split(",", -1);
        List<Put> puts = new ArrayList<>();
        for (line = temp.readLine(); line != null; line = temp.readLine())
        {
            String[] content = line.split(",", -1);
            if (content[0] != null)
            {
                for (int i = 1; i < cols.length; i++)
                {
                    puts.add(putData(content[0], Family[0], cols[i], content[i]));
                }
            }
        }
        Table tb = conn.getTable(TableName.valueOf(tableName));
        tb.put(puts);
    }

    public static void main(String[] args) throws IOException
    {
        Connection conn = getConn();
        createTable(conn, tableName, Family);
        putToTable(conn, tableName);
        conn.close();
    }
}

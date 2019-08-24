
```bash
$ vagrant up MACHINE01  
$ vagrant ssh MACHINE01 -- -l hduser
```

The password of *hduser* is `hduser`.
You're good to go!

## For learning Cassandra, below are the hardware requirements:

http://cassandra.apache.org/doc/latest/operating/hardware.html

1. Minimum Processor (i7 2300) or above Per a Node required: 2 core (Cassandra using CPU heavily during compaction process, compression, if enabled, reading data (more if compressed) etc. Try to get more cores if you can)
1. Minimum RAM Per a Node required: 4GB (Suggested: Minimum of 16 GB to a maximum of 96 GB of RAM per machine)
1. Minimum Free Disk Space Per a Node: 60GB 
1. Operating System of 64bit (Suggested)



## Clone a new VM from Master box file

```bash
[hadoop-single-node-vagrant]$ vagrant halt MACHINE01
[hadoop-single-node-vagrant]$ vagrant package MACHINE01  --output master.box
[hadoop-single-node-vagrant]$ vagrant box add robert-cassandra-box master.box
```

Now you can create virtual machines from this box by simply giving the name of the box in the Vagrantfile, like

```yaml
config.vm.box = "robert-cassandra-box"
```

## Creating Sample

```bash
MACHINE01/CASSANDRA_HOME/bin%>./cassandra
```

After you started cassandra in the other two nodes.

```bash
MACHINE02/CASSANDRA_HOME/bin%>./cassandra
MACHINE03/CASSANDRA_HOME/bin%>./cassandra

hduser@MACHINE01:~$ nodetool status
Datacenter: datacenter1
=======================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address          Load       Tokens       Owns (effective)  Host ID                               Rack
UN  107.170.38.238   108.61 KiB  256          65.8%             a239a80c-10fd-44c8-b651-61cfb1457e02  rack1
UN  107.170.112.81   93.96 KiB  256          69.4%             95fcfe4a-cc4c-4472-8666-32dcdf9c8f86  rack1
UN  107.170.115.161  30.06 KiB  256          64.8%             632291a7-547a-43ae-b0b1-c6e1b623a5d2  rack1
hduser@MACHINE01:~$ cqlsh
Connected to BedxheCluster at 127.0.0.1:9042.
[cqlsh 5.0.1 | Cassandra 3.11.4 | CQL spec 3.4.4 | Native protocol v4]
Use HELP for help.
cqlsh> CREATE KEYSPACE mykeyspace WITH REPLICATION = { 'class' : 'SimpleStrategy','replication_factor' : 1 };
cqlsh> USE mykeyspace;
cqlsh:mykeyspace> CREATE TABLE users (user_id int PRIMARY KEY, fname text, lname text);
cqlsh:mykeyspace> INSERT INTO users (user_id, fname, lname) VALUES (1745, 'john', 'smith');
cqlsh:mykeyspace> INSERT INTO users (user_id, fname, lname) VALUES (1744, 'john', 'doe');
cqlsh:mykeyspace> INSERT INTO users (user_id, fname, lname) VALUES (1746, 'john', 'smith');
cqlsh:mykeyspace> use mykeyspace;
cqlsh:mykeyspace> select * from users;

 user_id | fname | lname
---------+-------+-------
    1745 |  john | smith
    1744 |  john |   doe
    1746 |  john | smith

(3 rows)
cqlsh:mykeyspace>

```

```bash
CREATE KEYSPACE test WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1 };
CREATE TABLE test.kv(key text PRIMARY KEY, value int);
```

寫個兩筆資料進去kv表，然後確認一下：

```bash
cqlsh:test> INSERT INTO test.kv(key, value) VALUES ('key1', 1);
cqlsh:test> INSERT INTO test.kv(key, value) VALUES ('key2', 2);
cqlsh:test> SELECT * FROM kv;
 key  | value
------+-------
 key1 |     1
 key2 |     2
```

## Using Apache Spark-Cassandra Connector
1. Download [Spark](http://apache.stu.edu.tw/spark/spark-2.4.3/spark-2.4.3-bin-hadoop2.7.tgz) and extract it .
1. Install Scala 2.12.x

```bash
$ git clone https://github.com/datastax/spark-cassandra-connector.git
$ cd spark-cassandra-connector
$ sbt/sbt assembly
$ $SPARK_HOME/bin/spark-shell --jars ~/spark-cassandra-connector/spark-cassandra-connector/target/scala-2.10/connector-assembly-1.2.0-SNAPSHOT.jar 
```

or

```bash
spark-shell  --packages com.datastax.spark:spark-cassandra-connector_2.11:2.0.12  --driver-class-path  E:/Users/robert0714/.ivy2/jars/*.jar

spark-shell  --packages com.datastax.spark:spark-cassandra-connector_2.11:2.0.12  --driver-class-path  ${USERHOME}/.ivy2/jars/*.jar
```
In scala prompt,

```bash
scala> sc.stop
scala> import com.datastax.spark.connector._, org.apache.spark.SparkContext, org.apache.spark.SparkContext._, org.apache.spark.SparkConf
scala>  sc.stop
scala>  val conf = new SparkConf(true).set("spark.cassandra.connection.host","107.170.38.238")
scala>  val sc = new SparkContext(conf)
scala>  val test_spark_rdd = sc.cassandraTable("mykeyspace", "users")
scala>  test_spark_rdd.foreach(println)
```

## Running PySpark with Cassandra using spark-cassandra-connector
 
 Preparing python environment.
 
```bash
conda create --name cassandra  python=3.7 anaconda
conda activate cassandra
python -m pip install --upgrade pip
pip install cassandra-driver
pip install pyspark
```
 In python prompt
 
```python
(cassandra) E:\Users\robert0714\Desktop\spark-2.0.2-bin-hadoop2.7\bin>python
Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.datastax.spark:spark-cassandra-connector_2.11:2.0.12 --conf   spark.cassandra.connection.host=107.170.38.238    --driver-class-path  E:/Users/robert0714/.ivy2/jars/*.jar  pyspark-shell'


```
### windows
http://deelesh.github.io/pyspark-windows.html

#### Installing winutils
Let’s download the winutils.exe and configure our Spark installation to find winutils.exe.
1.  [hadoop-2.7.1](https://github.com/steveloughran/winutils/raw/master/hadoop-2.7.1/bin/winutils.exe)
1.  [hadoop-2.8.1](https://github.com/steveloughran/winutils/blob/master/hadoop-2.8.1/winutils.exe)
1.  [hadoop-3.0.0](https://github.com/steveloughran/winutils/blob/master/hadoop-3.0.0/bin/winutils.exe)

steps:
1.  Create a *hadoop\bin* folder inside the SPARK_HOME folder.
1.  Download the winutils.exe for the version of hadoop against which your Spark installation was built for.
1.  Create a system environment variable in Windows called *SPARK_HOME* that points to the SPARK_HOME folder path. 
1.  Create another system environment variable in Windows called *HADOOP_HOME* that points to the hadoop folder inside the SPARK_HOME folder.
1.  Since the *hadoop* folder is inside the SPARK_HOME folder, it is better to create *HADOOP_HOME* environment variable using a value of *%SPARK_HOME%\hadoop*. That way you don’t have to change HADOOP_HOME if SPARK_HOME is updated.

```python
(cassandra) C:\Users\robert0714>pyspark --packages "com.datastax.spark:spark-cassandra-connector_2.11:2.0.12" --conf   "spark.cassandra.connection.host=107.170.38.238"    --driver-class-path  "E:/Users/robert0714/.ivy2/jars/*.jar"

(cassandra) C:\Users\robert0714>pyspark --packages "com.datastax.spark:spark-cassandra-connector_2.11:2.4.1" --conf   "spark.cassandra.connection.host=107.170.38.238"    --driver-class-path  "E:/Users/robert0714/.ivy2/jars/*.jar"

>>> from pyspark import SparkConf
>>> from pyspark import SparkContext
>>> from pyspark.sql import SQLContext

def load_and_get_table_df(keys_space_name, table_name):
    table_df = sqlContext.read\
        .format("org.apache.spark.sql.cassandra")\
        .options(table=table_name, keyspace=keys_space_name)\
        .load() 
    return table_df
    
>>> users = load_and_get_table_df("mykeyspace", "users")
>>> users.show()


```

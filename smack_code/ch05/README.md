
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

## Using Apacje Spark-Cassandra Connector
1. Download [Spark](http://apache.stu.edu.tw/spark/spark-2.4.3/spark-2.4.3-bin-hadoop2.7.tgz) and extract it .
1. Install Scala 2.12.x

```bash
$ git clone https://github.com/datastax/spark-cassandra-connector.git
$ cd spark-cassandra-connector
$ sbt/sbt assembly
$ $SPARK_HOME/bin/spark-shell --jars ~/spark-cassandra-connector/spark-cassandra-connector/target/scala-2.10/connector-assembly-1.2.0-SNAPSHOT.jar 
```

In scala prompt,

```bash
scala> sc.stop
scala> import com.datastax.spark.connector._
scala> import org.apache.spark.SparkContext
scala> import org.apache.spark.SparkContext._
scala> import org.apache.spark.SparkConf
scala>  val conf = new SparkConf(true).set("spark.cassandra.connection.host","107.170.38.238")
scala>  val sc = new SparkContext(conf)
scala>  val test_spark_rdd = sc.cassandraTable("mykeyspace", "users")

```

# Hardware requirement for apache kafka
1. [ref](https://stackoverflow.com/questions/56696727/hardware-requirement-for-apache-kafka)
1. [ref](https://docs.confluent.io/current/installation/system-requirements.html)
1. [ref](https://docs.confluent.io/current/kafka/deployment.html)

# Single Node-Single Broker Cluster

## Starting the ZooKeeper server

```bash
[vagrant@MACHINE01 ~]$ sudo -s
[root@MACHINE01 vagrant]# su - hduser
[hduser@MACHINE01 ~]$ cd /usr/local/apache-kafka/
[hduser@MACHINE01 apache-kafka]$ bin/zookeeper-server-start.sh config/zookeeper.properties
```

or

```bash
[vagrant@MACHINE01 ~]$ sudo -s
[root@MACHINE01 vagrant]# su - hduser
[hduser@MACHINE01 ~]$ cd /usr/local/zookeeper/
[hduser@MACHINE01 zookeeper]$ bin/zkServer start
```

## Starting the Broker

```bash
[vagrant@MACHINE01 ~]$ sudo -s
[root@MACHINE01 vagrant]# su - hduser
[hduser@MACHINE01 ~]$ cd /usr/local/apache-kafka/
[hduser@MACHINE01 apache-kafka]$ bin/kafka-server-start.sh config/server.properties
```

## Creating a Topic

```bash
[vagrant@MACHINE01 ~]$ sudo -s
[root@MACHINE01 vagrant]# su - hduser
[hduser@MACHINE01 ~]$ cd /usr/local/apache-kafka/
[hduser@MACHINE01 apache-kafka]$ bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic amazingTopic
```

To obtain the list of topics on any Kafka server, use the following command:

```bash
[hduser@MACHINE01 apache-kafka]$   bin/kafka-topics.sh --list --zookeeper localhost:2181
```

Obtain the output:

```bash
amazingopic
```

To get the details of a particular topic , run **kafak-topics** command with **--describe** parameter:

```bash
[hduser@MACHINE01 apache-kafka]$ bin/kafka-topics.sh --describe --zookeeper localhost:2181  --topic amazingTopic

Topic:amazingTopic      PartitionCount:3        ReplicationFactor:1     Configs:
        Topic: amazingTopic     Partition: 0    Leader: 0       Replicas: 0     Isr: 0
        Topic: amazingTopic     Partition: 1    Leader: 0       Replicas: 0     Isr: 0
        Topic: amazingTopic     Partition: 2    Leader: 0       Replicas: 0     Isr: 0
```

## Starting a Producer

```bash
[hduser@MACHINE01 apache-kafka]$   bin/kafka-console-producer.sh --broker-list  localhost:9092 --topic amazingTopic
```


## Starting a Consumer

```bash
[hduser@MACHINE01 apache-kafka]$  bin/kafka-console-consumer.sh --zookeeper  localhost:2181 --topic amazingTopic --from-beginning

Using the ConsoleConsumer with old consumer is deprecated and will be removed in a future major release. Consider using the new consumer by passing [bootstrap-server] instead of [zookeeper].
```

or 

```bash
[hduser@MACHINE01 apache-kafka]$ bin/kafka-console-consumer.sh   --bootstrap-server     localhost:2181  --topic amazingTopic  --from-beginning
```

# Single Node-Multiple Broker Cluster

## Starting the ZooKeeper server

```bash
[vagrant@MACHINE01 ~]$ sudo -s
[root@MACHINE01 vagrant]# su - hduser
[hduser@MACHINE01 ~]$ cd /usr/local/apache-kafka/
[hduser@MACHINE01 apache-kafka]$ bin/zookeeper-server-start.sh config/zookeeper.properties
```


## Starting the Broker

```bash
[vagrant@MACHINE01 ~]$ sudo -s
[root@MACHINE01 vagrant]# su - hduser
[hduser@MACHINE01 ~]$ cd /usr/local/apache-kafka/
[hduser@MACHINE01 apache-kafka]$ bin/kafka-server-start.sh config/server-1.properties
[hduser@MACHINE01 apache-kafka]$ bin/kafka-server-start.sh config/server-2.properties
[hduser@MACHINE01 apache-kafka]$ bin/kafka-server-start.sh config/server-3.properties
```

## Creating a Topic

```bash
[vagrant@MACHINE01 ~]$ sudo -s
[root@MACHINE01 vagrant]# su - hduser
[hduser@MACHINE01 ~]$ cd /usr/local/apache-kafka/
[hduser@MACHINE01 apache-kafka]$ bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 2 --partitions 2 --topic reAmazingTopic
```

Obtain the output, as follows:

```bash
Created topic "reAmazingTopic".
```

To obtain the list of topics on any Kafka server, use the following command:

```bash
[hduser@MACHINE01 apache-kafka]$   bin/kafka-topics.sh --list --zookeeper localhost:2181
```
 


## Starting a Producer

```bash
[hduser@MACHINE01 apache-kafka]$   bin/kafka-console-producer.sh --broker-list  localhost:9093,localhost:9094, localhost:9095 --topic reAmazingTopic
```


## Starting a Consumer

```bash
[hduser@MACHINE01 apache-kafka]$  bin/kafka-console-consumer.sh --zookeeper  localhost:2181 --from-beginning --topic reAmazingTopic
OpenJDK 64-Bit Server VM warning: If the number of processors is expected to increase from one, then you should configure the number of parallel GC threads appropriately using -XX:ParallelGCThreads=N
Using the ConsoleConsumer with old consumer is deprecated and will be removed in a future major release. Consider using the new consumer by passing [bootstrap-server] instead of [zookeeper].
```

# SBT && Scala

https://www.scala-sbt.org/1.x/docs/sbt-by-example.html

```bash
(base) G:\tmp\big-data-smack\smack_code\ch08\kafka-samples>sbt
[info] Loading project definition from G:\tmp\big-data-smack\smack_code\ch08\kafka-samples\project
[info] Loading settings for project kafka-samples from build.sbt ...
[info] Set current project to ch08 (in build file:/G:/tmp/big-data-smack/smack_code/ch08/kafka-samples/)
[info] Welcome to sbt 1.3.0.
[info] Here are some highlights of this release:
[info]   - Coursier: new default library management using https://get-coursier.io
[info]   - Super shell: displays actively running tasks
[info]   - Turbo mode: makes `test` and `run` faster in interactive sessions. Try it by running `set ThisBuild / turbo := true`.
[info] See https://www.lightbend.com/blog/sbt-1.3.0-release for full release notes.
[info] Hide the banner for this release by running `skipBanner`.
[info] sbt server started at local:sbt-server-f9bec2c298e4218804e9
sbt:ch08>
sbt:ch08> reload
[info] Loading project definition from G:\tmp\big-data-smack\smack_code\ch08\kafka-samples\project
[info] Loading settings for project kafka-samples from build.sbt ...
[info] Set current project to ch08 (in build file:/G:/tmp/big-data-smack/smack_code/ch08/kafka-samples/)
sbt:ch08> compile
[success] Total time: 1 s, completed 2019/9/8 上午 12:14:28
sbt:ch08> 

```

## Scala Producers

### Step 4.  Create the Topic

Before running the program, you must create the topic . You can create it using the API (amazing, isn’t it?) or
from the command line:

```bash
[hduser@MACHINE01 apache-kafka]$ bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 3 --topic amazingTopic
```

### Step 5. Compile the Producer
Compile the program with this command:

```bash
[hduser@MACHINE01 apache-kafka]$  scalac . apress/ch08/SimpleProducer.scala
```

or 

```bash
[hduser@MACHINE01 apache-kafka]$  sbt
sbt:ch08>  compile
```


### Step 6. Run the Producer
Run the SimpleProducer with the following command:

```bash
[hduser@MACHINE01 apache-kafka]$  scala apress.ch08.SimpleProducer amazingTopic 10 
```

or

```bash
[hduser@MACHINE01 apache-kafka]$  sbt
sbt:ch08>  run amazingTopic 10
[warn] Multiple main classes detected.  Run 'show discoveredMainClasses' to see the list

Multiple main classes detected, select one to run:

 [1] apress.ch08.CustomPartitionProducer
 [2] apress.ch08.MultiThreadConsumer
 [3] apress.ch08.SimpleConsumer
 [4] apress.ch08.SimpleProducer

[info] running apress.ch08.SimpleProducer amazingTopic 10
Topic Name - amazingTopic
Message Count - 10
```

This program takes two arguments: the topic name and the number of messages to publish.

### Step 7. Run a Consumer

As you already saw, you can run the consumer program with the following command:

```bash
[hduser@MACHINE01 apache-kafka]$ bin/kafka-console-consumer.sh --zookeeper localhost:2181 --from-beginning --topic amazingTopic
```


## Producers with Custom Partitioning

Let’s jump to the next level by writing another program that implements customized message partitioning .The example consists of recollecting the IPs visiting a web site, which are recorded and published. The message has three parts: timestamp, web site name, and IP address.

### Step 5. Create the Topic
Before running the program, you must create the pageHits topic from the command line:

```bash
[hduser@MACHINE01 apache-kafka]$  bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 3 --partitions 5 --topic pageHits
```

### Step 6. Compile the Programs
Compile the programs with the following commands:

```bash
[hduser@MACHINE01 apache-kafka]$   scalac . apress/ch08/SimplePartitioner.scala
[hduser@MACHINE01 apache-kafka]$   scalac . apress/ch08/CustomPartitionProducer.scala
```

or

```bash
[hduser@MACHINE01 apache-kafka]$  sbt
sbt:ch08>  compile
```

### Step 7. Run the Producer
Run CustomPartitionProducer with the following command:

```bash
[hduser@MACHINE01 apache-kafka]$   scala apress.ch08.CustomPartitionProducer pageHits 100
```

or

```bash
[hduser@MACHINE01 apache-kafka]$  sbt
sbt:ch08>  run  pageHits 100
[warn] Multiple main classes detected.  Run 'show discoveredMainClasses' to see the list

Multiple main classes detected, select one to run:

 [1] apress.ch08.CustomPartitionProducer
 [2] apress.ch08.MultiThreadConsumer
 [3] apress.ch08.SimpleConsumer
 [4] apress.ch08.SimpleProducer

[info] running apress.ch08.CustomPartitionProducer  
pageHits 100
```

The program takes two arguments: the topic name and the number of messages to publish.

### Step 8. Run a Consumer
As you already saw, you can run the consumer program with the following command:

```bash
[hduser@MACHINE01 apache-kafka]$   bin/kafka-console-consumer.sh --zookeeper localhost:2181 --from-beginning --topic pageHits
```

## Simple Scala Consumers

Let’s write a single threaded Scala consumer using the Consumer API for consuming the messages from a topic. This SimpleConsumer is used to fetch messages from a topic and consume them. We assume that there is a single partition in the topic.

### Step 4. Create the Topic

Before running the program, you must create the amazingTopic topic from the command line:

```bash
[hduser@MACHINE01 apache-kafka]$  bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 3 --topic amazingTopic
```

To check whether a topic has been sucessfully create , run **kafak-topics** command with **--list** parameter:

```bash
[hduser@MACHINE01 apache-kafka]$ bin/kafka-topics.sh --list --zookeeper localhost:2181  --topic amazingTopic

amazingTopic
```

To get the details of a particular topic , run **kafak-topics** command with **--describe** parameter:

```bash
[hduser@MACHINE01 apache-kafka]$ bin/kafka-topics.sh --describe --zookeeper localhost:2181  --topic amazingTopic

Topic:amazingTopic      PartitionCount:3        ReplicationFactor:1     Configs:
        Topic: amazingTopic     Partition: 0    Leader: 0       Replicas: 0     Isr: 0
        Topic: amazingTopic     Partition: 1    Leader: 0       Replicas: 0     Isr: 0
        Topic: amazingTopic     Partition: 2    Leader: 0       Replicas: 0     Isr: 0
```


### Step 5. Compile the Program

Compile the program with the following command:

```bash
[hduser@MACHINE01 apache-kafka]$   scalac . apress/ch08/SimpleConsumer.scala
```

or

```bash
[hduser@MACHINE01 apache-kafka]$  sbt
sbt:ch08>  compile
```

### Step 6. Run the Producer

Run the SimpleProducer with the following command:

```bash
[hduser@MACHINE01 apache-kafka]$   scala apress.ch08.SimpleProducer amazingTopic 100
```

or

```bash
[hduser@MACHINE01 apache-kafka]$  sbt
sbt:ch08>  run   amazingTopic 100
[warn] Multiple main classes detected.  Run 'show discoveredMainClasses' to see the list

Multiple main classes detected, select one to run:

 [1] apress.ch08.CustomPartitionProducer
 [2] apress.ch08.MultiThreadConsumer
 [3] apress.ch08.SimpleConsumer
 [4] apress.ch08.SimpleProducer

[info] running apress.ch08.SimpleProducer
```
### Step 7. Run the Consumer

Run SimpleConsumer with the following command:

```bash
[hduser@MACHINE01 apache-kafka]$   scala apress.ch08.SimpleConsumer localhost:2181 testGroup amazingTopic
```

The SimpleConsumer class takes three arguments: the ZooKeeper connection string in <host:port> form, the unique group id, and the Kafka topic name

## Multithread Scala Consumers

A multithreaded consumer API design is based on the number of partitions in the topic and has a one-toone mapping approach between the thread and the partitions in the topic.

If you don’t have the one-to-one relation, conflicts may occur, such as a thread that never receives a message or a thread that receives messages from multiple partitions. Let’s program MultiThreadConsumer.

### Step 4. Create the Topic
Before running the program, you must create the amazingTopic topic from the command line:

```bash
[hduser@MACHINE01 apache-kafka]$  bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 2 --partitions 4 --topic amazingTopic
```


### Step 5. Compile the Program
Compile the program with the following command:

```bash
[hduser@MACHINE01 apache-kafka]$   scalac . apress/ch08/MultiThreadConsumer.scala
```

or

```bash
[hduser@MACHINE01 apache-kafka]$  sbt
sbt:ch08>  compile
```


### Step 6. Run the Producer
Run SimpleProducer with the following command:

```bash
[hduser@MACHINE01 apache-kafka]$   scala apress.ch08.SimpleProducer amazingTopic 100
```

or

```bash
[hduser@MACHINE01 apache-kafka]$  sbt
sbt:ch08>  run   amazingTopic 100
[warn] Multiple main classes detected.  Run 'show discoveredMainClasses' to see the list

Multiple main classes detected, select one to run:

 [1] apress.ch08.CustomPartitionProducer
 [2] apress.ch08.MultiThreadConsumer
 [3] apress.ch08.SimpleConsumer
 [4] apress.ch08.SimpleProducer

[info] running apress.ch08.SimpleProducer
```

### Step 7. Run the Consumer
Run MultiThreadConsumer with the following command:

```bash
[hduser@MACHINE01 apache-kafka]$   scala apress.ch08.MultiThreadConsumer localhost:2181 testGroup amazingTopic 4
```

## Kafka Administration

There are numerous tools provided by Kafka to administrate features such as cluster management, topic tools, and cluster mirroring. Let’s look at these tools in detail.

## Cluster Tools
As you already know, when replicating multiple partitions, you can have replicated data. Among replicas, one acts as leader and the rest as followers. When there is no leader, a follower takes leadership.

When the broker has to be shut down for maintenance activities, the new leader is elected sequentially. This means significant I/O operations on ZooKeeper. With a big cluster, this means a delay in availability.

To reach high availability, Kafka provides tools for shutting down brokers. This tool transfers the leadership among the replicas or to another broker. If you don’t have an in-sync replica available, the tool fails to shut down the broker to ensure data integrity.

This tool is used through the following command:

```bash
[hduser@MACHINE01 apache-kafka]$   bin/kafka-run-class.sh kafka.admin.ShutdownBroker --zookeeper <zookeeper_host:port/namespace> --broker <brokerID> --num.retries 3 --retry.interval.ms 100
```

The ZooKeeper URL and the broker id are mandatory parameters. There are other optional parameters;for example, num.retries (the default value is 0) and retry.interval.ms (the default value is 1000).
When the server is stopped gracefully, it syncs all of its logs to disk to avoid any log recovery when it is restarted again, because log recovery is a time-consuming task. Before shutdown, it migrates the leader partitions to other replicas; so it ensures low downtime for each partition.

Controlled shutdown is enabled in this way:

```bash
controlled.shutdown.enable=true
```


When there is a big cluster, Kafka ensures that the lead replicas are equally distributed among the broker. If a broker fails in shutdown, this distribution cannot be balanced.

To maintain a balanced distribution, Kafka has a tool to distribute lead replicas across the brokers in the cluster. This tool’s syntax is as follows:

```bash
[hduser@MACHINE01 apache-kafka]$   bin/kafka-preferred-replica-election.sh --zookeeper <zookeeper_host:port/namespace>
```


This tool updates the ZooKeeper path with a list of topic partitions whose lead replica needs to be moved. If the controller finds that the preferred replica is not the leader, it sends a request to the broker to make the preferred replica the partition leader. If the preferred replica is not in the ISR list, the controller fails the operation to avoid data loss.

You can specify a JSON list for this tool in this format:

```bash
[hduser@MACHINE01 apache-kafka]$   bin/kafka-preferred-replicaelection.sh --zookeeper <zookeeper_host:port/namespace> --path-to-jsonfile topicPartitionList.json
```

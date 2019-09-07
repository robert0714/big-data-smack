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

## Starting a Producer

```bash
[hduser@MACHINE01 apache-kafka]$   bin/kafka-console-producer.sh --broker-list  localhost:9092 --topic amazingTopic
```


## Starting a Consumer

```bash
[hduser@MACHINE01 apache-kafka]$  bin/kafka-console-consumer.sh --zookeeper  localhost:2181 --topic amazingTopic --from-beginning
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
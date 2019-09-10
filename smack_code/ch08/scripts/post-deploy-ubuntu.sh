#!/bin/bash
# ubuntu
value=$( grep -ic "entry" /etc/hosts )
if [ $value -eq 0 ]
then
echo "
127.0.0.1       localhost
::1             localhost
################ cassandra-cookbook host entry ############
107.170.38.238  MACHINE01
107.170.112.81  MACHINE02
107.170.115.161 MACHINE03
######################################################
" > /etc/hosts
fi
# sudo apt-get update
sudo apt-get  install -y rsync openjdk-8-jdk  nfs-common portmap  
sudo ln -s java-8-openjdk-amd64 /usr/lib/jvm/jdk

sudo sh -c 'echo export JAVA_HOME=/usr/lib/jvm/jdk/ >> /home/hduser/.bashrc'

# Add hadoop user
sudo addgroup hadoop
sudo adduser --ingroup hadoop hduser
echo hduser:hduser | sudo chpasswd
sudo adduser hduser sudo

sudo -u hduser ssh-keygen -t rsa -P '' -f /home/hduser/.ssh/id_rsa
sudo sh -c  "cat /home/hduser/.ssh/id_rsa.pub >> /home/hduser/.ssh/authorized_keys"
# Prevent ssh setup questions
sudo sh -c  "printf 'NoHostAuthenticationForLocalhost yes
 Host *  
    StrictHostKeyChecking no' > /home/hduser/.ssh/config"

# Download Scala to the vagrant shared directory if it doesn't exist yet
cd /vagrant
if [ ! -f scala-2.12.9.tgz ]; then
	wget https://www.scala-lang.org/files/archive/scala-2.12.9.tgz
fi
# Unpack Scala and install
sudo tar vxzf scala-2.12.9.tgz -C /usr/local
cd /usr/local
sudo mv scala-2.12.9 scala
sudo chown -R hduser:hadoop scala

# scala variables
sudo sh -c 'echo export SCALA_HOME=/usr/local/scala >> /home/hduser/.bashrc'
sudo sh -c 'echo export PATH=\$PATH:\$SCALA_HOME/bin >> /home/hduser/.bashrc'

# Download zookeeper to the vagrant shared directory if it doesn't exist yet
cd /vagrant
if [ ! -f apache-zookeeper-3.5.5-bin.tar.gz ]; then
	wget https://archive.apache.org/dist/zookeeper/zookeeper-3.5.5/apache-zookeeper-3.5.5-bin.tar.gz
fi
# Unpack zookeeper and install
sudo tar vxzf  apache-zookeeper-3.5.5-bin.tar.gz  -C /usr/local
cd /usr/local
sudo mv apache-zookeeper-3.5.5-bin  zookeeper
cp  /usr/local/zookeeper/conf/zoo_sample.cfg  /usr/local/zookeeper/conf/zoo.cfg
sudo chown -R hduser:hadoop zookeeper

# zookeeper variables
sudo sh -c 'echo export ZOOKEEPER_HOME=/usr/local/zookeeper >> /home/hduser/.bashrc'
sudo sh -c 'echo export PATH=\$PATH:\$ZOOKEEPER_HOME/bin >> /home/hduser/.bashrc'

# Download Kafka to the vagrant shared directory if it doesn't exist yet
# https://archive.apache.org/dist/kafka/0.10.2.2/kafka_2.12-0.10.2.2.tgz
# ftp://ftp.twaren.net/Unix/Web/apache/kafka/2.3.0/kafka_2.12-2.3.0.tgz

cd /vagrant
if [ ! -f kafka_2.12-2.3.0.tgz ]; then
	wget ftp://ftp.twaren.net/Unix/Web/apache/kafka/2.3.0/kafka_2.12-2.3.0.tgz
fi
# Unpack Kafka and install
sudo tar vxzf kafka_2.12-2.3.0.tgz -C /usr/local
cd /usr/local
sudo mv kafka_2.12-2.3.0 apache-kafka
sudo cp /vagrant/config/server-1.properties  /usr/local/apache-kafka/config/server-1.properties 
sudo cp /vagrant/config/server-2.properties  /usr/local/apache-kafka/config/server-2.properties 
sudo cp /vagrant/config/server-3.properties  /usr/local/apache-kafka/config/server-3.properties 
sudo chown -R hduser:hadoop apache-kafka

# Kafka variables
sudo sh -c 'echo export KAFKA_HOME=/usr/local/apache-kafka >> /home/hduser/.bashrc'
sudo sh -c 'echo export PATH=\$PATH:\$KAFKA_HOME/bin >> /home/hduser/.bashrc'
 


sudo cp -R  /vagrant/kafka-samples  /home/hduser/
sudo chown -R hduser:hadoop /home/hduser/kafka-samples

sudo curl https://bintray.com/sbt/rpm/rpm > bintray-sbt-rpm.repo
sudo mv bintray-sbt-rpm.repo /etc/yum.repos.d/
sudo apt-get install -y sbt screen   lsof

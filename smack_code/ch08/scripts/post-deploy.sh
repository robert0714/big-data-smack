#!/bin/bash
# centos 7.6
value=$( grep -ic "entry" /etc/hosts )
if [ $value -eq 0 ]
then
echo "
################ cassandra-cookbook host entry ############
107.170.38.238  MACHINE01
107.170.112.81  MACHINE02
107.170.115.161 MACHINE03
######################################################
" > /etc/hosts
fi
sudo  yum install epel-release -y
sudo  yum install -y java-1.8.0-openjdk  java-1.8.0-openjdk-devel 
sudo ln -s  /usr/lib/jvm/java-1.8.0-openjdk  /usr/lib/jvm/jdk

sudo sh -c 'echo export JAVA_HOME=/usr/lib/jvm/jdk/ >> /home/hduser/.bashrc'

# Add hadoop user
sudo groupadd hadoop
sudo useradd -g hadoop hduser
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



# Download Kafka to the vagrant shared directory if it doesn't exist yet
cd /vagrant
if [ ! -f kafka_2.12-2.3.0.tgz ]; then
	wget ftp://ftp.twaren.net/Unix/Web/apache/kafka/2.3.0/kafka_2.12-2.3.0.tgz
fi
# Unpack Kafka and install
sudo tar vxzf kafka_2.12-2.3.0.tgz -C /usr/local
cd /usr/local
sudo mv kafka_2.12-2.3.0 apache-kafka
sudo chown -R hduser:hadoop apache-kafka

# Kafka variables
sudo sh -c 'echo export KAFKA_HOME=/usr/local/apache-kafka >> /home/hduser/.bashrc'
sudo sh -c 'echo export PATH=\$PATH:\$KAFKA_HOME/bin >> /home/hduser/.bashrc'
 
sudo cp /vagrant/config/server-1.properties  /usr/local/apache-kafka/config/server-1.properties 
sudo cp /vagrant/config/server-2.properties  /usr/local/apache-kafka/config/server-2.properties 
sudo cp /vagrant/config/server-3.properties  /usr/local/apache-kafka/config/server-3.properties 
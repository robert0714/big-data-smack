'''
Created on Aug 26, 2019

@author: robert0714
'''
from configparser import ConfigParser
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pathlib import Path
from abc import ABC, abstractmethod


class AbstractConfig(ABC):

  @abstractmethod
  def returnSqlContext(self)  -> SQLContext: 
    pass


#
# for Cassandra
class PySpakIISIConfig(AbstractConfig):

    def __init__(self):
        # Provide the location of where the config file exists
        self.CONFIG_FILE = 'config.ini' 

    def returnSqlContext(self) -> SQLContext:
        config = self.parse_cassandra_config()
        response = {}
        if not config:
            response['message'] = "Unable to read configuration"
            return response
        
        username :str = config[0]
        password :str = config[1]
        host :str = config[2]
        port :str = config[3]
        spark :SparkSession = SparkSession\
            .builder\
            .config("spark.driver.extraClassPath", str(Path.home()) + "/.ivy2/jars/com.datastax.spark_spark-cassandra-connector_2.11-2.4.1.jar") \
            .master("local[2]") \
            .appName("SparkCassandraApp") \
            .config("spark.cassandra.connection.host", host) \
            .config("spark.cassandra.connection.port", port) \
            .config("spark.cassandra.auth.username", username) \
            .config("spark.cassandra.auth.password", password) \
            .getOrCreate()        
        spark.sparkContext.setLogLevel("OFF")
        sc : SparkContext = spark.sparkContext
        sqlContext : SQLContext = SQLContext(sc)
        return sqlContext
        
    def parse_cassandra_config(self):
        """Parse the configuration file and setup the required configuration."""
         
        config = ConfigParser()
        config.read(self.CONFIG_FILE)
        if 'cassandra_conf' not in config.sections():
            return False
        username = config['cassandra_conf']['username']
        password = config['cassandra_conf']['password']
        host = config['cassandra_conf']['host']
        port = config['cassandra_conf']['port']
    
        return (username, password, host, port)


if __name__ == '__main__':
    pass

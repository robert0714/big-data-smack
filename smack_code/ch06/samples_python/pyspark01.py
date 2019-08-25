# -*- coding: UTF-8 -*-
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pathlib import Path
 
def load_and_get_table_df(keys_space_name, table_name):
    spark = SparkSession\
        .builder\
        .config("spark.driver.extraClassPath",str(Path.home())+"/.ivy2/jars/com.datastax.spark_spark-cassandra-connector_2.11-2.4.1.jar") \
        .master("local[2]") \
        .appName("SparkCassandraApp") \
        .config("spark.cassandra.connection.host", "192.168.99.104") \
        .config("spark.cassandra.connection.port", "9042") \
        .config("spark.cassandra.auth.username", "cassandra") \
        .config("spark.cassandra.auth.password", "cassandra") \
        .getOrCreate()        
    spark.sparkContext.setLogLevel("OFF")
    sc = spark.sparkContext
    sqlContext = SQLContext(sc)
    table_df = sqlContext\
               .read.format("org.apache.spark.sql.cassandra")\
               .options(table=table_name, keyspace=keys_space_name).load() 
    return table_df
 
if __name__ == "__main__":
    print("開始執行RunWordCount")

users = load_and_get_table_df("mykeyspace", "users")
users.show()

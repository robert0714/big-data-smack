# -*- coding: UTF-8 -*-

from abc import ABC, abstractmethod

from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pathlib import Path

class PysparkTest(ABC):
    @abstractmethod
    def returnSparkSession(self): 
        pass

    
class Pyspark02(PysparkTest):
    def __init__(self):
        self.spark: SparkSession  = SparkSession\
                .builder\
                .master("local[2]") \
                .appName("SparkCassandraApp") \
                .config("spark.driver.extraClassPath",str(Path.home())+"/.ivy2/jars/com.datastax.spark_spark-cassandra-connector_2.11-2.4.1.jar") \
                .config("spark.cassandra.connection.host", "192.168.99.103") \
                .config("spark.cassandra.connection.port", "9042") \
                .config("spark.cassandra.auth.username", "cassandra") \
                .config("spark.cassandra.auth.password", "cassandra") \
                .getOrCreate() 
        self.spark.sparkContext.setLogLevel("OFF")
        
        self.sc: SparkContext = self.spark.sparkContext
        self.sqlContext: SQLContext = SQLContext(self.sc)
        
    def load_and_get_table_df(self,keys_space_name, table_name):  
        print("開始執行load_and_get_table_df") 
        #https://spark.apache.org/docs/2.2.0/api/python/pyspark.sql.html#pyspark.sql.DataFrame
        table_df: DataFrame = self.sqlContext\
                   .read.format("org.apache.spark.sql.cassandra")\
                   .options(table=table_name, keyspace=keys_space_name).load() 
        print("連線Cassandra抓資料")
        # https://github.com/datastax/spark-cassandra-connector/blob/master/doc/14_data_frames.md
        return table_df
    
    def returnSparkSession(self): 
        return self.spark
     
     
if __name__ == "__main__": 
        pyspark02: Pyspark02 = Pyspark02()
        try: 
            users  = pyspark02.load_and_get_table_df("mykeyspace", "users")
            users.show()
            
            #https://medium.com/coinmonks/running-pyspark-with-cassandra-using-spark-cassandra-connector-in-jupyter-notebook-9f1dc45e8dc9
            print("下groupBy 與count 語法")
            users.groupBy("user_id").count().orderBy('count', ascending=False).show()
            
             
            # 以下為錯誤示範
            # https://github.com/datastax/spark-cassandra-connector/blob/master/doc/13_spark_shell.md
            print("以下為錯誤示範")
#             df2 = sqlContext.sql("SELECT user_id AS f1, fname as f2 from mykeyspace.users")
#             df2.collect()
        except Exception: 
            print('exception')
            print(Exception)
        finally:
            pyspark02.returnSparkSession().stop()
            print('end')

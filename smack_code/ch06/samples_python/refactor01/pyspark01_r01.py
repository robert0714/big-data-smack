# -*- coding: UTF-8 -*-
from pyspark.sql.dataframe import DataFrame
from refactor01.spark_config import PySpakIISIConfig


def load_and_get_table_df(keys_space_name: str, table_name: str)  -> DataFrame: 
    
    sqlContext = PySpakIISIConfig().returnSqlContext()
        
    table_df : DataFrame = sqlContext\
               .read.format("org.apache.spark.sql.cassandra")\
               .options(table=table_name, keyspace=keys_space_name).load() 
    return table_df
 
if __name__ == "__main__":
    print("開始執行RunWordCount")
    
    users = load_and_get_table_df("mykeyspace", "users")
    users.show()
    
    #https://medium.com/coinmonks/running-pyspark-with-cassandra-using-spark-cassandra-connector-in-jupyter-notebook-9f1dc45e8dc9
    print("下groupBy 與count 語法")
    users.groupBy("user_id").count().orderBy('count', ascending=False).show()
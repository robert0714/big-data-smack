# -*- coding: UTF-8 -*-
from pyspark.sql.dataframe import DataFrame 
from refactor01.spark_config import PySpakCassandraConfig
from refactor01.spark_config import PySpakMSSQLConfig
import logging

class Test(object):

    def load_and_get_table_df(self, keys_space_name: str, table_name: str) -> DataFrame: 
        sqlContext = PySpakCassandraConfig().returnSqlContext()
        table_df : DataFrame = sqlContext\
                   .read.format("org.apache.spark.sql.cassandra")\
                   .options(table=table_name, keyspace=keys_space_name).load() 
        return table_df
    
    def load_and_get_table_df_by_mssql(self , table_name: str) -> DataFrame:  
        table_df : DataFrame = PySpakMSSQLConfig().returnDataFrameReader() \
                    .option("dbtable", table_name) .load()
        return table_df


if __name__ == "__main__":
    logging.info("開始執行RunWordCount")
    try:
        test = Test()
        users = test.load_and_get_table_df("mykeyspace", "users")
        users.show()
    
        # https://medium.com/coinmonks/running-pyspark-with-cassandra-using-spark-cassandra-connector-in-jupyter-notebook-9f1dc45e8dc9
        print("下groupBy 與count 語法")
        users.groupBy("user_id").count().orderBy('count', ascending=False).show()
    except Exception as e:   
        logging.error("%s", e, exc_info=False)
    finally:
        logging.info('end')
     

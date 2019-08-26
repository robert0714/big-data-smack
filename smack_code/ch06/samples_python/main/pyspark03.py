# -*- coding: UTF-8 -*-

from pyspark.sql import SparkSession
from pathlib import Path

if __name__ == "__main__": 
        try: 
            spark = SparkSession \
                .builder \
                .config("spark.driver.extraClassPath",str(Path.home())+"/.ivy2/jars/com.microsoft.sqlserver_mssql-jdbc-7.4.1.jre8.jar") \
                .appName("Python Spark SQL data source example") \
                .getOrCreate()
            
            jdbcDF = spark.read.format("jdbc") \
                .option("url", "jdbc:sqlserver://192.168.99.104:1433;databaseName=master") \
                .option("dbtable", "users") \
                .option("user", "sa") \
                .option("password", "1qaz2wsx#EDC").load()
                
            jdbcDF.show()
        except Exception: 
            print('exception')
            print(Exception)
        finally:
            print('end')

from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dbx2snow.config.ConfigStore import *
from dbx2snow.udfs import *

def tar_snow(spark: SparkSession, limit_50: DataFrame):
    from pyspark.dbutils import DBUtils
    writer = limit_50.write\
                 .format("snowflake")\
                 .options(**{
        "sfUrl": "https://tu22760.ap-south-1.aws.snowflakecomputing.com",
        "sfUser": "DEMOACCOUNT",
        "sfPassword": "{}".format(DBUtils(spark).secrets.get(scope = "bob_snow_demoaccount", key = "SnowSecret")),
        "sfDatabase": "BOBW",
        "sfSchema": "DEMO_OUTPUT",
        "sfWarehouse": "COMPUTE_WH",
        "sfRole": ""
                 })
    writer = writer.option("dbtable", "demo_test1")
    writer = writer.mode("overwrite")
    writer.save()

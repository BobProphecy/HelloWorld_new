from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from sqlscript.config.ConfigStore import *
from sqlscript.udfs import *

def select_hw_customer(spark: SparkSession, in0: DataFrame) -> (DataFrame):

    try:
        registerUDFs(spark)
    except NameError:
        print("registerUDFs not working")

    in0.createOrReplaceTempView("in0")
    df1 = spark.sql("select customer_id, concat(first_name,' ',last_name),phone,email from in0")

    return df1

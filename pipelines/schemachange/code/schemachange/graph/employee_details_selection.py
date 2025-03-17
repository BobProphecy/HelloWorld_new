from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from schemachange.config.ConfigStore import *
from schemachange.functions import *

def employee_details_selection(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("employee_id"), 
        col("f_name"), 
        col("l_name"), 
        col("title"), 
        col("manager_id"), 
        col("test_flag")
    )

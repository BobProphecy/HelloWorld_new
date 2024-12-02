from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from sales_view.udfs import *

def hello_world_hw_customers(spark: SparkSession) -> DataFrame:
    return spark.read.table("`bobwelshmer`.`hello_world`.`hw_customers`")

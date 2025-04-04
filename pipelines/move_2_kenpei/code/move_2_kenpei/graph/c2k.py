from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from move_2_kenpei.config.ConfigStore import *
from move_2_kenpei.functions import *

def c2k(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable("`kenpei`.`hello_world`.`customers`")

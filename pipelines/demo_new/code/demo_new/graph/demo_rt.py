from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_new.config.ConfigStore import *
from demo_new.functions import *

@instrument
def demo_rt(spark: SparkSession, limited_sort_results: DataFrame):
    limited_sort_results.write.format("delta").mode("overwrite").saveAsTable("`bobwelshmer`.`demo_output`.`demo_rt`")

from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_bob1.config.ConfigStore import *
from demo_bob1.functions import *

@instrument
def demo_bdo(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable("`bobwelshmer`.`demo_output`.`demo_bdo`")

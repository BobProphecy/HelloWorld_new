from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from streamer.config.ConfigStore import *
from streamer.functions import *

def Reformat_1(spark: SparkSession, StreamingSource_0: DataFrame) -> DataFrame:
    return StreamingSource_0

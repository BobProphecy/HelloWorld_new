from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from sales_view.udfs import *
from . import *
from .config import *

def sales_view_unity(spark: SparkSession, subgraph_config: SubgraphConfig) -> DataFrame:
    Config.update(subgraph_config)
    df_hello_world_hw_orders = hello_world_hw_orders(spark)
    df_hello_world_hw_customers = hello_world_hw_customers(spark)
    df_join_sales = join_sales(spark, df_hello_world_hw_orders, df_hello_world_hw_customers)
    subgraph_config.update(Config)

    return df_join_sales

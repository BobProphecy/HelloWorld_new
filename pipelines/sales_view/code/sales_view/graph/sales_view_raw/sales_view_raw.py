from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from sales_view.udfs import *
from . import *
from .config import *

def sales_view_raw(spark: SparkSession, subgraph_config: SubgraphConfig) -> DataFrame:
    Config.update(subgraph_config)
    df_customers = customers(spark)
    df_orders = orders(spark)
    df_orders_customers = orders_customers(spark, df_orders, df_customers)
    subgraph_config.update(Config)

    return df_orders_customers

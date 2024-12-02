from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testjson.config.ConfigStore import *
from testjson.udfs import *

def flatten_api_schema(spark: SparkSession, ProphecyAPI: DataFrame) -> DataFrame:
    flt_col = ProphecyAPI\
        .withColumn("item", explode_outer("item"))\
        .withColumn("variable", explode_outer("variable"))\
        .withColumn("item-item", explode_outer("item.item"))\
        .withColumn("item-item-response", explode_outer("item-item.response"))\
        .withColumn("item-item-request-header", explode_outer("item-item.request.header"))\
        .withColumn("item-item-request-url-host", explode_outer("item-item.request.url.host"))\
        .columns
    selectCols = [col("info-_exporter_id") if "info-_exporter_id" in flt_col else col("info._exporter_id")\
                    .alias("info-_exporter_id"),                   col("info-_postman_id") if "info-_postman_id" in flt_col else col("info._postman_id")\
                    .alias("info-_postman_id"),                   col("info-description") if "info-description" in flt_col else col("info.description")\
                    .alias("info-description"),                   col("info-name") if "info-name" in flt_col else col("info.name").alias("info-name"),                   col("info-schema") if "info-schema" in flt_col else col("info.schema").alias("info-schema"),                   col("item-item-name") if "item-item-name" in flt_col else col("item-item.name").alias("item-item-name"),                   col("item-item-request-body-graphql-query") if "item-item-request-body-graphql-query" in flt_col else col("item-item.request.body.graphql.query")\
                    .alias("item-item-request-body-graphql-query"),                   col("item-item-request-body-graphql-variables") if "item-item-request-body-graphql-variables" in flt_col else col("item-item.request.body.graphql.variables")\
                    .alias("item-item-request-body-graphql-variables"),                   col("item-item-request-body-mode") if "item-item-request-body-mode" in flt_col else col("item-item.request.body.mode")\
                    .alias("item-item-request-body-mode"),                   col("item-item-request-header") if "item-item-request-header" in flt_col else col("item-item.request.header")\
                    .alias("item-item-request-header"),                   col("item-item-request-method") if "item-item-request-method" in flt_col else col("item-item.request.method")\
                    .alias("item-item-request-method"),                   col("item-item-request-url-host") if "item-item-request-url-host" in flt_col else col("item-item.request.url.host")\
                    .alias("item-item-request-url-host"),                   col("item-item-request-url-raw") if "item-item-request-url-raw" in flt_col else col("item-item.request.url.raw")\
                    .alias("item-item-request-url-raw"),                   col("item-item-response") if "item-item-response" in flt_col else col("item-item.response")\
                    .alias("item-item-response"),                   col("item-name") if "item-name" in flt_col else col("item.name").alias("item-name"),                   col("variable-key") if "variable-key" in flt_col else col("variable.key").alias("variable-key"),                   col("variable-type") if "variable-type" in flt_col else col("variable.type").alias("variable-type"),                   col("variable-value") if "variable-value" in flt_col else col("variable.value").alias("variable-value")]

    return ProphecyAPI\
        .withColumn("item", explode_outer("item"))\
        .withColumn("variable", explode_outer("variable"))\
        .withColumn("item-item", explode_outer("item.item"))\
        .withColumn("item-item-response", explode_outer("item-item.response"))\
        .withColumn("item-item-request-header", explode_outer("item-item.request.header"))\
        .withColumn("item-item-request-url-host", explode_outer("item-item.request.url.host"))\
        .select(*selectCols)

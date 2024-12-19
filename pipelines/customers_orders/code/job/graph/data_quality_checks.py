from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs import *

@instrument
def data_quality_checks(spark: SparkSession, in0: DataFrame) -> (DataFrame, DataFrame):
    import re
    from pydeequ.checks import Check, CheckLevel, ConstrainableDataTypes
    from pydeequ.verification import VerificationSuite, VerificationResult

    return (in0,
            VerificationResult\
              .checkResultsAsDataFrame(
                spark,
                VerificationSuite(spark)\
                  .onData(in0)\
                  .addCheck(
                    Check(spark, CheckLevel.Warning, "Data Quality Checks")\
                      .isUnique("order_id", hint = "order_id NOT Unique")\
                      .hasCompleteness("customer_id", lambda x: x >= 1.0, hint = "customer_id contains NULLs")\
                      .isNonNegative("amount", lambda x: x >= 1.0, hint = "amount contains negatives")\
                      .isContainedIn("order_status", ["Approved", "Started", "Finished", "Pending"], lambda x: x >= 1.0, hint = "order_status contains invalid values")
                  )\
                  .run()
              )\
              .selectExpr("constraint_status", "constraint_message", "udf_extract_check_and_column(constraint) as parsed")\
              .selectExpr("parsed._1 as check_type", "parsed._2 as column", "constraint_status", "constraint_message"))

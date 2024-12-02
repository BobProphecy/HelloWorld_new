from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataquality.config.ConfigStore import *
from dataquality.functions import *

def DQ_orders(spark: SparkSession, in0: DataFrame) -> (DataFrame, DataFrame):
    import os
    os.environ["SPARK_VERSION"] = '3.3'
    from pydeequ.checks import Check, CheckLevel
    from pydeequ.verification import VerificationSuite, VerificationResult

    return (in0,
            VerificationResult.checkResultsAsDataFrame(
              spark,
              VerificationSuite(spark)\
                .onData(in0)\
                .addCheck(
                  Check(spark, CheckLevel.Error, "Review Check")\
                    .isComplete("order_id")\
                    .isUnique("order_id")\
                    .isUnique("customer_id")\
                    .isNonNegative("amount")\
                    .isContainedIn("order_status", [val.strip() for val in "Started, Pending, Approved, Finished".split(",")])
                )\
                .run()
            ))

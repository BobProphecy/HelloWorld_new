from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataquality.config.ConfigStore import *
from dataquality.functions import *

def DQ_customer(spark: SparkSession, in0: DataFrame) -> (DataFrame, DataFrame):
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
                    .isComplete("customer_id")\
                    .isUnique("customer_id")\
                    .isContainedIn("account_flags", [val.strip() for val in "A, B, C, D".split(",")])
                )\
                .run()
            ))

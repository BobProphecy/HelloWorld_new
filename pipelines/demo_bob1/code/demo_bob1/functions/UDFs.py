from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.lookups import (
    createLookup,
    createRangeLookup,
    lookup,
    lookup_last,
    lookup_match,
    lookup_count,
    lookup_row,
    lookup_row_reverse,
    lookup_nth
)

def registerUDFs(spark: SparkSession):
    spark.udf.register("factorial_UDF", factorial_UDF)
    spark.udf.register("prime_factorization_UDF", prime_factorization_UDF)
    spark.udf.register("square_value_UDF", square_value_UDF)
    

    try:
        from prophecy.utils import ScalaUtil
        ScalaUtil.initializeUDFs(spark)
    except :
        pass

@udf(returnType = IntegerType())
def factorial_UDF(number):

    if number < 0:
        raise Exception('Negative input')

    result = 1

    for i in range(1, number + 1):
        result *= i

        if result > 2 ** 31 - 1:  # Maximum value representable by a signed 32-bit integer
            return float('nan') # Return NaN if the result exceeds the limit

    return result

@udf(returnType = ArrayType(IntegerType()))
def prime_factorization_UDF(number):
    factors = []
    i = 2

    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)

    if number > 1:
        factors.append(number)

    return factors

@udf(returnType = IntegerType())
def square_value_UDF(value: int):
    return value * value

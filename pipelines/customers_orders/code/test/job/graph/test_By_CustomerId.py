from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from job.graph.By_CustomerId import *
from job.config.ConfigStore import *


class By_CustomerIdTest(BaseTestCase):

    def test_unit_test_(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/By_CustomerId/in0/schema.json',
            'test/resources/data/job/graph/By_CustomerId/in0/data/test_unit_test_.json',
            'in0'
        )
        dfIn1 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/By_CustomerId/in1/schema.json',
            'test/resources/data/job/graph/By_CustomerId/in1/data/test_unit_test_.json',
            'in1'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/By_CustomerId/out/schema.json',
            'test/resources/data/job/graph/By_CustomerId/out/data/test_unit_test_.json',
            'out'
        )
        dfOutComputed = By_CustomerId(self.spark, dfIn0, dfIn1)
        assertDFEquals(
            dfOut.select("customer_id", "first_name"),
            dfOutComputed.select("customer_id", "first_name"),
            self.maxUnequalRowsToShow
        )

    def test_unit_test__1(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/By_CustomerId/in0/schema.json',
            'test/resources/data/job/graph/By_CustomerId/in0/data/test_unit_test__1.json',
            'in0'
        )
        dfIn1 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/By_CustomerId/in1/schema.json',
            'test/resources/data/job/graph/By_CustomerId/in1/data/test_unit_test__1.json',
            'in1'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/By_CustomerId/out/schema.json',
            'test/resources/data/job/graph/By_CustomerId/out/data/test_unit_test__1.json',
            'out'
        )
        dfOutComputed = By_CustomerId(self.spark, dfIn0, dfIn1)

    def setUp(self):
        BaseTestCase.setUp(self)
        import os
        fabricName = os.environ['FABRIC_NAME']
        Utils.initializeFromArgs(
            self.spark,
            Namespace(
              file = f"configs/resources/config/{fabricName}.json",
              config = None,
              overrideJson = None,
              defaultConfFile = None
            )
        )

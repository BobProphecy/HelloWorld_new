from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from job.graph.clean_up import *
from job.config.ConfigStore import *


class clean_upTest(BaseTestCase):

    def test_unit_test_(self):
        dfBy_CustomerId = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/clean_up/By_CustomerId/schema.json',
            'test/resources/data/job/graph/clean_up/By_CustomerId/data/test_unit_test_.json',
            'By_CustomerId'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/clean_up/out/schema.json',
            'test/resources/data/job/graph/clean_up/out/data/test_unit_test_.json',
            'out'
        )
        dfOutComputed = clean_up(self.spark, dfBy_CustomerId)
        assertDFEquals(
            dfOut.select("customer_id", "full_name"),
            dfOutComputed.select("customer_id", "full_name"),
            self.maxUnequalRowsToShow
        )

    def test_unit_test__1(self):
        dfBy_CustomerId = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/clean_up/By_CustomerId/schema.json',
            'test/resources/data/job/graph/clean_up/By_CustomerId/data/test_unit_test__1.json',
            'By_CustomerId'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/clean_up/out/schema.json',
            'test/resources/data/job/graph/clean_up/out/data/test_unit_test__1.json',
            'out'
        )
        dfOutComputed = clean_up(self.spark, dfBy_CustomerId)
        assertDFEquals(
            dfOut.select("customer_id", "full_name", "order_id", "amount"),
            dfOutComputed.select("customer_id", "full_name", "order_id", "amount"),
            self.maxUnequalRowsToShow
        )

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

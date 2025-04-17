from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from job.graph.customer_data_cleanup import *
from job.config.ConfigStore import *


class customer_data_cleanupTest(BaseTestCase):

    def test_unit_test_(self):
        dfBy_CustomerId = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/customer_data_cleanup/By_CustomerId/schema.json',
            'test/resources/data/job/graph/customer_data_cleanup/By_CustomerId/data/test_unit_test_.json',
            'By_CustomerId'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/customer_data_cleanup/out/schema.json',
            'test/resources/data/job/graph/customer_data_cleanup/out/data/test_unit_test_.json',
            'out'
        )
        dfOutComputed = customer_data_cleanup(self.spark, dfBy_CustomerId)
        assertDFEquals(
            dfOut.select("customer_id", "full_name"),
            dfOutComputed.select("customer_id", "full_name"),
            self.maxUnequalRowsToShow
        )

    def test_unit_test__1(self):
        dfBy_CustomerId = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/customer_data_cleanup/By_CustomerId/schema.json',
            'test/resources/data/job/graph/customer_data_cleanup/By_CustomerId/data/test_unit_test__1.json',
            'By_CustomerId'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/customer_data_cleanup/out/schema.json',
            'test/resources/data/job/graph/customer_data_cleanup/out/data/test_unit_test__1.json',
            'out'
        )
        dfOutComputed = customer_data_cleanup(self.spark, dfBy_CustomerId)
        assertDFEquals(
            dfOut.select("customer_id", "full_name", "order_id", "amount"),
            dfOutComputed.select("customer_id", "full_name", "order_id", "amount"),
            self.maxUnequalRowsToShow
        )

    def test_unit_test__2(self):
        dfBy_CustomerId = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/customer_data_cleanup/By_CustomerId/schema.json',
            'test/resources/data/job/graph/customer_data_cleanup/By_CustomerId/data/test_unit_test__2.json',
            'By_CustomerId'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/customer_data_cleanup/out/schema.json',
            'test/resources/data/job/graph/customer_data_cleanup/out/data/test_unit_test__2.json',
            'out'
        )
        dfOutComputed = customer_data_cleanup(self.spark, dfBy_CustomerId)
        assertDFEquals(
            dfOut.select(
              "customer_id",
              "full_name",
              "order_id",
              "amount",
              "hash_customer_id",
              "hash_order_id",
              "company_name"
            ),
            dfOutComputed.select(
              "customer_id",
              "full_name",
              "order_id",
              "amount",
              "hash_customer_id",
              "hash_order_id",
              "company_name"
            ),
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

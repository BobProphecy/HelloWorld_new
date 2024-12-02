from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from job.graph.Aggregate_by_customer import *
from job.config.ConfigStore import *


class Aggregate_by_customerTest(BaseTestCase):

    def test_unit_test_(self):
        dfClean_up = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/Aggregate_by_customer/clean_up/schema.json',
            'test/resources/data/job/graph/Aggregate_by_customer/clean_up/data/test_unit_test_.json',
            'clean_up'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/Aggregate_by_customer/out/schema.json',
            'test/resources/data/job/graph/Aggregate_by_customer/out/data/test_unit_test_.json',
            'out'
        )
        dfOutComputed = Aggregate_by_customer(self.spark, dfClean_up)
        assertDFEquals(
            dfOut.select("customer_id", "full_name", "order_count", "sales_total"),
            dfOutComputed.select("customer_id", "full_name", "order_count", "sales_total"),
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

from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from job.graph.OrderBy_Sales import *
from job.config.ConfigStore import *


class OrderBy_SalesTest(BaseTestCase):

    def test_unit_test_(self):
        dfAggregate_by_customer = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/OrderBy_Sales/Aggregate_by_customer/schema.json',
            'test/resources/data/job/graph/OrderBy_Sales/Aggregate_by_customer/data/test_unit_test_.json',
            'Aggregate_by_customer'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/OrderBy_Sales/out/schema.json',
            'test/resources/data/job/graph/OrderBy_Sales/out/data/test_unit_test_.json',
            'out'
        )
        dfOutComputed = OrderBy_Sales(self.spark, dfAggregate_by_customer)
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

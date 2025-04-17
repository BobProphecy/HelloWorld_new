from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from job.graph.by_sales_total_desc import *
from job.config.ConfigStore import *


class by_sales_total_descTest(BaseTestCase):

    def test_unit_test_(self):
        dfAggregate_by_customer = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/by_sales_total_desc/Aggregate_by_customer/schema.json',
            'test/resources/data/job/graph/by_sales_total_desc/Aggregate_by_customer/data/test_unit_test_.json',
            'Aggregate_by_customer'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/by_sales_total_desc/out/schema.json',
            'test/resources/data/job/graph/by_sales_total_desc/out/data/test_unit_test_.json',
            'out'
        )
        dfOutComputed = by_sales_total_desc(self.spark, dfAggregate_by_customer)
        assertDFEquals(
            dfOut.select("customer_id", "full_name", "order_count", "sales_total"),
            dfOutComputed.select("customer_id", "full_name", "order_count", "sales_total"),
            self.maxUnequalRowsToShow
        )

    def test_unit_test__1(self):
        dfAggregate_by_customer = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/by_sales_total_desc/Aggregate_by_customer/schema.json',
            'test/resources/data/job/graph/by_sales_total_desc/Aggregate_by_customer/data/test_unit_test__1.json',
            'Aggregate_by_customer'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/by_sales_total_desc/out/schema.json',
            'test/resources/data/job/graph/by_sales_total_desc/out/data/test_unit_test__1.json',
            'out'
        )
        dfOutComputed = by_sales_total_desc(self.spark, dfAggregate_by_customer)
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

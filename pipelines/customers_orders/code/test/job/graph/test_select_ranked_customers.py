from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from job.graph.select_ranked_customers import *
from job.config.ConfigStore import *


class select_ranked_customersTest(BaseTestCase):

    def test_unit_test_(self):
        dfRow_number_by_customer_count = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/select_ranked_customers/row_number_by_customer_count/schema.json',
            'test/resources/data/job/graph/select_ranked_customers/row_number_by_customer_count/data/test_unit_test_.json',
            'row_number_by_customer_count'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/select_ranked_customers/out/schema.json',
            'test/resources/data/job/graph/select_ranked_customers/out/data/test_unit_test_.json',
            'out'
        )
        dfOutComputed = select_ranked_customers(self.spark, dfRow_number_by_customer_count)
        assertDFEquals(
            dfOut.select("row_count", "region", "CUSTOMER_COUNT"),
            dfOutComputed.select("row_count", "region", "CUSTOMER_COUNT"),
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

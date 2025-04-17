from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from job.graph.row_number_by_customer_count import *
from job.config.ConfigStore import *


class row_number_by_customer_countTest(BaseTestCase):

    def test_unit_test_(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/row_number_by_customer_count/in0/schema.json',
            'test/resources/data/job/graph/row_number_by_customer_count/in0/data/test_unit_test_.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/row_number_by_customer_count/out/schema.json',
            'test/resources/data/job/graph/row_number_by_customer_count/out/data/test_unit_test_.json',
            'out'
        )
        dfOutComputed = row_number_by_customer_count(self.spark, dfIn0)
        assertDFEquals(
            dfOut.select("region", "CUSTOMER_COUNT", "row_count"),
            dfOutComputed.select("region", "CUSTOMER_COUNT", "row_count"),
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

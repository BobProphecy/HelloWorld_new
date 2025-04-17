from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from job.graph.distinct_customer_ids import *
from job.config.ConfigStore import *


class distinct_customer_idsTest(BaseTestCase):

    def test_unit_test_(self):
        dfSelect_customer_id = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/distinct_customer_ids/select_customer_id/schema.json',
            'test/resources/data/job/graph/distinct_customer_ids/select_customer_id/data/test_unit_test_.json',
            'select_customer_id'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/distinct_customer_ids/out/schema.json',
            'test/resources/data/job/graph/distinct_customer_ids/out/data/test_unit_test_.json',
            'out'
        )
        dfOutComputed = distinct_customer_ids(self.spark, dfSelect_customer_id)
        assertDFEquals(dfOut.select("customer_id"), dfOutComputed.select("customer_id"), self.maxUnequalRowsToShow)

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

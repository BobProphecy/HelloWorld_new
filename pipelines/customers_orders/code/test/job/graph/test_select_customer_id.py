from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from job.graph.select_customer_id import *
from job.config.ConfigStore import *


class select_customer_idTest(BaseTestCase):

    def test_unit_test_(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/select_customer_id/in0/schema.json',
            'test/resources/data/job/graph/select_customer_id/in0/data/test_unit_test_.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/select_customer_id/out/schema.json',
            'test/resources/data/job/graph/select_customer_id/out/data/test_unit_test_.json',
            'out'
        )
        dfOutComputed = select_customer_id(self.spark, dfIn0)
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

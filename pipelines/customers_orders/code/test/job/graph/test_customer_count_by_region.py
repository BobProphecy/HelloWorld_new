from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from job.graph.customer_count_by_region import *
from job.config.ConfigStore import *


class customer_count_by_regionTest(BaseTestCase):

    def test_unit_test_(self):
        dfApply_region_business_rule = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/customer_count_by_region/apply_region_business_rule/schema.json',
            'test/resources/data/job/graph/customer_count_by_region/apply_region_business_rule/data/test_unit_test_.json',
            'apply_region_business_rule'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/customer_count_by_region/out/schema.json',
            'test/resources/data/job/graph/customer_count_by_region/out/data/test_unit_test_.json',
            'out'
        )
        dfOutComputed = customer_count_by_region(self.spark, dfApply_region_business_rule)
        assertDFEquals(
            dfOut.select("region", "CUSTOMER_COUNT"),
            dfOutComputed.select("region", "CUSTOMER_COUNT"),
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

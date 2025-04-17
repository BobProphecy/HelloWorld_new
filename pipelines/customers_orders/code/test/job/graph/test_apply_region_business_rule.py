from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from job.graph.apply_region_business_rule import *
from job.config.ConfigStore import *


class apply_region_business_ruleTest(BaseTestCase):

    def test_unit_test_(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/apply_region_business_rule/in0/schema.json',
            'test/resources/data/job/graph/apply_region_business_rule/in0/data/test_unit_test_.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/job/graph/apply_region_business_rule/out/schema.json',
            'test/resources/data/job/graph/apply_region_business_rule/out/data/test_unit_test_.json',
            'out'
        )
        dfOutComputed = apply_region_business_rule(self.spark, dfIn0)
        assertDFEquals(
            dfOut.select(
              "customer_id",
              "first_name",
              "last_name",
              "phone",
              "email",
              "country_code",
              "account_open_date",
              "account_flags",
              "region"
            ),
            dfOutComputed.select(
              "customer_id",
              "first_name",
              "last_name",
              "phone",
              "email",
              "country_code",
              "account_open_date",
              "account_flags",
              "region"
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

import unittest

from test.job.graph.test_join_by_customer_id import *
from test.job.graph.test_aggregate_sales_by_customer import *
from test.job.graph.test_row_number_by_customer_count import *
from test.job.graph.test_customer_data_cleanup import *
from test.job.graph.test_customer_count_by_region import *
from test.job.graph.test_select_ranked_customers import *
from test.job.graph.test_apply_region_business_rule import *
from test.job.graph.test_select_customer_id import *
from test.job.graph.test_by_sales_total_desc import *
from test.job.graph.test_distinct_customer_ids import *

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(unittest.TestSuite())

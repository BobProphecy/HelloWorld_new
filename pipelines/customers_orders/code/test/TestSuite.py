import unittest

from test.job.graph.test_join_by_customer_id import *
from test.job.graph.test_aggregate_sales_by_customer import *
from test.job.graph.test_customer_data_cleanup import *
from test.job.graph.test_by_sales_total_desc import *

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(unittest.TestSuite())

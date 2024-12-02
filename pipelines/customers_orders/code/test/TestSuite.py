import unittest

from test.job.graph.test_By_CustomerId import *
from test.job.graph.test_Aggregate_by_customer import *
from test.job.graph.test_clean_up import *
from test.job.graph.test_OrderBy_Sales import *

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(unittest.TestSuite())

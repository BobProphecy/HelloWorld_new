from sales_view.graph.sales_view_raw.config.Config import SubgraphConfig as sales_view_raw_Config
from sales_view.graph.sales_view_unity.config.Config import SubgraphConfig as sales_view_unity_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, sales_view_raw: dict=None, sales_view_unity: dict=None, **kwargs):
        self.spark = None
        self.update(sales_view_raw, sales_view_unity)

    def update(self, sales_view_raw: dict={}, sales_view_unity: dict={}, **kwargs):
        prophecy_spark = self.spark
        self.sales_view_raw = self.get_config_object(
            prophecy_spark, 
            sales_view_raw_Config(prophecy_spark = prophecy_spark), 
            sales_view_raw, 
            sales_view_raw_Config
        )
        self.sales_view_unity = self.get_config_object(
            prophecy_spark, 
            sales_view_unity_Config(prophecy_spark = prophecy_spark), 
            sales_view_unity, 
            sales_view_unity_Config
        )
        pass

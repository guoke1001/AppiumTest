#coding=utf-8
__author__ = 'tangyao'

from hamcrest import *

from config.driver_config import DriverConfig
from page.xueqiupage import XueQiuPage


class TestSearch:
    def setup(self):
        self.driver_config=DriverConfig()
        self.driver=self.driver_config.get_driver()
        self.xueqiu=XueQiuPage(self.driver)
    def test_get_price(self):

        assert_that(self.xueqiu.goto_search().search("阿里巴巴").select(0).getprice("BABA"),close_to(100,200))


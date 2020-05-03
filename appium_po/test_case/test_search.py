#coding=utf-8
__author__ = 'tangyao'

from appium_po.page.xueqiupage import XueQiuPage
from hamcrest import *


class TestSearch:
    def setup(self):
        self.xueqiu=XueQiuPage()
    def test_get_price(self):
        assert_that(self.xueqiu.goto_search().search("阿里巴巴").select(0).getprice("BABA"),close_to(100,200))


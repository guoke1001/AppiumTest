#coding=utf-8
__author__ = 'tangyao'

from config.driver_config import DriverConfig
from page.xueqiupage import XueQiuPage


class TestTrade:
    def setup(self):
        self.driver_config = DriverConfig()
        self.driver = self.driver_config.get_driver()
        self.xueqiu = XueQiuPage(self.driver)
        self.trade=self.xueqiu.goto_trade()
    def test_open_hs(self):
        self.trade.open_hs()
    def test_us(self):
        self.trade.us_trade()




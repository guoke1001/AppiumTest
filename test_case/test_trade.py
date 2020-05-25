#coding=utf-8
__author__ = 'tangyao'

from config.driver_config import DriverConfig
from page.xueqiupage import XueQiuPage


class TestTrade:
    # def setup(self):
    #     self.driver = DriverConfig().get_driver()
    #     self.xueqiu = XueQiuPage(self.driver)
    #     self.trade=self.xueqiu.goto_trade()
    def test_open_hs(self,common_driver):
        self.xueqiu = XueQiuPage(common_driver)
        self.xueqiu.goto_trade().open_hs()
    # def test_us(self,common_driver):
    #     self.xueqiu = XueQiuPage(common_driver)
    #     self.xueqiu.goto_trade().us_trade()




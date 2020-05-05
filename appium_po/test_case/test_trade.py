#coding=utf-8
__author__ = 'tangyao'

from appium_po.page.xueqiupage import XueQiuPage


class TestTrade:
    def setup(self):
        xueqiu=XueQiuPage()
        self.trade=xueqiu.goto_trade()
    def test_open_hs(self):
        self.trade.open_hs()



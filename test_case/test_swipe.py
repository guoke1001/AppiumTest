#coding=utf-8
__author__ = 'tangyao'

from config.driver_config import DriverConfig
from page.xueqiu.Xue_Qiu_Page import Xue_Qiu_Page


class TestSwipe:
    def setup(self):
        # self.driver_config=DriverConfig()
        self.driver=DriverConfig().get_driver()
        self.xue_qiu=Xue_Qiu_Page(self.driver)


    def test_swipe(self):
        self.xue_qiu.swipe()

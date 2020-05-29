#coding=utf-8
__author__ = 'tangyao'

import allure
from config.log_config import logger
from page.xueqiupage import XueQiuPage

lo=logger()
allure.feature("测试长按")
class Test_Pre:
    allure.story("长按")
    allure.severity(allure.severity_level.CRITICAL)
    def test_pre(self,common_driver):
        xueqiu=XueQiuPage(common_driver)
        text=xueqiu.goto_hq().press().select(0)
        lo.info(text)
        assert "贵州茅台"==text

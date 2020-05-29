#coding=utf-8
__author__ = 'tangyao'

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from common.base_page import BasePage


class Hang_Qing_Page(BasePage):
    _info=(By.ID,"com.xueqiu.android:id/content_recycler")
    _product=(By.XPATH,"//*[contains(@text,'贵州茅台')]")
    _zhid=(By.XPATH,"//*[contains(@text,'置顶')]")


    def press(self):
        el=self.find(self._product)
        TouchAction(self.driver).long_press(el).perform()
        self.find(self._zhid).click()
        return self
    def select(self,index):
        te=self.driver.find_elements(*self._info)[0].find_element_by_id("com.xueqiu.android:id/portfolio_stockName").text
        return te

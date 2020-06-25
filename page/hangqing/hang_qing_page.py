#coding=utf-8
__author__ = 'tangyao'

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from common.base_page import BasePage


class Hang_Qing_Page(BasePage):
    _info=(By.ID,"com.xueqiu.android:id/content_recycler")
    _product=(By.XPATH,"//*[contains(@text,'贵州茅台')]")
    _zhid=(By.XPATH,"//*[contains(@text,'置顶')]")
    _big=(By.XPATH,"//*[@text='大事']")


    def press(self):
        el=self.find_element(self._product)
        self.lon_press(el)
        self.find_element(self._zhid).click()
        return self
    def select(self,index):
        te=self.find_elements(self._info)[index].find_element_by_id("com.xueqiu.android:id/portfolio_stockName").text
        return te
    def go_to_big(self):
        self.find_element(self._big).click()
        tex=self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).getChildByText(new UiSelector().className("android.widget.TextView"), "中国平安")').text
        return tex

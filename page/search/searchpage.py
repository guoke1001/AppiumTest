#coding=utf-8
__author__ = 'tangyao'

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.base_page import BasePage


class SearchPage(BasePage):

    _search_key=(By.XPATH,"//*[contains(@text,'BABA')]")
    _input_key=(By.ID,"com.xueqiu.android:id/search_input_text")
    def search(self,keywords):
        self.find_element(self._input_key).send_keys(keywords)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self._search_key))

        return self
    def select(self,index):
        self.driver.find_elements_by_id("com.xueqiu.android:id/name")[index].click()
        return self
    def getprice(self,stock_type):
        price = float(self.driver.find_element_by_xpath("//*[contains(@text,'"+stock_type+"')]/../../..//*[contains(@resource-id,'current_price')]").text)
        return price







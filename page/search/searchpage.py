#coding=utf-8
__author__ = 'tangyao'

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SearchPage():


    def search(self,keywords):
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(keywords)

        # WebDriverWait(self.driver, 10, 2).until(expected_conditions.visibility_of_element_located(('BABA')))

        return self
    def select(self,index):
        self.driver.find_elements_by_id("com.xueqiu.android:id/name")[index].click()
        return self
    def getprice(self,stock_type):

        price = float(self.driver.find_element_by_xpath("//*[contains(@text,'"+stock_type+"')]/../../..//*[contains(@resource-id,'current_price')]").text)
        return price







#coding=utf-8
__author__ = 'tangyao'

from appium.webdriver.webdriver import WebDriver


class SearchPage():

    def __init__(self,driver:WebDriver):
        self.driver=driver

    def search(self,keywords):
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(keywords)
        return self
    def select(self,index):
        self.driver.find_elements_by_id("com.xueqiu.android:id/name")[index].click()
        return self
    def getprice(self,stock_type):
        price = float(self.driver.find_element_by_xpath("//*[contains(@text,'"+stock_type+"')]/../../..//*[contains(@resource-id,'current_price')]").text)
        return price







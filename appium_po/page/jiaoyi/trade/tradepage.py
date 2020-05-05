#coding=utf-8
__author__ = 'tangyao'

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TradePage:
    _open_hs=(By.XPATH,"//*[contains(@text,'A股开户')]")
    def __init__(self,driver:WebDriver):
        self.driver=driver

    def open_hs(self):
        #显式等待
        WebDriverWait(self.driver,20).until(expected_conditions.visibility_of_element_located(self._open_hs))
        self.driver.find_element(*self._open_hs).click()
        return self

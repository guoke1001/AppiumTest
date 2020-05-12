#coding=utf-8
__author__ = 'tangyao'

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TradePage:
    _hs=(By.XPATH,"//*[@text='沪深']")
    _open_hs=(By.XPATH,"//*[contains(@text,'A股开户')]")
    _us_trade=((By.XPATH,"//*[contains(@text,'港美')]"))
    def __init__(self,driver:WebDriver):
        self.driver=driver

    def open_hs(self):

        #显式等待
        WebDriverWait(self.driver,20).until(expected_conditions.visibility_of_element_located(self._hs))
        self.driver.find_element(*self._hs).click()
        self.driver.find_element(*self._open_hs).click()
        return self
    def us_trade(self):
        self.driver.find_element(*self._us_trade).click()

        return self


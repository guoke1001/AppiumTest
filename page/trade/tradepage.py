#coding=utf-8
__author__ = 'tangyao'

from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.base_page import BasePage
from config.log_config import logger

lo=logger()
class TradePage(BasePage):
    _hs=(By.XPATH,"//*[@text='沪深']")
    # _open_hs=(MobileBy.ACCESSIBILITY_ID,'A股开户')
    _open_hs=(By.XPATH,"//*[contains(@text,'A股开户')]")
    _us_trade=(By.XPATH,"//*[contains(@text,'港美')]")
    _phone_number=(By.ID,'phone-number')
    _ss=(MobileBy.ACCESSIBILITY_ID,"开户服务由平安证券提供")

    def open_hs(self):
        self.find_element(self._open_hs).click()
        # self.driver.find_element(*self._open_hs).click()
        # WebDriverWait(self.driver,30,0.1).until(expected_conditions.visibility_of_element_located(self._ss))
        # self.driver.find_element_by_id('phone-number').send_keys("18612977085")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("phone-number")').send_keys("111")
        return self
    def us_trade(self):
        self.find_element(self._us_trade).click()

        return self


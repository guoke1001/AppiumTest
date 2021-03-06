#coding=utf-8
__author__ = 'tangyao'

from time import sleep

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.base_page import BasePage
from common.gesture_mainpulation import gesture_mainpulation


class Xue_Qiu_Page(BasePage):

    _lock=(By.XPATH,"//*[@text='关注']")
    def swipe(self):
        self.wipe=gesture_mainpulation(self.driver)
        self.find(self._lock).click()

        self.wipe.swipe_up()


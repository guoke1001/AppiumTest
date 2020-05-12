#coding=utf-8
__author__ = 'tangyao'

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from common.Base_page import BasePage


class Use_Profile_Page(BasePage):

    _login_webchat=(By.XPATH,"//*[@text='微信']")
    def __init__(self,driver:WebDriver):
        self.driver=driver

    def login_by_webchat(self):
        self.driver.find_element(*self._login_webchat).click()
        text=self.find(self.toast_locator()).text
        if text!=None:
            return text
        else:
            pass

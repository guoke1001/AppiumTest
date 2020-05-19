#coding=utf-8
__author__ = 'tangyao'

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from config.log_config import logger

log = logger()


class Use_Profile_Page(BasePage):

    _login_webchat=(By.XPATH,"//*[@text='微信']")

    def login_by_webchat(self):
        log.info("page")
        self.driver.find_element(*self._login_webchat).click()
        text=self.find(self.toast_locator()).text
        log.info('111111111111111'+text)
        if text!=None:
            self.screen_shot("登录")
            return text
        else:
            pass

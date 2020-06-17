#coding=utf-8
__author__ = 'tangyao'

import os
from datetime import datetime

import allure
from appium.webdriver import WebElement
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config.log_config import logger
from config.global_config import SCREENSHOT_DIR

log=logger()
class BasePage:
    black_list = [
        (By.ID, 'image_cancel'),
    ]
    max = 0

    def __init__(self,driver:WebDriver):
        self.driver=driver

    #封装查找单个方法，使用显示等待，考虑进入app可能会有升级等弹窗，使用blacklist来判断
    def find_element(self, locator) -> WebElement:
        #todo: 处理弹框 异常处理 动态浮动的元素的处理
        try:
            return WebDriverWait(self.driver,10,0.2).until(expected_conditions.visibility_of_element_located(locator))
        except Exception as e:
            #黑名单处理
            if BasePage.max > 3:
                log.info("没有找到元素")
                raise e
            BasePage.max +=1
            for black in self.black_list:
                elements = self.driver.find_elements(*black)
                if len(elements) >= 1:
                    elements[0].click()

            return self.find_element(locator)

     #封装查找元素方法，返回的是list
    def find_elements(self, locator) -> WebElement:
        #todo: 处理弹框 异常处理 动态浮动的元素的处理
        try:
            return WebDriverWait(self.driver,10,0.2).until(expected_conditions.visibility_of_any_elements_located(locator))
            # return self.driver.find_element(*locator)

        except Exception as e:
            #黑名单处理
            if BasePage.max > 3:
                log.info("没有找到元素")
                raise e
            BasePage.max += 1
            for black in self.black_list:
                elements = self.driver.find_elements(*black)
                if len(elements) >= 1:
                    elements[0].click()

            return self.find_elements(locator)


    @classmethod
    def id_locator(cls,value):
        return (By.ID,value)

    @classmethod
    def text_locator(cls,value):
        return (By.NAME,value)

    @classmethod
    def xpath_locator(cls,value):
        return (By.XPATH,"//*[@text=%s]"%value)

    @classmethod
    def toast_locator(cls):
        return (By.XPATH,"//*[@class='android.widget.Toast']")

    def lon_press(self,locator,times=None):
        TouchAction(self.driver).long_press(locator,times).perform()

    def get_webview(self,webname):
        webviews=self.driver.contexts
        for web in webviews:
            if webname in web:
                return webname
    def swich_webview(self):
        self.driver.switch_to.context(self.get_webview("xxxx"))


    #截屏
    def screen_shot(self,describ=None):
        if not os.path.exists(SCREENSHOT_DIR):
            os.mkdir(SCREENSHOT_DIR)
        file_name=SCREENSHOT_DIR+"/{}_{}.png".format((datetime.now()).strftime('%Y-%m-%d %H:%M:%S'),describ)
        self.driver.save_screenshot(file_name)
        with open(file_name,'rb') as f:
            file=f.read()
        allure.attach(file,describ,allure.attachment_type.PNG)
        log.info("截图文件保存在:{}".format(file_name))

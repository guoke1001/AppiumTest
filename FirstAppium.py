#coding=utf-8
__author__ = 'tangyao'

from appium import webdriver
from selenium.webdriver.common.by import By
'''
appium入门，简单事例
'''

class TestAppium:

    def setup(self):
        server = "http://localhost:4723/wd/hub"
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # caps["app"] = "./app/xueqiu.apk"
        #每次跑用例不重置app
        caps["noReset"]=True
        #权限弹窗自动处理
        caps["autoGrantPermissions"] = True

        self.driver = webdriver.Remote(server, caps)

        self.driver.implicitly_wait(15)

    def test_phone(self):
        self.driver.find_element(By.id,"com.xueqiu.android:id/user_profile_icon").click()
        # self.driver.find_element_by_id("com.xueqiu.android:id/user_profile_icon").click()

    def teardown(self):
        self.driver.quit()



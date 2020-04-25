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
        # self.driver.find_element(By.ID,"com.xueqiu.android:id/user_profile_icon").click()

        # print(self.driver.find_element_by_xpath("//*[contains(@text,'我的')]").get_attribute("index"))
        self.driver.find_element_by_xpath("//*[@text='我的']").click()
        self.driver.find_element(By.XPATH,"//*[@text='手机号']").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/register_phone_number").send_keys("18612977085")
        print(self.driver.find_element_by_id("com.xueqiu.android:id/register_phone_number").get_attribute("class"))

        #获取当前activity
        print(self.driver.current_activity)
        print(self.driver.current_context)
        # print(self.driver.current_window_handle)
        # print(self.driver.current_url)


        # self.driver.find_element_by_id("com.xueqiu.android:id/user_profile_icon").click()

    def testswipe(self):
        self.driver.find_element_by_xpath("//*[@text='行情']").click()

        self.driver.find_element_by_xpath("//*[@text='市场']").click()
        size=self.driver.get_window_size()
        width=size["width"]
        height=size["height"]
        self.driver.swipe(width*0.8,height*0.8,width*0.1,height*0.2,1000)
    def test_uiaumator(self):
        self.driver.find_element_by_xpath("//*[@text='行情']").click()
        self.driver.find_element_by_xpath("//*[@text='市场']").click()

        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(2)).scrollIntoView(new UiSelector().text("金通灵").instance(0));').click()
        self.driver.find_element_by_android_uiautomator(
            '''new UiScrollable
            (new UiSelector().scrollable(true).instance(0)).scrollIntoView(
            new UiSelector().text("HooBl").instance(0));''').click()

    def teardown(self):
        # self.driver.quit()
        pass



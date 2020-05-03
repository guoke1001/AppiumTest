#coding=utf-8
__author__ = 'tangyao'

from appium import webdriver

from appium_po.page.searchpage import SearchPage


class XueQiuPage:
    def __init__(self):
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
        #隐示等待
        self.driver.implicitly_wait(15)


    def goto_search(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        return SearchPage(self.driver)
#coding=utf-8
__author__ = 'tangyao'

from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from common.Base_page import BasePage
from page.search.searchpage import SearchPage
from page.trade.tradepage import TradePage
from page.use_profile.use_profile_page import Use_Profile_Page
from page.xueqiu.Xue_Qiu_Page import Xue_Qiu_Page


class XueQiuPage(BasePage):
    driver=None
    _appPackage="com.xueqiu.android"
    _appActivity=".view.WelcomeActivityAlias"

    def __init__(self,driver:WebDriver):
        self.driver=driver
        if XueQiuPage.driver==None:
            print('first')
            XueQiuPage.driver=self.driver
        else:
            print('11111')
            self.driver.start_activity(self._appPackage, self._appActivity)

    # def first_App(self):
    #     server = "http://localhost:4723/wd/hub"
    #     caps = {}
    #     caps["platformName"] = "android"
    #     caps["deviceName"] = "5483e9c3"
    #     caps["appPackage"] = self._appPackage
    #     caps["appActivity"] = self._appActivity
    #     # caps["app"] = "./app/xueqiu.apk"
    #     # 每次跑用例不重置app
    #     caps["noReset"] = True
    #     # 权限弹窗自动处理
    #     caps["autoGrantPermissions"] = True
    #
    #     self.driver = webdriver.Remote(server, caps)
    #     # 隐式等待
    #     self.driver.implicitly_wait(15)
    #     XueQiuPage.driver=self.driver
    #
    #

    def goto_search(self):

        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        return SearchPage(self.driver)
    def goto_trade(self):
        self.driver.find_element_by_xpath("//*[@text='交易']").click()
        return TradePage(self.driver)
    def goto_profile(self):
        self.driver.find_element_by_xpath("//*[@text='我的']").click()
        return Use_Profile_Page(self.driver)
    def goto_xueqiu(self):
        self.driver.find_element_by_xpath("//*[@text='雪球']")
        return Xue_Qiu_Page(self.driver)

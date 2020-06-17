#coding=utf-8
__author__ = 'tangyao'

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.base_page import BasePage
from config.log_config import logger
from page.HANGQING.hang_qing_page import Hang_Qing_Page
from page.search.searchpage import SearchPage
from page.trade.tradepage import TradePage
from page.use_profile.use_profile_page import Use_Profile_Page
from page.xueqiu.Xue_Qiu_Page import Xue_Qiu_Page


lo=logger()
class XueQiuPage(BasePage):
    # drivers=None
    _appPackage="com.xueqiu.android"
    _appActivity=".view.WelcomeActivityAlias"
    # _skill_loading=(By.ID,"com.xueqiu.android:id/tv_skip")
    _skill_loading=(By.ID,"com.xueqiu.android:id/tv_skip_fullscreen")
    # _skill_loading=(By.XPATH,"//*[contains(@text,'跳过')]")
    _hq=(By.XPATH,"//*[contains(@text,'行情')]")


    #
    # def __init__(self,driver:WebDriver):
    #     super().__init__(driver)
    #     # if XueQiuPage.drivers==None:
    #     #     print('first')
    #     #     XueQiuPage.drivers=self.driver
    #     # else:
    #     #     print('11111')
    #     #     self.driver.start_activity(self._appPackage, self._appActivity)
    #     # print(WebDriverWait(self.driver, 10, 2).until(expected_conditions.visibility_of_element_located(self._skill_loading)))
    #     self.find(self._skill_loading).click()



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

    def loading_page(self):

        self.find_element(self._skill_loading).click()
        return self
    def goto_search(self):

        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        return SearchPage(self.driver)
    def goto_trade(self):
        self.find_element((By.XPATH,"//*[@text='交易']")).click()
        lo.info(self.driver.contexts)
        return TradePage(self.driver)
    def goto_profile(self):
        self.driver.find_element_by_xpath("//*[@text='我的']").click()
        return Use_Profile_Page(self.driver)
    def goto_xueqiu(self):
        self.driver.find_element_by_xpath("//*[@text='雪球']")
        return Xue_Qiu_Page(self.driver)
    def goto_hq(self):
        self.find_element(self._hq).click()
        return Hang_Qing_Page(self.driver)

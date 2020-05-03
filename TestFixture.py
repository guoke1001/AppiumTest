#coding=utf-8
__author__ = 'tangyao'

import pytest
from appium import webdriver

'''
fixture:
  1.用法https://www.cnblogs.com/huizaia/p/10331469.html
  2.yield上面的是setup，下面的是teardown

'''
class TestFixture:


    @pytest.fixture()
    def tfixture(self):
        server = "http://localhost:4723/wd/hub"
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # caps["app"] = "./app/xueqiu.apk"
        # 每次跑用例不重置app
        caps["noReset"] = True
        # 权限弹窗自动处理
        caps["autoGrantPermissions"] = True

        self.driver = webdriver.Remote(server, caps)

        self.driver.implicitly_wait(15)
        yield
        self.driver.quit()

    @pytest.mark.parametrize("keywords,stock_type,prices", [
        ("阿里巴巴", "BABA", "202.67"),
        ("小米", "01810", "10.20")
    ])
    def test_search(self,tfixture, keywords, stock_type, prices):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(keywords)
        # lis=self.driver.find_elements_by_id("com.xueqiu.android:id/name")
        self.driver.find_elements_by_id("com.xueqiu.android:id/name")[0].click()

        # for i in lis:
        #     if i.text==u"阿里巴巴":
        #         i.click()
        #         break
        price = self.driver.find_element_by_xpath(
            "//*[contains(@text,'" + stock_type + "')]/../../..//*[contains(@resource-id,'current_price')]").text
        assert price == prices
        # self.driver.find_element_by_xpath("//*[contains(@text,'阿里')]")

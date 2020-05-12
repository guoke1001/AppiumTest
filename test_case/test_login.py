#coding=utf-8
__author__ = 'tangyao'

from config.driver_config import DriverConfig
from page.xueqiupage import XueQiuPage


class TestLogin:

    def setup_class(self):
        self.driver_config=DriverConfig()
        self.driver=self.driver_config.get_driver()
        self.xueqiu=XueQiuPage(self.driver)
        self.login=self.xueqiu.goto_profile()

    def test_login_by_webchat(self):
        tex=self.login.login_by_webchat()
        print(tex)
        assert '您尚未安装微信' in tex



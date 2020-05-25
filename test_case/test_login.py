# #coding=utf-8
# __author__ = 'tangyao'
#
# import allure
#
# from config.log_config import logger
# from config.driver_config import DriverConfig
# from conftest import common_driver
# from page.xueqiupage import XueQiuPage
#
# log=logger()
# # @allure.title("登录用例")#标题
# @allure.feature("测试登录用例")#分为大类
# class TestLogin:
#     #
#     # def setup(self,common_driver):
#     #
#     #     self.xueqiu=XueQiuPage(common_driver)
#     #     self.login=self.xueqiu.goto_profile()
#
#
#
#     @allure.story("微信登录")#小类
#     @allure.severity(allure.severity_level.CRITICAL)#bug严重等级
#     def test_login_by_webchat(self,common_driver):
#         log.info("test")
#         xueqiu = XueQiuPage(common_driver)
#
#         login = xueqiu.goto_profile()
#         tex=login.login_by_webchat()
#         # self.xueqiu.screen_shot("登录")
#         assert '您尚未安装微信' in tex
#
#

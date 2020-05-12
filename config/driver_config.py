#coding=utf-8
__author__ = 'tangyao'

from appium import webdriver


class DriverConfig:
    _appPackage = "com.xueqiu.android"
    _appActivity = ".view.WelcomeActivityAlias"
    def get_driver(self):
        try:
            server = "http://localhost:4723/wd/hub"
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "5483e9c3"
            caps["appPackage"] = self._appPackage
            caps["appActivity"] = self._appActivity
            caps['unicodeKeyboard'] = 'true'  # 是否支持unicode的键盘。如果需要输入中文，要设置为“true”
            caps['resetKeyboard'] = 'true'  # 是否在测试结束后将键盘重轩为系统默认的输入法。
            caps['newCommandTimeout'] = '120'  # Appium服务器待appium客户端发送新消息的时间。默认为60秒
            # caps["app"] = "./app/xueqiu.apk"
            caps["noReset"] = True #不重新安装app
            # 权限弹窗自动处理
            caps["autoGrantPermissions"] = True #处理权限弹窗 True默认授权

            self.driver = webdriver.Remote(server, caps)
            # 隐式等待
            self.driver.implicitly_wait(15)
            return self.driver
        except Exception as e:
            raise e

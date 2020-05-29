#coding=utf-8
__author__ = 'tangyao'

import multiprocessing
import os
import subprocess
from datetime import datetime
from time import sleep

import yaml
from appium import webdriver

from config.log_config import logger
from config.global_config import project_path, IMPLICITLY_WAIT_TIME

log=logger()
class DriverConfig:
    def __init__(self,device_info):
        self.device_info=device_info
        self.system_port=device_info['serverPort']+2000
        cmd="appium -p {0} -bp {1} -U {2} --log-timestamp --local-timezone".format(self.device_info['serverPort'],self.device_info["serverPort"]+2000,
                                                  self.device_info["deviceName"])
        log.info(cmd)
        # os.system(cmd)
        subprocess.Popen(cmd,shell=True,stdout=open("./logs/{0}_{1}_appium.log".format(datetime.now().strftime("%Y-%m-%d_%H:%M:%S"),device_info["deviceName"]),'a'),stderr=subprocess.STDOUT)
        sleep(5) #防止appium服务没有完全启动就执行测试报错

    def get_driver(self,automationName='appium'):
        # 配置yaml文件路径
        DESIRED_CAPS_PATH=os.path.join(project_path,"yaml","desired_caps.yaml")
        with open(DESIRED_CAPS_PATH,encoding="utf-8") as file:
            data=yaml.load(file,Loader=yaml.FullLoader)

        log.info("读取配置文件成功")
        log.info(data)
        try:
            caps = {}
            caps["platformName"] = data["platformName"]
            caps["deviceName"] = self.device_info["deviceName"]
            caps["appPackage"] = data["appPackage"]
            caps['platformVersion'] = self.device_info["platformVersion"]
            caps["appActivity"] = data["appActivity"]
            # caps['unicodeKeyboard'] = data["unicodeKeyboard"] # 是否支持unicode的键盘。如果需要输入中文，要设置为“true”
            # caps['resetKeyboard'] = data["resetKeyboard"] # 是否在测试结束后将键盘重轩为系统默认的输入法。
            caps['newCommandTimeout'] = data["newCommandTimeout"]# Appium服务器待appium客户端发送新消息的时间。默认为60秒
            caps['systemPort'] = self.system_port  # 重要，不定义会出现socket hang up错误！
            # caps["app"] = data["app"]
            caps["noReset"] = data["noReset"] #不重新安装app
            if automationName!='appium':
                caps['automationName']=automationName
            # 权限弹窗自动处理
            caps["autoGrantPermissions"] = data["autoGrantPermissions"] #处理权限弹窗 True默认授权
            driver=webdriver.Remote("http://localhost:{0}/wd/hub".format(str(self.device_info['serverPort'])), caps)
            # 隐式等待
            # driver.implicitly_wait(IMPLICITLY_WAIT_TIME)
            log.info("启动App成功")
            return driver
        except Exception as e:
            raise e

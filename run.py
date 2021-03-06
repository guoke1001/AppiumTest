#coding=utf-8
__author__ = 'tangyao'

import os
import shutil

import pytest
from multiprocessing import Pool
from config import global_config
from config.log_config import logger
from util.global_manager import GlobalManager

log=logger()

device_infos = [
        {"platformVersion": "7.1.2", "serverPort": 4726, "deviceName": "5483e9c3"},
        {"platformVersion": "9", "serverPort": 4727, "deviceName": "emulator-5554"}
    ]
def run_pytest(device_info):
    pytest.main([f"--cmdopt={device_info}","./test_case","--alluredir","./report/allure_result"])

def pytest_start():

    with Pool(len(device_infos)) as pool:
        pool.map(run_pytest, device_infos)
        pool.close()
        pool.join()

def close_appium_server():
    for i in device_infos:
        os.system("lsof -n -i:{0}".format(format(i.get('serverPort'))+" | grep LISTEN | awk '{print $2}' | xargs kill"))
def generate_report():
    log.info("生成报告……")
    if not os.path.exists(global_config.REPORT_RESULT_PATH):
        os.mkdir(global_config.REPORT_RESULT_PATH)
    os.system(f"allure generate {global_config.REPORT_RESULT_PATH} -o {global_config.REPORT_END_PATH} --clean")
            # 复制history文件夹，在本地生成趋势图
    REPORT_RESULT_FILES=global_config.REPORT_RESULT_PATH
    files = os.listdir(REPORT_RESULT_FILES)
    result_history_dir = os.path.join(REPORT_RESULT_FILES, "history")
    # 如果不存在则先创建文件夹
    if not os.path.exists(result_history_dir):
        os.mkdir(result_history_dir)
    for file in files:
        shutil.copy(os.path.join(REPORT_RESULT_FILES, file), result_history_dir)



if __name__ == '__main__':
    global_m=GlobalManager()
    global_m.delet_report()
    pytest_start()
    close_appium_server()
    generate_report()

#coding=utf-8
__author__ = 'tangyao'

import os
import shutil

from config.log_config import logger
from config.global_config import SCREENSHOT_DIR, REPORT_PATH, LOG_FOLDER


class GlobalManager:
    def __init__(self):
        self.log=logger()

    #删除旧结果集
    def delet_report(self):
        self.log.info('删除旧的报告')
        if os.path.exists(REPORT_PATH):
            shutil.rmtree(REPORT_PATH)

    #删除截图目录
    def delete_screen(self):
        self.log.info('删除旧的截图')
        if os.path.exists(SCREENSHOT_DIR):
            shutil.rmtree(SCREENSHOT_DIR)
    #删除日志目录
    def delete_log(self):
        if os.path.exists(LOG_FOLDER):
            shutil.rmtree(LOG_FOLDER)


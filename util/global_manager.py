#coding=utf-8
__author__ = 'tangyao'

import os
import shutil

from config.log_config import logger
from config.global_config import REPORT_RESULT_PATH, SCREENSHOT_DIR, REPORT_PATH


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


#coding=utf-8
__author__ = 'tangyao'

import os

from config.log_config import logger
from config.global_config import REPORT_RESULT_PATH, SCREENSHOT_DIR


class GlobalManager:
    def __init__(self):
        self.log=logger()

    #删除旧结果集
    def delet_report(self):
        self.log.info('删除旧的报告')
        if not os.path.exists(REPORT_RESULT_PATH):
            os.rmdir(REPORT_RESULT_PATH)
    #删除截图目录
    def delete_screen(self):
        self.log.info('删除旧的截图')
        if not os.path.exists(SCREENSHOT_DIR):
            os.rmdir(SCREENSHOT_DIR)

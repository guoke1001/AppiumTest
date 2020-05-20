#coding=utf-8
__author__ = 'tangyao'

import os
import time

#项目路径
from datetime import datetime

project_path=os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]),'.'))

# ---------------- 日志相关 --------------------
# 日志级别
LOG_LEVEL = 'debug'
LOG_STREAM_LEVEL = 'debug'  # 屏幕输出流
LOG_FILE_LEVEL = 'info'   # 文件输出流
# 日志命名
LOG_FOLDER = os.path.join(project_path, 'logs')
LOG_FILE_NAME = os.path.join(LOG_FOLDER, datetime.now().strftime('%Y-%m-%d') + '.log')
# ---------------- 截图相关 --------------------
SCREENSHOT_DIR = os.path.join(project_path, "screenshot")
# ---------------- 压缩文件相关 --------------------
ZIP_DIR=os.path.join(project_path,"report","zip")
ZIP_File_DIR=os.path.join(project_path,"report")

# ---------------- 测试报告 --------------------
REPORT_PATH = os.path.join(project_path, "report")
REPORT_RESULT_PATH = os.path.join(REPORT_PATH, "allure_result")
REPORT_END_PATH = os.path.join(REPORT_PATH, "allure_report")
REPORT_HISTORY_PATH = os.path.join(REPORT_PATH, "allure_report", "history")

# ---------------- 隐式等待时间 --------------------
IMPLICITLY_WAIT_TIME = 5

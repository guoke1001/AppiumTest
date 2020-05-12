#coding=utf-8
__author__ = 'tangyao'

import os
import time

#项目路径
project_path=os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]),'.'))
#测试用例路径
test_case_path=project_path+"/test_case"
#测试报告路径
report_path=project_path+'/report_path'
#测试报告名称
report_name=report_path+time.strptime('%Y%m%d%h%s',time.localtime())

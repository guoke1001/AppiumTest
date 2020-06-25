#coding=utf-8
__author__ = 'tangyao'


import pytest

from config.log_config import logger
from config.driver_config import DriverConfig

log=logger()
base_driver=None

def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default="device", help="None")

def pytest_collection_modifyitems(config,items):
    """
      1、测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    所有的测试用例收集完毕后调用, 可以再次过滤或者对它们重新排序
    items （收集的测试项目列表）
      2、config.getoption("--cmdopt")获取命令行传递过来的参数
      3、config.getoption获取传递过来的设备信息，再添加到nodeid，这样针对每个设备都会生成一条用例
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")+" : "+eval(config.getoption("--cmdopt"))["deviceName"]

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")

@pytest.fixture
def common_driver(cmdopt):
    print(111111111111111111,eval(cmdopt))
    global base_driver
    global device
    if base_driver==None:
        base_driver=DriverConfig(eval(cmdopt))
    driver=base_driver.get_driver()
    yield driver
    driver.close_app()
    driver.quit()

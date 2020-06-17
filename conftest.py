#coding=utf-8
__author__ = 'tangyao'


import pytest

from config.log_config import logger
from config.driver_config import DriverConfig

log=logger()
base_driver=None

def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default="device", help="None")

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")

@pytest.fixture
def common_driver(cmdopt):
    global base_driver
    if base_driver==None:
        base_driver=DriverConfig(eval(cmdopt))
    driver=base_driver.get_driver()
    yield driver
    driver.close_app()
    driver.quit()



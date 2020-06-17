#coding=utf-8
__author__ = 'tangyao'

from appium.webdriver.webdriver import WebDriver

from common.base_page import BasePage

'''
description:手势操作
'''
class gesture_mainpulation(BasePage):
    def __init__(self):
        self.x = self.driver.get_window_size()['width']
        self.y = self.driver.get_window_size()['height']
    def swipe_left(self):
        '''左滑屏幕'''

        self.driver.swipe(self.x*0.8,self.y/2,self.x/2,self.y*0.1)

    def swipe_right(self):
        '''右滑屏幕'''

        self.driver.swipe(self.x*0.1,self.y/2,self.x*0.8,self.y/2)

    def swipe_down(self):
        '''下滑屏幕'''

        self.driver.swipe(self.x/2,self.y*0.1,self.x/2,self.y*0.8,500)


    def swipe_up(self):
        '''上滑屏幕'''
        self.driver.swipe(self.x/2,self.y*0.9,self.x/2,self.y*0.2,500)

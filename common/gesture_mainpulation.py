#coding=utf-8
__author__ = 'tangyao'

from appium.webdriver.webdriver import WebDriver

'''
description:手势操作
'''
class gesture_mainpulation:
    def __init__(self,driver:WebDriver):
        self.driver=driver
        self.x = self.driver.get_window_size()['width']
        self.y = self.driver.get_window_size()['height']
    def swipe_left(self):
        '''左滑'''

        self.driver.swipe(self.x*3/4,self.y/4,self.x/4,self.y/4)

    def swipe_right(self):
        '''右滑'''

        self.driver.swipe(self.x/4,self.y/4,self.x*3/4,self.y/4)

    def swipe_down(self):
        '''下滑'''

        self.driver.swipe(self.x/2,self.y*3/5,self.x/2,self.y/5)


    def swipe_up(self):
        '''上滑'''
        self.driver.swipe(self.x/2,self.y/4,self.x/2,self.y*3/4)

#!/usr/bin/python  
#-*-coding:utf-8-*-
#userbiubiubiu
from appium import webdriver
from time import sleep

class App_config(object):

     def app(slef,abcd):
          abcd.find_elements_by_id('com.tencent.mm:id/iq')[0].click()
          sleep(2)
          abcd.find_element_by_id('com.tencent.mm:id/kh').send_keys('优酷视频')
          sleep(2)
          abcd.find_element_by_id('com.tencent.mm:id/px').click()
          sleep(2)
          abcd.find_elements_by_class_name('android.widget.RelativeLayout')[2].click()()
          sleep(2)
          abcd.find_element_by_class_name('android.widget.Image').click()
          sleep(2)
          abcd.find_elements_by_class_name('android.widget.Button')[1].click()
          sleep(2)




#!/usr/bin/python  
#-*-coding:utf-8-*-
#userbiubiubiu
import unittest
from appium import webdriver
from time import sleep
from 框架.config.APP_config import App_config
from 框架.data.diandan_data import Diandan_data
class App_test(unittest.TestCase):
    shuju=Diandan_data().diandan_shuju()
    def setUp(self):

        abc = {'platformName': 'Android',
               # 'platformVersion':'5.0',
               'deviceName': '127.0.0.0:',
               'appPackage': 'com.tencent.mm',
               'appActivity': '.ui.LauncherUI'  # 获取Activity 1.monkey 找到cmp=  2.从日志中查找 cmp=com.netease.cloudmusic
               }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', abc)
        sleep(2)
        self.driver.find_element_by_id('com.tencent.mm:id/e4g').click()
        sleep(2)
        self.driver.find_element_by_id('com.tencent.mm:id/cou').click()
        sleep(2)
        self.driver.find_elements_by_id('com.tencent.mm:id/kh')[0].send_keys('275445403')
        sleep(2)
        self.driver.find_elements_by_id('com.tencent.mm:id/kh')[1].send_keys('fei19961224...')
        sleep(2)
        self.driver.find_element_by_id('com.tencent.mm:id/cov').click()
        sleep(30)
        self.driver.find_elements_by_class_name('android.widget.Button')[0].click()
        sleep(50)
        App_config().app(self.driver)

#     def test_1(self):
#
#         App_config().app(self.driver,self.shuju[0][0],self.shuju[0][1])
#         neirong=self.driver.find_element_by_id('asdsadasada').text()
#         self.assertEqual(neirong,'Sky')
#
#     def tearDown(self):
#          self.driver.quit()
# if __name__=='__main__':
#     unittest.main()
a=App_test()
a.setUp()
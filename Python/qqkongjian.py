#!/usr/bin/python  
#-*-coding:utf-8-*-
#userbiubiubiu
import xlrd
shuju=[]
f=xlrd.open_workbook('1.xls')
sheet=f.sheets()[0]
num=sheet.nrows
for i in range(num):
    if i == 0:
        continue
    else:
        shuju.append(sheet.row_values(i))

import unittest
from selenium import webdriver
from time import sleep
import HTMLTestRunner
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from ddt import ddt,data,unpack
class QQkongjian(unittest.TestCase):

    def setup(self,u,p):
        global dr
        dr = webdriver.Chrome()
        dr.get('https://www.qzone.qq.com')
        sleep(2)

        dr.switch_to.frame('login_frame')
        sleep(2)

        dr.find_element_by_id('switcher_plogin').click()
        sleep(2)

        dr.find_element_by_id('u').send_keys('{}'.format(u))
        sleep(2)

        dr.find_element_by_id('p').send_keys('{}'.format(p))
        sleep(2)

        dr.find_element_by_id('login_button').click()
        sleep(2)
        abcd=dr.title
        return abcd

    def test_1(self):
        abc=QQkongjian().setup(int(shuju[0][0]),shuju[0][1])
        self.assertEqual(abc,'寻情妹的空间 [http://819787014.qzone.qq.com]')
    def test_2(self):
        abc=QQkongjian().setup(int(shuju[1][0]),shuju[1][1])
        self.assertEqual(abc,'QQ空间-分享生活，留住感动')
    def test_3(self):
        abc=QQkongjian().setup(int(shuju[2][0]),shuju[2][1])
        self.assertEqual(abc,'QQ空间-分享生活，留住感动')

    def baobiao(self):
        suit = unittest.TestSuite()
        suit.addTest(QQkongjian('test_1'))
        f = open('abc.html', 'wb', )
        biaoti=HTMLTestRunner.HTMLTestRunner(stream=f,title='索赔测试报告',tester='吴彦祖',description='结果如下')
        biaoti.run(suit)
        f.close()
    def tearDown(self):
        dr.quit()
if  __name__=="__main__":
    unittest.main()

#cldrag_and_drop(1.起始位置，结束位置)
#drag_and_drop_by_offset(起始位置，x轴坐标，y轴坐标)
# start = dr.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[1]/div[1]')
# ActionChains(dr).drag_and_drop_by_offset(start,60,0).perform()
# sleep(2)

# dr.find_element_by_css_selector('#aIcenter > span').click()
# sleep(2)
# dr.find_element_by_css_selector('#fct_1753038958_311_0_1554364786_0_1 > div.f-single-foot > div.f-op-detail.f-detail.content-line > p > a.item.qz_like_btn_v3 > i').click()

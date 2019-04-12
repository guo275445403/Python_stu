#!/usr/bin/python  
#-*-coding:utf-8-*-
#userbiubiubiu
# import requests
# import json
# url = "https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData"
#
# # body = "{\r\t\"method\": \"getOrderQueryList\",\r\t\"queryMethod\": \"全部\",\r\t\"code\": \"\",\r\t\"queryDate\": \"\",\r\t\"queryEndDate\": \"\",\r\t\"orderStatus\": \"未签收\",\r\t\"orderPriority\": \"全部\",\r\t\"orderException\": \"全部\",\r\t\"status\": \"全部\",\r\t\"pageSize\": 10,\r\t\"curPage\": 1\r}"
# head = {
#     'Content-Type': "application/json",
#     'x-dealer-code': "2100150",
#     'x-position-code': "D_PO_1028",
#     'x-resource-code': "BASIC_DATA",
#     'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
#     'x-user-code': "djy0mx",
#     'x-access-token': "0da5606a534fa727dfd7f502df38be65",
#     # 'cache-control': "no-cache",
#     # 'Postman-Token': "da05ee37e5676e7b27972b2892e0fdeb"
#     }
# body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode('utf-8')
#
# res=requests.post(url=url,headers=head,data=body)
# mes=res.json()
# assert (mes["data"]["applicationType"][0]["name"]) =="多装"
import unittest,requests,time
import HTMLTestRunner  #产生测试报告的模块

#
# def yonglia():
#     url = "https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData"
#     head = {
#         'Content-Type': "application/json",
#         'x-dealer-code': "2100150",
#         'x-position-code': "D_PO_1028",
#         'x-resource-code': "BASIC_DATA",
#         'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
#         'x-user-code': "djy0mx",
#         'x-access-token': "0da5606a534fa727dfd7f502df38be65",
#         # 'cache-control': "no-cache",
#         # 'Postman-Token': "da05ee37e5676e7b27972b2892e0fdeb"
#     }
#     body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode(
#         'utf-8')
#     res = requests.post(url=url, headers=head, data=body)
#     mes = res.json()
#     return mes
# msg=yonglia()

# class Suopezi(unittest.TestCase):
#     def test2(self):
#         url = "https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData"
#         head = {
#             'Content-Type': "application/json",
#             'x-dealer-code': "2100150",
#             'x-position-code': "D_PO_1028",
#             'x-resource-code': "BASIC_DATA",
#             'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
#             'x-user-code': "djy0mx",
#             'x-access-token': "0da5606a534fa727dfd7f502df38be65",
#             # 'cache-control': "no-cache",
#             # 'Postman-Token': "da05ee37e5676e7b27972b2892e0fdeb"
#         }
#         body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": "qwe","curPage": 1}'.encode(
#             'utf-8')
#         res = requests.post(url=url, headers=head, data=body)
#         mes = res.json()
#         self.assertNotEqual((mes["data"]["applicationType"][0]["name"]),"装")
#     def test3(self):
#         url = "https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData"
#         head = {
#             'Content-Type': "application/json",
#             'x-dealer-code': "2100150",
#             'x-position-code': "D_PO_1028",
#             'x-resource-code': "BASIC_DATA",
#             'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
#             'x-user-code': "djy0mx",
#             'x-access-token': "0da5606a534fa727dfd7f502df38be65",
#             # 'cache-control': "no-cache",
#             # 'Postman-Token': "da05ee37e5676e7b27972b2892e0fdeb"
#         }
#         body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": {},"curPage": 1}'.encode(
#             'utf-8')
#         res = requests.post(url=url, headers=head, data=body)
#         mes = res.json()
#         self.assertIn(mes["data"]["applicationType"][0]["name"],["多","装"])
#     def test4(self):
#         self.assertNotEqual(132,456)
# if  __name__=="__main__":
#     #创建一个测试套件
#     suit = unittest.TestSuite()
#     #添加测试用例
#     for i in range(1,5):
#         suit.addTest(Suopei('test{}'.format(i)))
#     shijian=time.strftime('%Y-%m-%d %H:%M:%S',time.locaime(time.time()))
#     f=open('abc.html','wb',)
#     #定义测试报告内容
#     biaoti=HTMLTestRunner.HTMLTestRunner(stream=f,title='索赔测试报告',tester='吴彦祖',description='结果如下')
#     biaoti.run(suit)
#     f.close()
#setup 在每次用例执行之前先执行一次，作用：初始化测试环境
# #teardown 在每次用例执行之后再执行一次


#Web自动化测试
# 环境搭建
# 1.安装python`
# 2.安装selenium模块
# 3.下载浏览器驱动
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
#定义浏览器
# dr=webdriver.Chrome()

# #设置网页大小 set_window_size
# dr.set_window_size(400,500)

# #设置浏览器位置 set_window_position
# dr.set_window_position(300,100)

#设置浏览器最大化
# dr.maximize_window()

#最小化
# dr.minimize_window()

#打开网址
# dr.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
# sleep(2)

#定位  核心
#1.通过标签中的id属性定位
# dr.find_element_by_id('kw').send_keys('DNF')
# sleep(3)
# dr.find_element_by_id('su').click()
# sleep(2)

#2.通过标签中的class属性定位
# dr.find_element_by_class_name("favurl").click()
# sleep(2)
# dr.back()
#3.通过标签中的name属性定位
# dr.find_element_by_name('tj_trtieba').click()

#4.通过标签中的文本属性定位
# dr.find_element_by_link_text('hao123').click()

#5.通过标签中的模糊文本属性定位
# dr.find_element_by_partial_link_text('新').click()

#6.通过标签的名称来定位定位，通常用来定位一组数据
# dr.find_elements_by_tag_name('标签名称')

#7.通过css来定位
# dr.find_element_by_css_selector('#kw')

#8.xpath定位，路径定位  xpath(路径标记语言） xml（可扩展性标记语言）
# dr.find_element_by_xpath('//*[@id="kw"]')

# 定位一组数据 需要同时对多个数据进行操作
# wd = dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_tag_name('option')
# 层级定位 遇到复杂的元素定位时
# for i in wd:
        # i.click()
        # sleep(2)
#处理框架  iframe窗口(框架id属性，name属性，定位到框架)
# dr.switch_to.frame('login_frame') #切换到某一个框架
# dr.switch_to.default_content()    #切换到最初的页面
# dr.switch_to.parent_frame()#会到父框架页面


#获取网址标题
# print(dr.title)
# #获取网页的网址
# print(dr.current_url)

# dr.get('https://www.4399.com')
# sleep(2)
# #回退 back
# dr.back()
# sleep(2)
# #前进 forward
# dr.forward()
# sleep(2)

#模拟动作
# click() 点击  send_keys() 输入
# text 获取定位到的元素的文本
# clear() 清空定位到的元素上面的数据

#关闭浏览器 并断开连接quit   关闭浏览器，不断开连接 close
# dr.quit()

#处理浏览器窗口，
# dr.current_window_handle()  #获取当前窗口的句柄(字符串)
# print(dr.window_handles)       #获取所有窗口的句柄(字符串)
# dr.switch_to.window(qq[-1]) #切换窗口
# print(dr.title)

import selenium.webdriver.support.ui as ui
#对鼠标的操作
dr=webdriver.Chrome()
dr.maximize_window()
dr.get('https://www.jd.com')
sleep(2)


#智能等待，设置一个最大等待时间，检测某个元素出现，就不会继续等待
# wait = ui.WebDriverWait(dr, 10)
#出现定位元素，就不等待
# wait.until(lambda dr: dr.find_element_by_xpath('//*[@id="J_rec"]/div/div[3]/a/div/img').is_displayed())
# print('hello')
#获取定位到的元素某个属性的值
w=dr.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]')
a=w.get_attribute('href')
print(a)

# w=dr.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_tag_name('li')
# for i in w:
#     #控制鼠标来移动到元素的位置上
#     ActionChains(dr).move_to_element(i).perform()#执行
#     sleep(2)
#切换到弹出框
# ww=dr.switch_to.alert
# print(ww.text)
#点击弹出框上的确定
# ww.accpet()
#点击取消
# w.dismiss()
# 输入
# w.send_keys('输入内容')

#处理页面滚动条
# for i in range(1,10000,500):
#     js='var q=document.documentElement.scrollTop={}'.format(i)
# 执行JavaScript语句
#     dr.execute_script(js)
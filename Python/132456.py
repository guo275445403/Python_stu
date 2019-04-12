#!/usr/bin/python  
#-*-coding:utf-8-*-
#userbiubiubiu
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
dr=webdriver.Chrome()
dr.get('https://www.jd.com/')
sleep(2)
# dr.find_element_by_id('kw').send_keys('jd')
# sleep(2)
# dr.find_element_by_id('su').click()
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[3]/div[1]/div/div/div[1]/div/div[1]/div/h2/a[1]').click()
# qq = dr.window_handles
# print(qq)
# dr.switch_to.window(qq[-1])
# sleep(2)
dr.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="loginname"]').send_keys('18348326189')
sleep(2)
dr.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys('fei19961224')
sleep(2)
dr.find_element_by_xpath('//*[@id="loginsubmit"]').click()
sleep(2)
start = dr.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[1]/div[1]')

ActionChains(dr).drag_and_drop_by_offset(start,80,0).perform()


dr.find_element_by_xpath('//*[@id="J_seckill"]/div/div[2]/div[1]/div/div/div/div[5]/a/div[1]/img').click()
sleep(2)
start = dr.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[1]/div[1]')
ActionChains(dr).drag_and_drop_by_offset(start,60,0).perform()
sleep(2)
dr.find_element_by_xpath('//*[@id="J_cate"]/ul/li[2]/a[1]').click()
sleep(2)
qqq=dr.window_handles
dr.switch_to.window(qqq[-1])
dr.find_element_by_xpath('/html/body/div[4]/div[5]/div/div[2]/div[2]/ul[1]/li[1]/a[1]/img').click()
sleep(2)
qqq=dr.window_handles
dr.switch_to.window(qqq[-1])
dr.find_element_by_xpath('//*[@id="InitCartUrl"]').click()
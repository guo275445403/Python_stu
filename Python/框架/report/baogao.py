#!/usr/bin/python  
#-*-coding:utf-8-*-
#userbiubiubiu
from 框架.report import HTMLTestRunner
import unittest

def baogao(aa):
    suit=unittest.TestSuite()
    # suit.addTest(unittest.makeSuite(Suopei_test)) #
    #参数1存放用例的文件夹路径 参数2 正则匹配内容,自动找匹配的文件，并且找到文件中以test开头的用例
    for j in aa:
        dis = unittest.defaultTestLoader.discover(r'E:\Python\框架\test', pattern='{}_test.py'.format(j.strip()))
        for i in dis:
            suit.addTest(i)
    f=open(r'E:\Python\框架\report\aa.html','wb')
    runner=HTMLTestRunner.HTMLTestRunner(title='索赔测试报告',stream=f,description='结果如下',tester='吴彦祖')
    runner.run(suit)
    f.close()
if __name__=='__main__':
    pass
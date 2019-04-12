#!/usr/bin/python  
#-*-coding:utf-8-*-
#userbiubiubiu
import unittest,requests
from 框架.config.suopei import Suopei
from 框架.data.suopei_data import Suopei_duqu

class Suopei_test(unittest.TestCase):
    shuju= Suopei_duqu().duqu_shuju()

    def test_1(self):
        suo=Suopei().jichushuju(int(self.shuju[0][0]),int(self.shuju[0][1]))
        self.assertEqual(suo['data']['applicationType'][0]['name'],'多装')
    def test_2(self):
        suo = Suopei().jichushuju(self.shuju[1][0], int(self.shuju[1][1]))
        self.assertNotIn(suo['message'], '多装')
    def test_3(self):
        suo = Suopei().jichushuju(int(self.shuju[2][0]), self.shuju[2][1])
        self.assertNotEqual(suo['message'],'多装')

class shouyezhuangtai(unittest.TestCase):

    def test_4(self):
        suo=Suopei().shouyezhuangtai()
        self.assertEqual(suo['status'],1)
if __name__=='__main__':
    unittest.main()
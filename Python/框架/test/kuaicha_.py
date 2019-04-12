#!/usr/bin/python
#-*-coding:utf-8-*-
#userbiubiubiu
from 框架.data.kuaicha_data  import Kuaicha_data
from 框架.config.suopei import Kuaicha_config
import unittest
class Kuaicha_test(unittest.TestCase):
    shuju=Kuaicha_data().duqu_kuaicha()

    def test_1(self):
        cha=Kuaicha_config().xuexiao(self.shuju[1])
        self.assertEqual(cha['code'], 0)
    def test_2(self):
        cha = Kuaicha_config().xuexiao(self.shuju[2])
        self.assertEqual(cha['msg'],'学校快查成功')
    def test_3(self):
        cha = Kuaicha_config().xuexiao(self.shuju[3])
        self.assertNotEqual(cha['data'][0]["schoolName"],'123')

if __name__ == '__main__':
    unittest.main()
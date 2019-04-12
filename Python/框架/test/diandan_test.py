#!/usr/bin/python  
#-*-coding:utf-8-*-
#userbiubiubiu
import unittest
from 框架.config.dingdan_config import Diandan_config
from 框架.data.diandan_data import Diandan_data

class Dingdan_test(unittest.TestCase):
    shuju = Diandan_data().diandan_shuju()

    def test_zhuangtai_1(self):
        neirong=Diandan_config().zhuangtai()
        self.assertEqual(neirong['status'], 1)
    def test_liebiao_1(self):
        canshu=Diandan_config().liebiao(int(self.shuju[0][0]), int(self.shuju[0][1]))
        self.assertEqual(canshu['status'],1)
    def test_dingdanmingxi_1(self):
        canshu =Diandan_config().dingdanmingxi(int(self.shuju[0][2]),int(self.shuju[0][3]))
        self.assertEqual(canshu['status'], 1)
    def test_peijian_1(self):
        canshu = Diandan_config().peijian(self.shuju[0][4])
        self.assertEqual(canshu['status'], 1)
    def test_tiaobodan_1(self):
        canshu = Diandan_config().tiaobodan(self.shuju[0][5])
        self.assertEqual(canshu['status'], 1)


    def test_zhuangtai_2(self):
        neirong = Diandan_config().zhuangtai()
        self.assertEqual(neirong['status'], 1)

    def test_liebiao_2(self):
        canshu = Diandan_config().liebiao(self.shuju[1][0], self.shuju[1][1])
        self.assertEqual(canshu['message'], "get error")

    def test_dingdanmingxi_2(self):
        canshu = Diandan_config().dingdanmingxi(self.shuju[1][2], self.shuju[1][3])
        self.assertEqual(canshu['message'], "get error")

    def test_peijian_2(self):
        canshu = Diandan_config().peijian(self.shuju[1][4])
        self.assertEqual(canshu['message'], "get error")

    def test_tiaobodan_2(self):
        canshu = Diandan_config().tiaobodan(self.shuju[1][5])
        self.assertEqual(canshu['message'], "get error")


    def test_zhuangtai_3(self):
        neirong = Diandan_config().zhuangtai()
        self.assertEqual(neirong['status'], 1)

    def test_liebiao_3(self):
        canshu = Diandan_config().liebiao(self.shuju[2][0], self.shuju[2][1])
        self.assertEqual(canshu['message'], "get error")

    def test_dingdanmingxi_3(self):
        canshu = Diandan_config().dingdanmingxi(self.shuju[2][2], self.shuju[2][3])
        self.assertEqual(canshu['message'], "get error")

    def test_peijian_3(self):
        canshu = Diandan_config().peijian(self.shuju[2][4])
        self.assertEqual(canshu['message'], "get error")

    def test_tiaobodan_3(self):
        canshu = Diandan_config().tiaobodan(self.shuju[2][5])
        self.assertEqual(canshu['message'], "get error")



    def test_zhuangtai_4(self):
        neirong = Diandan_config().zhuangtai()
        self.assertEqual(neirong['status'], 1)

    def test_liebiao_4(self):
        canshu = Diandan_config().liebiao(self.shuju[3][0], self.shuju[3][1])
        self.assertEqual(canshu['message'], "get error")

    def test_dingdanmingxi_4(self):
        canshu = Diandan_config().dingdanmingxi(self.shuju[3][2], self.shuju[3][3])
        self.assertEqual(canshu['message'], "get error")

    def test_peijian_4(self):
        canshu = Diandan_config().peijian(self.shuju[3][4])
        self.assertEqual(canshu['message'], "get error")

    def test_tiaobodan_4(self):
        canshu = Diandan_config().tiaobodan(self.shuju[3][5])
        self.assertEqual(canshu['message'], "get error")


    def test_zhuangtai_5(self):
        neirong = Diandan_config().zhuangtai()
        self.assertEqual(neirong['status'], 1)

    def test_liebiao_5(self):
        canshu = Diandan_config().liebiao(self.shuju[4][0], self.shuju[4][1])
        self.assertEqual(canshu['message'], "get error")

    def test_dingdanmingxi_5(self):
        canshu = Diandan_config().dingdanmingxi(self.shuju[4][2], self.shuju[4][3])
        self.assertEqual(canshu['message'], "get error")

    def test_peijian_5(self):
        canshu = Diandan_config().peijian(self.shuju[4][4])
        self.assertEqual(canshu['message'], "get error")

    def test_tiaobodan_5(self):
        canshu = Diandan_config().tiaobodan(self.shuju[4][5])
        self.assertEqual(canshu['message'], "get error")

if __name__=='__main__':
    unittest.main()

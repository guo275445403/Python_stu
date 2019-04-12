#!/usr/bin/python  
#-*-coding:utf-8-*-
#userbiubiubiu
import unittest,requests,time
import HTMLTestRunner  #产生测试报告的模块


def yonglia():
    url = "https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData"
    head = {
        'Content-Type': "application/json",
        'x-dealer-code': "2100150",
        'x-position-code': "D_PO_1028",
        'x-resource-code': "BASIC_DATA",
        'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
        'x-user-code': "djy0mx",
        'x-access-token': "0da5606a534fa727dfd7f502df38be65",
        # 'cache-control': "no-cache",
        # 'Postman-Token': "da05ee37e5676e7b27972b2892e0fdeb"
    }
    body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode(
        'utf-8')
    res = requests.post(url=url, headers=head, data=body)
    mes = res.json()
    return mes
msg=yonglia()

class Suopei(unittest.TestCase):
    def test_1(self):
        self.assertEqual(msg['data']["applicationType"][0]["name"],"装")
    def test2(self):
        self.assertNotEqual(msg['data']["applicationType"][0]["name"],"多装")
    def test3(self):
        pass
    def test4(self):
        pass
if  __name__=="__main__":
    suit = unittest.TestSuite()
    for i in range(1,5):
         suit.addTest(Suopei('test{}'.format(i)))
    shijian=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    f=open('abcd.html','wb',)
    biaoti=HTMLTestRunner.HTMLTestRunner(stream=f,title='索赔测试报告',tester='吴彦祖',description='结果如下')
    biaoti.run(suit)
    f.close()
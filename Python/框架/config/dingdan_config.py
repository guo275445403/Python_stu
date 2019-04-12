#!/usr/bin/python  
#-*-coding:utf-8-*-
#userbiubiubiu
import requests
class Diandan_config(object):

    def zhuangtai(self):
        url='https://mobileqa.dms.saic-gm.com/api/dev/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderHomePage'

        head={
    'Content-Type': "application/json",
    'x-dealer-code': "2100005",
    'x-position-code': "D_PO_1028",
    'x-resource-code': "pol4s_partOrder_orderHomePage",
    'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
    'x-user-code': "dhxc1u",
    'x-access-token': "0da5606a534fa727dfd7f502df38be65",
    'cache-control': "no-cache",
    'Postman-Token': "e2d81122-6e4d-4ac2-b987-40938088d0d3"
    }
        res=requests.post(url,headers=head)
        msg=res.json()
        return msg
    def liebiao(self,a,aa):
        url='https://mobileqa.dms.saic-gm.com/api/dev/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderList'

        head={ 'Content-Type': "application/json",
    'x-dealer-code': "2100001",
    'x-position-code': "D_PO_1028",
    'x-resource-code': "pol4s_partOrder_orderList",
    'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
    'x-user-code': "dhxc1u",
    'x-access-token': "da05ee37e5676e7b27972b2892e0fdeb",
    'cache-control': "no-cache",
    'Postman-Token': "c02ebfff-bb56-4cbe-9af6-dbc5b07bcbd0"}

        body='{"pageNum":%s,"pageSize": %s,"queryTerms": {"orderType": "","orderStatus": "","orderDelayFlag": "","orderNo": "","startReportDate": "","endReportDate": ""}}' % (a,aa)

        res=requests.post(url,headers=head,data=body)
        msg=res.json()
        return msg

    def dingdanmingxi(self,b,bb):
        url='https://mobileqa.dms.saic-gm.com/api/dev/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderHomePage'

        head={   'Content-Type': "application/json",
    'x-dealer-code': "2100005",
    'x-position-code': "D_PO_1028",
    'x-resource-code': "pol4s_partOrder_orderHomePage",
    'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
    'x-user-code': "dhxc1u",
    'x-access-token': "da05ee37e5676e7b27972b2892e0fdeb",
    'cache-control': "no-cache",
    'Postman-Token': "b12c7859-2cdc-4d08-9259-acebb7d1679b"}
        body='{"pageNum":%s,"pgeSize":%s,"queryTerms":{ "orderNo":3108}}' % (b,bb)
        res=requests.post(url,headers=head,data=body)
        msg=res.json()
        return msg
    def peijian(self,c):
        url='https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrderSearch/partOrderDetailSearch'

        head={    'Content-Type': "application/json",
    'x-dealer-code': "2100005",
    'x-position-code': "D_PO_1028",
    'x-resource-code': "pol4s_partOrderSearch_partOrderDetailSearch",
    'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
    'x-user-code': "dhxc1u",
    'x-access-token': "0da5606a534fa727dfd7f502df38be65",
    'cache-control': "no-cache",
    'Postman-Token': "11f72edd-3ab0-442a-94e5-6719e1819708"}

        body='{"pageNum":"1","pgeSize":"10","queryTerms":{"orderNo":%s}}'%(c)
        res=requests.post(url,headers=head,data=body)
        msg=res.json()
        return msg
    def tiaobodan(self,d):
        url='https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/orderManage/list'

        head={    'Content-Type': "application/json",
    'x-dealer-code': "2100001",
    'x-position-code': "D_PO_1028",
    'x-resource-code': "pol4s_orderManage_list",
    'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
    'x-user-code': "dhxc1u",
    'x-access-token': "da05ee37e5676e7b27972b2892e0fdeb",
    'cache-control': "no-cache",
    'Postman-Token': "a3f69aba-4b2e-4f65-83c2-5f77ef75aa9f"}

        body='{"queryTerms":{"partCode":%s,"partName":"","vehicleModel":"-1","dimsPartType":"-1","ugentLevel":"1","isCanSunPack":"-1","isTransfer":"-1","isDelay":"-1","isEffective":"-1","isDimsRecommend":"-1","orderNo":"","cancelStatus":"-1"},"pageNum":""}'%(d)

        res=requests.post(url,headers=head,data=body)
        msg=res.json()
        return msg
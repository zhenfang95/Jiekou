#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/10/24 14:56

import unittest,json
from base.method import *
from common import readExcel
from page.xiaoe import *

class TestServerBuy(unittest.TestCase):
    '''服务订购支付下单'''
    def setUp(self):
        self.obj = Method()
        self.asser = IsContent()
        self.excel = readExcel.OperationExcel()

    def requesData(self,row):
        return self.excel.getRequestData(row)

    def isContent(self, r, row):
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 0)
        self.assertTrue(self.asser.isContent(row=row, str1=r.text))

    def isContent_a(self, r):
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 16)
        self.assertEqual(r.json()['msg'],'存在待支付订单 ~')

    def test_001(self):
        '''创建B端版本服务支付订单'''
        r = self.obj.method(3,data=self.requesData(3),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        if r.json()['code'] == 0:
            self.isContent(r,3)
            writeDataYaml(key1='serverOrder_id1',vlue1=r.json()['data']['order_id'])
        else:
            self.isContent_a(r)
            writeDataYaml(key1='serverOrder_id1',vlue1=r.json()['data']['order_id'])

    def test_002(self):
        '''H5购买店铺版本调起支付'''
        dict1 = json.loads(self.requesData(4))  #json反序列化
        dict1['order_id'] = getserverOrderId1()
        r = self.obj.get(4,params=dict1,headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,4)

    def test_003(self):
        '''取消店铺版本服务订购订单'''
        dict1 = json.loads(self.requesData(5))
        dict1['order_id'] = getserverOrderId1()
        r = self.obj.post(5,data=dict1,headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,5)

    def test_004(self):
        '''创建B端增值服务支付订单'''
        r = self.obj.method(6,data=self.requesData(6),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        if r.json()['code'] == 0:
            self.isContent(r,6)
            writeDataYaml(key1='serverOrder_id2',vlue1=r.json()['data']['order_id'])
        else:
            self.isContent_a(r)
            writeDataYaml(key1='serverOrder_id2',vlue1=r.json()['data']['order_id'])

    def test_005(self):
        '''H5购买增值服务调起支付'''
        dict1 = json.loads(self.requesData(7))
        dict1['order_id'] = getserverOrderId2()
        r = self.obj.get(7,params=dict1,headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,7)

    def test_006(self):
        '''取消功能服务订购订单'''
        dict1 = json.loads(self.requesData(8))
        dict1['order_id'] = getserverOrderId2()
        r = self.obj.post(8,data=dict1,headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,8)

if __name__ == "__main__":
    unittest.main(verbosity=2)
#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/12/27 14:15

import unittest
import re
import requests
from common import readExcel
from base.method import *
from page.xiaoe import *

class TestWXB_App(unittest.TestCase):
    '''吴晓波APP支付下单'''
    def setUp(self):
        self.excel = readExcel.OperationExcel()
        self.obj = Method()
        self.asser = IsContent()

    def requesData(self,row):
        return self.excel.getRequestData(row)

    def isContent(self,r,row):
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 0)
        self.assertTrue(self.asser.isContent(row=row,str1=r.text))

    def test_001(self):
        '''进入波豆余额页'''
        r = self.obj.post(301,data=setWXZapp_01(301),headers=getHeaderWXB_App())
        mylog.info('result：%s' % r.json())
        self.isContent(r,301)

    def test_002(self):
        '''获取可充值金额列表'''
        for i in range(6):
            r = self.obj.post(302,data=setWXZapp_01(302),headers=getHeaderWXB_App())
            mylog.info('result：%s' % r.json())
            self.isContent(r,302)
            writeDataYaml(key1='product_id'+str(i),vlue1=r.json()['data'][i]['product_id'])
            writeDataYaml(key1='balance',vlue1=r.json()['data'][i]['balance'])
            writeDataYaml(key1='price',vlue1=r.json()['data'][i]['price'])

    def test_003(self):
        '''波豆预支付下单'''
        for i in range(6):
            dict1 = setWXZapp_02()
            dict1['product_id'] = getRead(key1='product_id'+str(i))
            dict2=json.dumps(dict1)
            r = self.obj.post(303,data=dict2,headers=getHeaderWXB_App())
            mylog.info('result：%s' % r.json())
            self.isContent(r,303)
            writeDataYaml(key1='APP_order_id'+str(i),vlue1=r.json()['data']['order_id'])

    def test_004(self):
        '''波豆微信支付下单'''
        for i in range(6):
            dict1 = setWXZapp_03(304)
            dict1['pre_order_id'] = getRead(key1='APP_order_id'+str(i))
            dict2=json.dumps(dict1)
            r = self.obj.post(304,data=dict2,headers=getHeaderWXB_App())
            mylog.info('result：%s' % r.json())
            self.isContent(r,304)

    def test_005(self):
        '''波豆支付宝支付下单'''
        for i in range(6):
            dict1 = setWXZapp_03(305)
            dict1['pre_order_id'] = getRead(key1='APP_order_id'+str(i))
            dict2=json.dumps(dict1)
            r = self.obj.post(305,data=dict2,headers=getHeaderWXB_App())
            mylog.info('result：%s' % r.json())
            self.isContent(r,305)

    def test_006(self):
        '''进入开通超级会员页'''
        r = self.obj.post(306,data=setWXZapp_01(306),headers=getHeaderWXB_App())
        mylog.info('result：%s' % r.json())
        self.isContent(r,306)
        writeDataYaml(key1='APP_svip_id',vlue1=r.json()['data']['svip_id'])
        writeDataYaml(key1='APP_resource_id',vlue1=r.json()['data']['resource_id'])
        writeDataYaml(key1='price',vlue1=r.json()['data']['price'])

    def test_007(self):
        '''超级会员微信下单'''
        r = self.obj.post(307,data=setWXZapp_04(307),headers=getHeaderWXB_App())
        mylog.info('result：%s' % r.json())
        self.isContent(r,307)

    def test_008(self):
        '''超级会员支付宝下单'''
        time.sleep(2)
        r = self.obj.post(308,data=setWXZapp_04(308),headers=getHeaderWXB_App())
        mylog.info('result：%s' % r.json())
        self.isContent(r,308)

    def test_009(self):
        '''我的收藏拉取商品列表'''
        r = self.obj.post(309,data=setWXZapp_01(309),headers=getHeaderWXB_App())
        mylog.info('result：%s' % r.json())
        self.isContent(r,309)
        writeDataYaml(key1='APP_goods_id',vlue1=r.json()['data']['goods_list'][0]['info']['goods_id'])
        writeDataYaml(key1='APP_goods_type',vlue1=r.json()['data']['goods_list'][0]['info']['goods_type'])

    def test_010(self):
        '''进入每天听见吴晓波会员详情页'''
        r = self.obj.post(310,data=setWXZapp_05(),headers=getHeaderWXB_App())
        mylog.info('result：%s' % r.json())
        self.isContent(r,310)

    def test_011(self):
        '''每天听见吴晓波会员微信下单'''
        r = self.obj.post(311,data=setWXZapp_06(311),headers=getHeaderWXB_App())
        mylog.info('result：%s' % r.json())
        self.isContent(r,311)

    def test_012(self):
        '''每天听见吴晓波会员支付宝下单'''
        r = self.obj.post(312,data=setWXZapp_06(312),headers=getHeaderWXB_App())
        mylog.info('result：%s' % r.json())
        self.isContent(r,312)

if __name__ == '__main__':
    unittest.main()

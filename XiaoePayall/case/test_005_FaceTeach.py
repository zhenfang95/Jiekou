#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/12/23 14:26

import unittest
import re
import requests
from common import readExcel
from base.method import *
from page.xiaoe import *

class TestFaceTeach(unittest.TestCase):
    '''面授课支付下单'''
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
        '''新建体验课'''
        r = self.obj.post(237,data=setNewFace(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,237)
        writeDataYaml(key1='course_offline_id_01',vlue1=r.json()['data']['course_offline_id'])

    def test_002(self):
        '''获取体验课列表'''
        r = self.obj.method(238,data=self.requesData(238),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,238)
        writeDataYaml(key1='goods_code_01',vlue1=r.json()['data']['list'][0]['specs'][0]['goods_code'])

    def test_003(self):
        '''面授课批价下单'''
        r = self.obj.post(239,data=setFace_buy(row=239,keyid1='goods_code_01',keyid2='course_offline_id_01'),headers=getHeadersInfo_H5())
        #mylog.info('result：%s' % r.json())
        self.isContent(r,239)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_16',vlue1=r.json()['data']['best_coupon']['cu_id'])

    def test_004(self):
        '''体验课下单支付'''
        r = self.obj.post(240,data=setFace_buy02(),headers=getHeadersPublic_H5('face_url'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,240)

    def test_005(self):
        '''体验课优惠券下单支付'''
        time.sleep(2)
        r = self.obj.post(241,data=setFace_buy03(),headers=getHeadersPublic_H5('face_url'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,241)

    def test_006(self):
        '''新建课程-课时售卖'''
        r = self.obj.post(242,data=setNewCourse(row=242,name='pay_课时',title='pay_课节_'),headers=getHeaderJson())
        mylog.info('result：%s' % r.json())
        self.isContent(r,242)
        writeDataYaml(key1='course_id_01',vlue1=r.json()['data']['course_id'])

    def test_007(self):
        '''新建招生-课时'''
        r = self.obj.post(243,data=setNewFacehour(row=243,title='Pay_正式课-课时售卖',couid='course_id_01'),headers=getHeaderJson())
        mylog.info('result：%s' % r.json())
        self.isContent(r,243)
        writeDataYaml(key1='course_offline_id_02',vlue1=r.json()['data']['course_offline_id'])

    def test_008(self):
        '''获取正式课-课时列表'''
        r = self.obj.method(244,data=self.requesData(244),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,244)
        writeDataYaml(key1='goods_code_02',vlue1=r.json()['data']['list'][0]['specs'][0]['goods_code'])

    def test_009(self):
        '''课时面授课批价下单'''
        r = self.obj.post(245,data=setFace_buy(row=245,keyid1='goods_code_02',keyid2='course_offline_id_02'),headers=getHeadersPublic_H5('face_url'))
        #mylog.info('result：%s' % r.json())
        self.isContent(r,245)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_17', vlue1=r.json()['data']['coupon']['valid'][0]['cu_id'])

    def test_010(self):
        '''课时面授课下单支付'''
        r =self.obj.post(246,data=setFaceBuy_hsb(row=246,skid='goods_code_02',reid='course_offline_id_02',couid='course_id_01'),headers=getHeadersPublic_H5('face_url'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,246)

    def test_011(self):
        '''课时面授课优惠券下单支付'''
        r = self.obj.post(247,data=setFaceBuy_hsb_c(row=247,skid='goods_code_02',reid='course_offline_id_02',cosid='course_id_01',cu_id='cu_id_17'),headers=getHeadersPublic_H5('face_url'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,247)

    def test_012(self):
        '''新建课程-时段售卖'''
        r = self.obj.post(248,data=setNewCourse(row=248,name='pay_课程',title='pay_课节_'),headers=getHeaderJson())
        mylog.info('result：%s' % r.json())
        self.isContent(r,248)
        writeDataYaml(key1='course_id_02',vlue1=r.json()['data']['course_id'])

    def test_013(self):
        '''新建招生-时段'''
        r = self.obj.post(249,data=setNewFacehour(row=249,title='Pay_正式课-时段售卖',couid='course_id_02'),headers=getHeaderJson())
        mylog.info('result：%s' % r.json())
        self.isContent(r,249)
        writeDataYaml(key1='course_offline_id_03',vlue1=r.json()['data']['course_offline_id'])

    def test_014(self):
        '''获取正式课-时段列表'''
        r = self.obj.method(250,data=self.requesData(250),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,250)
        writeDataYaml(key1='goods_code_03',vlue1=r.json()['data']['list'][0]['specs'][0]['goods_code'])

    def test_015(self):
        '''时段面授课批价下单'''
        r = self.obj.post(251,data=setFace_buy(row=251,keyid1='goods_code_03',keyid2='course_offline_id_03'),headers=getHeadersPublic_H5('face_url'))
        #mylog.info('result：%s' % r.json())
        self.isContent(r,251)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_18', vlue1=r.json()['data']['coupon']['valid'][0]['cu_id'])

    def test_016(self):
        '''时段面授课下单支付'''
        r =self.obj.post(252,data=setFaceBuy_hsb(row=252,skid='goods_code_03',reid='course_offline_id_03',couid='course_id_02'),headers=getHeadersPublic_H5('face_url'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,252)

    def test_017(self):
        '''时段面授课优惠券下单支付'''
        time.sleep(2)
        r = self.obj.post(253,data=setFaceBuy_hsb_c(row=253,skid='goods_code_03',reid='course_offline_id_03',cosid='course_id_02',cu_id='cu_id_18'),headers=getHeadersPublic_H5('face_url'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,253)

    def test_018(self):
        '''新建课程-班级售卖'''
        r = self.obj.post(254,data=setNewCourse(row=254,name='pay_课程',title='pay_课节_'),headers=getHeaderJson())
        mylog.info('result：%s' % r.json())
        self.isContent(r,254)
        writeDataYaml(key1='course_id_03',vlue1=r.json()['data']['course_id'])

    def test_019(self):
        '''新建班级'''
        r = self.obj.post(255,data=setNewFaceClass(),headers=getHeaderJson())
        mylog.info('result：%s' % r.json())
        self.isContent(r,255)
        writeDataYaml(key1='class_id',vlue1=r.json()['data']['class_id'])
        writeDataYaml(key1='class_name',vlue1=r.json()['data']['class_name'])

    def test_020(self):
        '''新建招生-班级'''
        r = self.obj.post(256,data=setFaceClass(),headers=getHeaderJson())
        mylog.info('result：%s' % r.json())
        self.isContent(r,256)
        writeDataYaml(key1='course_offline_id_04',vlue1=r.json()['data']['course_offline_id'])

    def test_021(self):
        '''获取正式课-班级列表'''
        r = self.obj.method(257, data=self.requesData(257), headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,257)
        writeDataYaml(key1='goods_code_04', vlue1=r.json()['data']['list'][0]['specs'][0]['goods_code'])

    def test_022(self):
        '''班级面授课批价下单'''
        r = self.obj.post(258, data=setFace_buy(row=258, keyid1='goods_code_04', keyid2='course_offline_id_04'),headers=getHeadersPublic_H5('face_url'))
        #mylog.info('result：%s' % r.json())
        self.isContent(r,258)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_19', vlue1=r.json()['data']['coupon']['valid'][0]['cu_id'])

    def test_023(self):
        '''班级面授课下单支付'''
        r = self.obj.post(259, data=setFaceBuy_hsb(row=259, skid='goods_code_04', reid='course_offline_id_04',couid='course_id_03'), headers=getHeadersPublic_H5('face_url'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,259)

    def test_024(self):
        '''班级面授课优惠券下单支付'''
        time.sleep(2)
        r = self.obj.post(260, data=setFaceBuy_hsb_c(row=260, skid='goods_code_04', reid='course_offline_id_04',cosid='course_id_03', cu_id='cu_id_19'),headers=getHeadersPublic_H5('face_url'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,260)

if __name__=='__main__':
    unittest.main()
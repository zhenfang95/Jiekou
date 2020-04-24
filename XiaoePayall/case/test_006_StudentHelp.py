#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/12/25 10:19

import unittest
import re
import requests
from common import readExcel
from base.method import *
from page.xiaoe import *

class TestStudentHelp(unittest.TestCase):
    '''助学工具支付下单'''
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
        '''新建日历打卡'''
        r = self.obj.post(262,data=setCalendarclock(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,262)
        writeDataYaml(key1='activity_id_6',vlue1=r.json()['data']['activity_id'])

    def test_002(self):
        '''进入h5日历打卡页面'''
        r = requests.get(self.excel.getUrl(263).format(getRead(key1='activity_id_6')),headers=getHeadersInfo_H5(),verify=False)
        self.assertIn('打卡主页',r.text)
        mylog.info('result：PASS')

    def test_003(self):
        '''日历打卡批价下单'''
        r = self.obj.post(264,data=setCalendarBuy(row=264,keyid='activity_id_6'),headers=getHeadersInfo_H5())
        #mylog.info('result：%s' % r.json())
        self.isContent(r,264)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_20',vlue1=r.json()['data']['best_coupon']['cu_id'])

    def test_004(self):
        '''日历打卡下单支付'''
        r = self.obj.post(265,data=setCalendarBuy(row=265,keyid='activity_id_6'),headers=getHeadersPublic_H5('clock_url'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,265)

    def test_005(self):
        '''日历打卡优惠券下单支付'''
        time.sleep(2)
        r = self.obj.post(266,data=setCalendarBuy_c(row=266,keyid='activity_id_6',cuid='cu_id_20'),headers=getHeadersPublic_H5('clock_url'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,266)

    def test_006(self):
        '''新建作业打卡'''
        r = self.obj.post(267,data=setTaskclock(),headers=getHeaderJson())
        mylog.info('result：%s' % r.json())
        self.isContent(r,267)
        writeDataYaml(key1='activity_id_7',vlue1=r.json()['data']['activity_id'])

    def test_007(self):
        '''进入h5作业打卡页面'''
        r = requests.get(self.excel.getUrl(268).format(getRead(key1='activity_id_7')),headers=getHeadersInfo_H5(),verify=False)
        self.assertIn('打卡主页',r.text)
        mylog.info('result：PASS')

    def test_008(self):
        '''作业打卡批价下单'''
        r = self.obj.post(269,data=setCalendarBuy(row=269,keyid='activity_id_7'),headers=getHeadersInfo_H5())
        #mylog.info('result：%s' % r.json())
        self.isContent(r,269)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_21',vlue1=r.json()['data']['best_coupon']['cu_id'])

    def test_009(self):
        '''作业打卡下单支付'''
        r = self.obj.post(270,data=setCalendarBuy(row=270,keyid='activity_id_7'),headers=getHeadersPublic_H5('clock_url'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,270)

    def test_010(self):
        '''作业打卡优惠券下单支付'''
        time.sleep(2)
        r = self.obj.post(271,data=setCalendarBuy_c(row=271,keyid='activity_id_7',cuid='cu_id_21'),headers=getHeadersPublic_H5('clock_url'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,271)

    def test_011(self):
        '''新建闯关打卡'''
        r = self.obj.post(272,data=setPassclock(),headers=getHeaderJson())
        mylog.info('result：%s' % r.json())
        self.isContent(r,272)
        writeDataYaml(key1='activity_id_8',vlue1=r.json()['data']['activity_id'])

    def test_012(self):
        '''进入h5闯关打卡页面'''
        r = requests.get(self.excel.getUrl(273).format(getRead(key1='activity_id_8')),headers=getHeadersInfo_H5(),verify=False)
        self.assertIn('打卡主页',r.text)
        mylog.info('result：PASS')

    def test_013(self):
        '''闯关打卡批价下单'''
        r = self.obj.post(274,data=setCalendarBuy(row=274,keyid='activity_id_8'),headers=getHeadersInfo_H5())
        #mylog.info('result：%s' % r.json())
        self.isContent(r,274)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_22',vlue1=r.json()['data']['best_coupon']['cu_id'])

    def test_014(self):
        '''闯关打卡下单支付'''
        r = self.obj.post(275,data=setCalendarBuy(row=275,keyid='activity_id_8'),headers=getHeadersPublic_H5('clock_url'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,275)

    def test_015(self):
        '''闯关打卡优惠券下单支付'''
        time.sleep(2)
        r = self.obj.post(276,data=setCalendarBuy_c(row=276,keyid='activity_id_8',cuid='cu_id_22'),headers=getHeadersPublic_H5('clock_url'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,276)

    def test_016(self):
        '''新建教辅周边商品'''
        r = self.obj.post(277,data=setNewTeaching(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,277)

    def test_017(self):
        '''获取教辅周边商品列表'''
        r = self.obj.method(278,params=self.requesData(278),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,278)
        writeDataYaml(key1='pageurl_11',vlue1=r.json()['data']['data'][0]['pageUrl'])
        writeDataYaml(key1='resource_id_18',vlue1=r.json()['data']['data'][0]['id'])

    def test_018(self):
        '''教辅周边商品批价下单'''
        r = self.obj.post(279,data=setTeaching(row=279,keyid='resource_id_18'),headers=getHeadersInfo_H5())
        #mylog.info('result：%s' % r.json())
        self.isContent(r,279)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')

    def test_019(self):
        '''教辅周边商品下单支付'''
        r = self.obj.post(280,data=setTeaching(row=280,keyid='resource_id_18'),headers=getHeadersPublic_H5('clock_url'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,280)

    def test_020(self):
        '''新建小社群'''
        r = self.obj.post(281,data=setNewCommunity(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,281)
        writeDataYaml(key1='com_id',vlue1=r.json()['com_id'])

    def test_021(self):
        '''获取小社群列表'''
        r = self.obj.get(282,headers=getHeadersInfo())
        self.assertIn('data-clipboard-text="https:',r.text)
        writeDataYaml(key1='pageurl_12',vlue1=re.findall(r'data-clipboard-text="(.+?)">',r.text)[0])

    def test_022(self):
        '''小社群下单支付'''
        r = self.obj.post(283,data=setCommunity(),headers=getHeadersPublic_H5('pageurl_12'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,283)

    def test_023(self):
        '''进入付费问答主页'''
        r = self.obj.get(284,headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,284)
        writeDataYaml(key1='pageurl_13',vlue1=r.json()['data']['page_url'])
        writeDataYaml(key1='q_id',vlue1=r.json()['data']['id'])

    def test_024(self):
        '''编辑付费问答'''
        r = self.obj.post(285,data=setAnswers(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,285)

    def test_025(self):
        '''编辑答主'''
        r = self.obj.post(286,data=setAnswersUser(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,286)

    def test_026(self):
        '''访问付费问答专区'''
        r = self.obj.post(287,data=setAnswers_u(row=287),headers=getHeadersPublic_H5('pageurl_13'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,287)

    def test_027(self):
        '''付费问答专区上传图片'''
        r = self.obj.method(288,data=self.requesData(288),headers=getHeadersPublic_H5('pageurl_13'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,288)

    def test_028(self):
        '''付费问答专区提问'''
        r = self.obj.post(289,data=setAnswers_u1(),headers=getHeadersPublic_H5('pageurl_13'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,289)
        writeDataYaml(key1='question_id',vlue1=r.json()['data']['question_id'])

    def test_029(self):
        '''付费问答专区下单'''
        r = self.obj.post(290,data=setAnswers_u2(row=290,keyid='question_id'),headers=getHeadersPublic_H5('pageurl_13'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,290)

    def test_030(self):
        '''访问付费问答的回答专区'''
        r = self.obj.post(291,data=setAnswers_u(row=291),headers=getHeadersPublic_H5('pageurl_13'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,291)
        writeDataYaml(key1='question_id_1',vlue1=r.json()['data'][0]['question_id'])

    def test_031(self):
        '''访问付费问答的回答专区下单'''
        r = self.obj.post(292,data=setAnswers_u2(row=292,keyid='question_id_1'),headers=getHeadersPublic_H5('pageurl_13'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,292)

    def test_032(self):
        '''新建活动管理-付费'''
        r = self.obj.post(293,data=setNewActivity(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,293)

    def test_033(self):
        '''获取活动管理列表'''
        r = self.obj.method(294,data=self.requesData(294),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,294)
        writeDataYaml(key1='activity_id_9',vlue1=r.json()['data']['list'][0]['id'])
        writeDataYaml(key1='activity_url',vlue1=r.json()['data']['list'][0]['activity_url'])

    def test_034(self):
        '''进入付费活动页'''
        r = requests.get(self.excel.getUrl(295).format(getRead(key1='activity_url').split('/')[4]),headers=getHeadersInfo_H5(),verify=False)
        self.assertIn('Pay_活动管理',r.text)

    def test_035(self):
        '''参与付费活动'''
        r = self.obj.post(296,data=setActivity(),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,296)
        writeDataYaml(key1='sku_id',vlue1=r.json()['data']['tickets'][0]['sku_id'])
        writeDataYaml(key1='ticket_id',vlue1=r.json()['data']['tickets'][0]['ticket_id'])

    def test_036(self):
        '''付费活动原价批价下单'''
        r = self.obj.post(297,data=setActivity_o(),headers=getHeadersInfo_H5())
        #mylog.info('result：%s' % r.json())
        self.isContent(r,297)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_23',vlue1=r.json()['data']['coupon']['valid'][0]['cu_id'])

    def test_037(self):
        '''付费活动下单支付'''
        time.sleep(2)
        r = self.obj.post(298,data=setActivity_p(),headers=getHeaderActivity_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,298)

    def test_038(self):
        '''付费活动优惠券下单支付'''
        time.sleep(2)
        r = self.obj.post(299,data=setActivity_c(),headers=getHeaderActivity_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,299)

if __name__=='__main__':
    unittest.main()
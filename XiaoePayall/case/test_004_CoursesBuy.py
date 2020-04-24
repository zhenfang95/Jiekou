#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/12/11 18:13

import unittest
import re,urllib,json
import requests
from common import readExcel
from base.method import *
from page.xiaoe import *

class TestCoursesBuy(unittest.TestCase):
    '''在线课程支付下单'''
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

    def isContent_a(self,r,row):
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 1)
        self.assertTrue(self.asser.isContent(row=row,str1=r.text))

    def test_001(self):
        '''B端停用超级会员'''
        r = self.obj.get(116,headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,116)

    def test_002(self):
        '''B端启用超级会员'''
        r = self.obj.get(117,headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,117)

    def test_003(self):
        '''B端获取超级会员svip_id'''
        r = self.obj.get(118,headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,118)
        writeDataYaml(key1='svip_id',vlue1=r.json()['data']['base_info']['id'])

    def test_004(self):
        '''C端获取超级会员页面链接地址'''
        r = self.obj.post(119,headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,119)
        writeDataYaml(key1='pageUrl13',vlue1=r.json()['data']['jump_url'])

    def test_005(self):
        '''C端超级会员购买批价'''
        time.sleep(5)
        r = self.obj.post(120,data=setSvip(),headers=getSvip_h5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,120)

    def test_006(self):
        '''C端超级会员购买/续费'''
        time.sleep(5)
        r = self.obj.post(121,data=setSvip_1(),headers=getSvip_h5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,121)

    def test_007(self):
        '''B端调用上传图片接口'''
        r = self.obj.get(122,headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.assertEqual(r.json()['code'],'0')
        self.assertEqual(r.json()['message'],'成功')

    def test_008(self):
        '''B端新建图文'''
        r = self.obj.post(123,data=setNewgraphic01(row=123,title='Pay_新建图文'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,123)
        writeDataYaml(key1='resource_id_10',vlue1=r.json()['data']['resource_id'])

    def test_009(self):
        '''B端图文再次编辑'''
        r = self.obj.post(124,data=setEditagain(row=124,title='Pay_编辑图文',resource_id='resource_id_10'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,124)

    def test_010(self):
        '''获取B端图文列表'''
        r = self.obj.method(125,params=self.requesData(125),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,125)
        writeDataYaml(key1='content_url_7',vlue1=r.json()['data']['resourceList'][0]['pageUrl'])

    def test_011(self):
        '''C端进入图文详情页'''
        r = self.obj.post(126,data=setXqpublic(row=126,keyid='resource_id_10',pageurl='content_url_7'),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,126)

    def test_012(self):
        '''购买图文批价下单'''
        time.sleep(5)
        r = self.obj.post(127,data=setBuyPublic(row=127,keyid='resource_id_10'),headers=getHeadersInfo_H5())
        #mylog.info('result：%s' % r.json())
        self.isContent(r,127)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_3',vlue1=r.json()['data']['coupon']['valid'][0]['cu_id'])

    def test_013(self):
        '''购买图文下单支付'''
        r = self.obj.post(128,data=setBuyPublic(row=128,keyid='resource_id_10'),headers=getHeadersPublic_H5('content_url_7'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,128)

    def test_014(self):
        '''购买图文优惠券下单支付'''
        r = self.obj.post(129,data=setCouponPublic(row=129,keyid='resource_id_10',cuid='cu_id_3'),headers=getHeadersPublic_H5('content_url_7'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,129)

    def test_015(self):
        '''购买后确认图文内容'''
        r = self.obj.post(130,data=setXqpublic(row=130,keyid='resource_id_10',pageurl='content_url_7'),headers=getHeadersPublic_H5('content_url_7'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,130)

    def test_016(self):
        '''新建音频'''
        r = self.obj.post(131,data=setNewgraphic01(131,title='pay_新建音频'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,131)
        writeDataYaml(key1='resource_id_11',vlue1=r.json()['data']['resource_id'])

    def test_017(self):
        '''再次编辑音频'''
        r = self.obj.post(132,data=setEditagain(row=132,title='pay_编辑音频',resource_id='resource_id_11'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,132)

    def test_018(self):
        '''获取音频列表'''
        r = self.obj.method(133,params=self.requesData(133),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,133)
        writeDataYaml(key1='pageurl_01',vlue1=r.json()['data']['resourceList'][0]['pageUrl'])

    def test_019(self):
        '''C端进入音频商品详情页'''
        r = self.obj.post(134,data=setXqpublic(row=134,keyid='resource_id_11',pageurl='pageurl_01'),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,134)

    def test_020(self):
        '''购买音频批价下单'''
        time.sleep(5)
        r = self.obj.post(135,data=setBuyPublic(row=135,keyid='resource_id_11'),headers=getHeadersInfo_H5())
        #mylog.info('result：%s' % r.json())
        self.isContent(r,135)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_4',vlue1=r.json()['data']['coupon']['valid'][0]['cu_id'])

    def test_021(self):
        '''购买音频下单支付'''
        r = self.obj.post(136,data=setBuyPublic(row=136,keyid='resource_id_11'),headers=getHeadersPublic_H5('pageurl_01'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,136)

    def test_022(self):
        '''购买音频优惠券下单支付'''
        r = self.obj.post(137,data=setCouponPublic(row=137,keyid='resource_id_11',cuid='cu_id_4'),headers=getHeadersPublic_H5('pageurl_01'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,137)

    def test_023(self):
        '''购买后确认音频购买成功'''
        r = self.obj.post(138,data=setXqpublic(row=138,keyid='resource_id_11',pageurl='pageurl_01'),headers=getHeadersPublic_H5('pageurl_01'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,138)

    def test_024(self):
        '''B端调用上传视频接口'''
        r = self.obj.method(139,data=self.requesData(139),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,139)

    def test_025(self):
        '''新建视频'''
        r = self.obj.post(140,data=setNewgraphic01(140,title='pay_新建视频'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,140)
        writeDataYaml(key1='resource_id_12',vlue1=r.json()['data']['resource_id'])

    def test_026(self):
        '''再次编辑视频'''
        r = self.obj.post(141,data=setEditagain(row=141,title='pay_编辑视频',resource_id='resource_id_12'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,141)

    def test_027(self):
        '''获取视频列表'''
        r = self.obj.method(142,params=self.requesData(142),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,142)
        writeDataYaml(key1='pageurl_02',vlue1=r.json()['data']['resourceList'][0]['pageUrl'])

    def test_028(self):
        '''C端进入视频商品详情页'''
        r = self.obj.post(143,data=setXqpublic(row=143,keyid='resource_id_12',pageurl='pageurl_02'),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,143)

    def test_029(self):
        '''购买视频批价下单'''
        time.sleep(5)
        r = self.obj.post(144,data=setBuyPublic(row=144,keyid='resource_id_12'),headers=getHeadersInfo_H5())
        #mylog.info('result：%s' % r.json())
        self.isContent(r,144)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_5',vlue1=r.json()['data']['coupon']['valid'][0]['cu_id'])

    def test_030(self):
        '''购买视频下单支付'''
        r = self.obj.post(145,data=setBuyPublic(row=145,keyid='resource_id_12'),headers=getHeadersPublic_H5('pageurl_02'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,145)

    def test_031(self):
        '''购买视频优惠券下单支付'''
        r = self.obj.post(146,data=setCouponPublic(row=146,keyid='resource_id_12',cuid='cu_id_5'),headers=getHeadersPublic_H5('pageurl_02'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,146)

    def test_032(self):
        '''购买后确认视频购买成功'''
        r = self.obj.post(147,data=setXqpublic(row=147,keyid='resource_id_12',pageurl='pageurl_02'),headers=getHeadersPublic_H5('pageurl_02'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,147)

    def test_033(self):
        '''新建语音直播'''
        r = self.obj.post(148,data=setNewLive(row=148,title='pay_新建语音直播'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,148)
        writeDataYaml(key1='alive_id_01',vlue1=r.json()['alive_id'])

    def test_034(self):
        '''重新编辑语音直播'''
        r = self.obj.post(149,data=setEditLive(row=149,title='pay_编辑语音直播',alive_id='alive_id_01'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,149)

    def test_035(self):
        '''获取语音直播列表'''
        r = self.obj.method(150,params=self.requesData(150),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,150)
        writeDataYaml(key1='pageurl_03',vlue1=r.json()['data']['resourceList'][0]['pageUrl'])

    def test_036(self):
        '''C端进入语音直播详情页'''
        r = self.obj.post(151,data=setXqpublic(row=151,keyid='alive_id_01',pageurl='pageurl_03'),headers=getHeadersPublic_H5('pageurl_03'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,151)

    def test_037(self):
        '''购买语音直播批价下单'''
        time.sleep(5)
        r = self.obj.post(152,data=setBuyPublic(row=152,keyid='alive_id_01'),headers=getHeadersPublic_H5('pageurl_03'))
        #mylog.info('result：%s' % r.json())
        self.isContent(r,152)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_6', vlue1=r.json()['data']['coupon']['valid'][0]['cu_id'])

    def test_038(self):
        '''购买语音直播下单支付'''
        r = self.obj.post(153,data=setLivepublic(row=153,keyid='alive_id_01'),headers=getHeadersPublic_H5('pageurl_03'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,153)

    def test_039(self):
        '''购买语音直播优惠券下单支付'''
        r = self.obj.post(154,data=setLiveCoupublic(row=154,keyid='alive_id_01',cuid='cu_id_6'),headers=getHeadersPublic_H5('pageurl_03'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,154)

    def test_040(self):
        '''确认语音直播购买成功'''
        r = self.obj.post(155,data=setXqpublic(row=155,keyid='alive_id_01',pageurl='pageurl_03'),headers=getHeadersPublic_H5('pageurl_03'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,155)

    def test_041(self):
        '''B端设置直播嘉宾、讲师'''
        r = self.obj.post(156,data=setLivey1(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,156)

    def test_042(self):
        '''C端获取一个进入直播间的alive_room_url'''
        r = requests.get(self.excel.getUrl(157).format(getRead(key1='alive_id_01')),headers=getHeadersInfo_H5(),verify=False)
        self.isContent(r,157)
        writeDataYaml(key1='alive_room',vlue1=r.json()['data']['bizData']['data']['alive_room'])

    def test_043(self):
        '''获取直播间的room_id'''
        url=self.excel.getUrl(158).format(getRead(key1='alive_room').split('/')[4])
        r = requests.get(url,headers=getHeadersInfo_H5(),verify=False)
        self.assertIn('value="{',r.text)
        writeDataYaml(key1='room_id',vlue1=list(re.findall(r'&quot;group_id&quot;:&quot;(.+?)&quot',r.text))[0])


    def test_044(self):
        '''C端讲师发语音'''
        r = self.obj.post(159,data=setLivey2(),headers=getHeadersInfo_H5_VIP())
        mylog.info('result：%s' % r.json())
        self.isContent(r,159)

    def test_045(self):
        '''学员给讲师打赏'''
        r = self.obj.post(160,data=setLivey3(),headers=getHeadersLive_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,160)

    def test_046(self):
        '''新建视频直播'''
        r = self.obj.post(161,data=setNewLive(row=161,title='pay_新建视频直播'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,161)
        writeDataYaml(key1='alive_id_02',vlue1=r.json()['alive_id'])

    def test_047(self):
        '''重新编辑视频直播'''
        r = self.obj.post(162,data=setEditLive(row=162,title='pay_编辑视频直播',alive_id='alive_id_02'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,162)

    def test_048(self):
        '''获取视频直播列表'''
        r = self.obj.method(163,params=self.requesData(163),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,163)
        writeDataYaml(key1='pageurl_04',vlue1=r.json()['data']['resourceList'][0]['pageUrl'])

    def test_049(self):
        '''C端进入视频直播详情页'''
        r = self.obj.post(164,data=setXqpublic(row=164,keyid='alive_id_02',pageurl='pageurl_04'),headers=getHeadersPublic_H5('pageurl_04'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,164)

    def test_050(self):
        '''购买视频直播批价下单'''
        time.sleep(5)
        r = self.obj.post(165, data=setBuyPublic(row=165, keyid='alive_id_02'),headers=getHeadersPublic_H5('pageurl_04'))
        #mylog.info('result：%s' % r.json())
        self.isContent(r, 165)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_7', vlue1=r.json()['data']['coupon']['valid'][0]['cu_id'])

    def test_051(self):
        '''购买视频直播下单支付'''
        r = self.obj.post(166,data=setLivepublic(row=166,keyid='alive_id_02'),headers=getHeadersPublic_H5('pageurl_04'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,166)

    def test_052(self):
        '''购买视频直播优惠券下单支付'''
        r = self.obj.post(167,data=setLiveCoupublic(row=167,keyid='alive_id_02',cuid='cu_id_7'),headers=getHeadersPublic_H5('pageurl_04'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,167)

    def test_053(self):
        '''确认视频直播购买成功'''
        r = self.obj.post(168,data=setXqpublic(row=168,keyid='alive_id_02',pageurl='pageurl_04'),headers=getHeadersPublic_H5('pageurl_04'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,168)

    def test_054(self):
        '''新建ppt直播'''
        r = self.obj.post(169,data=setNewLive(row=169,title='pay_新建ppt直播'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,169)
        writeDataYaml(key1='alive_id_03',vlue1=r.json()['alive_id'])

    def test_055(self):
        '''重新编辑ppt直播'''
        r = self.obj.post(170,data=setEditLive(row=170,title='pay_编辑ppt直播',alive_id='alive_id_03'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,170)

    def test_056(self):
        '''获取ppt直播列表'''
        r = self.obj.method(171,params=self.requesData(171),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,171)
        writeDataYaml(key1='pageurl_05',vlue1=r.json()['data']['resourceList'][0]['pageUrl'])

    def test_057(self):
        '''C端进入ppt直播详情页'''
        r = self.obj.post(172,data=setXqpublic(row=172,keyid='alive_id_03',pageurl='pageurl_05'),headers=getHeadersPublic_H5('pageurl_05'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,172)

    def test_058(self):
        '''购买ppt直播批价下单'''
        time.sleep(5)
        r = self.obj.post(173, data=setBuyPublic(row=173, keyid='alive_id_03'),headers=getHeadersPublic_H5('pageurl_05'))
        #mylog.info('result：%s' % r.json())
        self.isContent(r,173)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_8', vlue1=r.json()['data']['coupon']['valid'][0]['cu_id'])

    def test_059(self):
        '''购买ptt直播下单支付'''
        r = self.obj.post(174,data=setLivepublic(row=174,keyid='alive_id_03'),headers=getHeadersPublic_H5('pageurl_05'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,174)

    def test_060(self):
        '''购买ppt直播优惠券下单支付'''
        r = self.obj.post(175,data=setLiveCoupublic(row=175,keyid='alive_id_03',cuid='cu_id_8'),headers=getHeadersPublic_H5('pageurl_05'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,175)

    def test_061(self):
        '''确认ppt直播购买成功'''
        r = self.obj.post(176,data=setXqpublic(row=176,keyid='alive_id_03',pageurl='pageurl_05'),headers=getHeadersPublic_H5('pageurl_05'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,176)

    def test_062(self):
        '''新建实时视频直播'''
        r = self.obj.post(177,data=setNewLive(row=177,title='pay_新建实时视频直播'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,177)
        writeDataYaml(key1='alive_id_04',vlue1=r.json()['alive_id'])

    def test_063(self):
        '''重新编辑实时视频直播'''
        r = self.obj.post(178,data=setEditLive(row=178,title='pay_编辑实时视频直播',alive_id='alive_id_04'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,178)

    def test_064(self):
        '''获取实时视频直播列表'''
        r = self.obj.method(179,params=self.requesData(179),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,179)
        writeDataYaml(key1='pageurl_06',vlue1=r.json()['data']['resourceList'][0]['pageUrl'])

    def test_065(self):
        '''C端进入实时视频直播详情页'''
        r = self.obj.post(180,data=setXqpublic(row=180,keyid='alive_id_04',pageurl='pageurl_06'),headers=getHeadersPublic_H5('pageurl_06'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,180)

    def test_066(self):
        '''购买实时视频直播批价下单'''
        time.sleep(5)
        r = self.obj.post(181, data=setBuyPublic(row=181, keyid='alive_id_04'),headers=getHeadersPublic_H5('pageurl_06'))
        #mylog.info('result：%s' % r.json())
        self.isContent(r,181)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_9', vlue1=r.json()['data']['coupon']['valid'][0]['cu_id'])

    def test_067(self):
        '''购买实时视频直播下单支付'''
        r = self.obj.post(182,data=setLivepublic(row=182,keyid='alive_id_04'),headers=getHeadersPublic_H5('pageurl_06'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,182)

    def test_068(self):
        '''购买实时视频直播优惠券下单支付'''
        r = self.obj.post(183,data=setLiveCoupublic(row=183,keyid='alive_id_04',cuid='cu_id_9'),headers=getHeadersPublic_H5('pageurl_06'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,183)

    def test_069(self):
        '''确认实时视频直播购买成功'''
        r = self.obj.post(184,data=setXqpublic(row=184,keyid='alive_id_04',pageurl='pageurl_06'),headers=getHeadersPublic_H5('pageurl_06'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,184)

    def test_070(self):
        '''新建桌面共享直播'''
        r = self.obj.post(185,data=setNewLive(row=185,title='pay_新建桌面共享直播'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,185)
        writeDataYaml(key1='alive_id_05',vlue1=r.json()['alive_id'])

    def test_071(self):
        '''重新编辑桌面共享直播'''
        r = self.obj.post(186,data=setEditLive(row=186,title='Pay_编辑桌面共享直播',alive_id='alive_id_05'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,186)

    def test_072(self):
        '''获取桌面共享直播列表'''
        r = self.obj.method(187,params=self.requesData(187),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,187)
        writeDataYaml(key1='pageurl_07',vlue1=r.json()['data']['resourceList'][0]['pageUrl'])

    def test_073(self):
        '''C端进入桌面共享直播详情页'''
        r = self.obj.post(188,data=setXqpublic(row=188,keyid='alive_id_05',pageurl='pageurl_07'),headers=getHeadersPublic_H5('pageurl_07'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,188)

    def test_074(self):
        '''购买桌面共享直播批价下单'''
        time.sleep(5)
        r = self.obj.post(189, data=setBuyPublic(row=189, keyid='alive_id_05'),headers=getHeadersPublic_H5('pageurl_07'))
        #mylog.info('result：%s' % r.json())
        self.isContent(r,189)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_10', vlue1=r.json()['data']['coupon']['valid'][0]['cu_id'])

    def test_075(self):
        '''购买桌面共享直播下单支付'''
        r = self.obj.post(190,data=setLivepublic(row=190,keyid='alive_id_05'),headers=getHeadersPublic_H5('pageurl_07'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,190)

    def test_076(self):
        '''购买桌面共享直播优惠券下单支付'''
        r = self.obj.post(191,data=setLiveCoupublic(row=191,keyid='alive_id_05',cuid='cu_id_10'),headers=getHeadersPublic_H5('pageurl_07'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,191)

    def test_077(self):
        '''确认桌面共享直播购买成功'''
        r = self.obj.post(192,data=setXqpublic(row=192,keyid='alive_id_05',pageurl='pageurl_07'),headers=getHeadersPublic_H5('pageurl_07'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,192)

    def test_078(self):
        '''新建电子书'''
        r = self.obj.post(193,data=setNewgraphic01(row=193,title='pay_新建电子书'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,193)
        writeDataYaml(key1='resource_id_13',vlue1=r.json()['data']['resource_id'])

    def test_079(self):
        '''再次编辑电子书'''
        r = self.obj.post(194,data=setEditagain(row=194,title='pay_编辑电子书',resource_id='resource_id_13'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,194)

    def test_080(self):
        '''获取电子书列表'''
        r = self.obj.method(195,params=self.requesData(195),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,195)
        writeDataYaml(key1='pageurl_08',vlue1=r.json()['data']['resourceList'][0]['pageUrl'])

    def test_081(self):
        '''C端进入电子书详情页'''
        r = self.obj.post(196,data=setXqpublic(row=196,keyid='resource_id_13',pageurl='pageurl_08'),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,196)

    def test_082(self):
        '''购买电子书批价下单'''
        time.sleep(5)
        r = self.obj.post(197,data=setBuyPublic(row=196,keyid='resource_id_13'),headers=getHeadersInfo_H5())
        self.isContent(r,197)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_11',vlue1=r.json()['data']['coupon']['valid'][0]['cu_id'])

    def test_083(self):
        '''购买电子书下单支付'''
        time.sleep(2)
        r = self.obj.post(198,data=setLivepublic(198,keyid='resource_id_13'),headers=getHeadersPublic_H5('pageurl_08'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,198)

    def test_084(self):
        '''购买电子书优惠券下单支付'''
        r = self.obj.post(199,data=setLiveCoupublic(row=199,keyid='resource_id_13',cuid='cu_id_11'),headers=getHeadersPublic_H5('pageurl_08'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,199)

    def test_085(self):
        '''确认电子书购买成功'''
        r = self.obj.post(200,data=setXqpublic(row=200,keyid='resource_id_13',pageurl='pageurl_08'),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,200)

    def test_086(self):
        '''新建专栏'''
        r = self.obj.post(201,data=setNewColumn(row=201,title='pay_新建专栏'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,201)
        writeDataYaml(key1='resource_id_14',vlue1=r.json()['data']['resource_id'])

    def test_087(self):
        '''重新编辑专栏'''
        r = self.obj.post(202,data=setEditColumn(row=202,title='pay_编辑专栏',resource_id='resource_id_14'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,202)

    def test_088(self):
        '''获取专栏列表'''
        r = self.obj.get(203,headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,203)
        writeDataYaml(key1='content_url_8',vlue1=r.json()['data']['packageListInfo']['data'][0]['content_url'])

    def test_089(self):
        '''专栏添加图文知识商品'''
        r = self.obj.post(204,data=setspColumn(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,204)

    def test_090(self):
        '''C端进入专栏详情页'''
        r = self.obj.post(205,data=setXqpublic_a(row=205,keyid='resource_id_14',pageurl='content_url_8'),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,205)

    def test_091(self):
        '''购买专栏批价下单'''
        time.sleep(5)
        r = self.obj.post(206,data=setBuyPublic_a(row=206,keyid='resource_id_14'),headers=getHeadersInfo_H5())
        #mylog.info('result：%s' % r.json())
        self.isContent(r,206)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_12',vlue1=r.json()['data']['coupon']['valid'][0]['cu_id'])

    def test_092(self):
        '''购买专栏下单支付'''
        r = self.obj.post(207,data=setColumnPublic(row=207,keyid='resource_id_14'),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,207)

    def test_093(self):
        '''购买专栏优惠券下单支付'''
        r = self.obj.post(208,data=setColumnPublic_c(row=208,keyid='resource_id_14',cuid='cu_id_12'),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,208)

    def test_094(self):
        '''新建大专栏'''
        r = self.obj.post(209,data=setNewColumn(row=209,title='pay_新建大专栏'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent_a(r,209)

    def test_095(self):
        '''获取大专栏列表'''
        r = self.obj.get(210,headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,210)
        writeDataYaml(key1='resource_id_15',vlue1=r.json()['data']['topicListInfo']['data'][0]['id'])
        writeDataYaml(key1='pageurl_09',vlue1=r.json()['data']['topic_on_url_list'][0])

    def test_096(self):
        '''重新编辑大专栏'''
        r = self.obj.post(211,data=setEditColumn(row=211,title='pay_编辑大专栏',resource_id='resource_id_15'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent_a(r,211)

    def test_097(self):
        '''将小专栏加入到大专栏'''
        r = self.obj.post(212,data=setspColumn_a(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,212)

    def test_098(self):
        '''C端进入大专栏详情页'''
        r = self.obj.post(213,data=setXqpublic_a(row=213,keyid='resource_id_15',pageurl='pageurl_09'),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,213)

    def test_099(self):
        '''购买大专栏批价下单'''
        time.sleep(5)
        r = self.obj.post(214,data=setBuyPublic_a(row=214,keyid='resource_id_15'),headers=getHeadersInfo_H5())
        self.isContent(r,214)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_13',vlue1=r.json()['data']['coupon']['valid'][0]['cu_id'])

    def test_100(self):
        '''购买大专栏下单支付'''
        r = self.obj.post(215,data=setColumn_pub(row=215,keyid='resource_id_15'),headers=getHeadersPublic_H5('pageurl_09'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,215)

    def test_101(self):
        '''购买大专栏优惠券下单支付'''
        r = self.obj.post(216,data=setColumn_pub_c(row=216,keyid='resource_id_15',cuid='cu_id_13'),headers=getHeadersPublic_H5('pageurl_09'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,216)

    def test_102(self):
        '''新建会员'''
        r = self.obj.post(217,data=setNewColumn(row=217,title='pay_新建会员'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,217)
        writeDataYaml(key1='resource_id_16',vlue1=r.json()['data']['resource_id'])

    def test_103(self):
        '''重新编辑会员'''
        r = self.obj.post(218,data=setEditColumn(row=218,title='pay_编辑会员',resource_id='resource_id_16'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,218)

    def test_104(self):
        '''添加会员权益（单品）'''
        r = self.obj.post(219,data=setVip1(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,219)

    def test_105(self):
        '''添加会员权益(专栏)'''
        r = self.obj.post(220,data=setVip2(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,220)

    def test_106(self):
        '''获取会员列表'''
        r = self.obj.get(221,headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,221)
        writeDataYaml(key1='pageurl_10',vlue1=r.json()['data']['member_on_url_list'][0])

    def test_107(self):
        '''C端进入购买会员详情页'''
        r = self.obj.post(222,data=setXqpublic_a(row=222,keyid='resource_id_16',pageurl='pageurl_10'),headers=getHeadersPublic_H5('pageurl_10'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,222)

    def test_108(self):
        '''购买会员批价下单'''
        time.sleep(5)
        r = self.obj.post(223,data=setBuyPublic_a(row=223,keyid='resource_id_16'),headers=getHeadersPublic_H5('pageurl_10'))
        #mylog.info('result：%s' % r.json())
        self.isContent(r,223)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_14',vlue1=r.json()['data']['coupon']['valid'][0]['cu_id'])

    def test_109(self):
        '''购买会员下单支付'''
        r = self.obj.post(224,data=setColumnPublic(row=224,keyid='resource_id_16'),headers=getHeadersPublic_H5('pageurl_10'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,224)

    def test_110(self):
        '''购买会员优惠券下单支付'''
        r = self.obj.post(225,data=setColumnPublic_c(row=225,keyid='resource_id_16',cuid='cu_id_14'),headers=getHeadersPublic_H5('pageurl_10'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,225)

    def test_111(self):
        '''新建训练营'''
        xx = "".join(random.sample('ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789', 6))
        dict1 = json.loads(OperationExcel().getRequestData(226))
        dict1['title'] = 'Pay_训练营' + xx
        r = self.obj.post(226,data=dict1,headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,226)
        writeDataYaml(key1='CampId',vlue1=r.json()['data']['id'])

    def test_112(self):
        '''新建免费训练营'''
        r = self.obj.post(227,data=setFreeCamp(),headers=getHeaderJson())
        mylog.info('result：%s' % r.json())
        self.isContent(r,227)

    def test_113(self):
        '''新建付费训练营'''
        r = self.obj.post(228,data=setFreeCamp_p(),headers=getHeaderJson())
        mylog.info('result：%s' % r.json())
        self.isContent(r,228)
        writeDataYaml(key1='term_id',vlue1=r.json()['data']['term_id'])

    def test_114(self):
        '''获取训练营营期列表'''
        r = self.obj.get(229,params=setFreeCamp_p0(),headers=getHeaderJson())
        mylog.info('result：%s' % r.json())
        self.isContent(r,229)
        writeDataYaml(key1='share_url',vlue1=r.json()['data']['terms'][0]['share_url'])
        writeDataYaml(key1='name10',vlue1=r.json()['data']['terms'][0]['title'])

    def test_115(self):
        '''C端进入购买训练营详情页'''
        r = self.obj.post(230,data=setFreeCamp_p1(),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,230)
        writeDataYaml(key1='resource_id_17',vlue1=r.json()['data']['available_info']['resource_id'])

    def test_116(self):
        '''购买训练营批价下单'''
        time.sleep(5)
        r = self.obj.post(231,data=setBuyPublic_a(row=231,keyid='resource_id_17'),headers=getHeadersInfo_H5())
        #mylog.info('result：%s' % r.json())
        self.isContent(r,231)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_15',vlue1=r.json()['data']['coupon']['valid'][0]['cu_id'])

    def test_117(self):
        '''购买训练营下单支付'''
        r = self.obj.post(232,data=setColumn_pub(row=232,keyid='resource_id_17'),headers=getHeadersPublic_H5('share_url'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,232)

    def test_118(self):
        '''购买训练营优惠券下单支付'''
        r = self.obj.post(233,data=setColumn_pub_c(row=233,keyid='resource_id_17',cuid='cu_id_15'),headers=getHeadersPublic_H5('share_url'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,233)

    def test_119(self):
        '''进入训练营课程目录'''
        r = self.obj.post(234,data=setFreeCamp_p3(),headers=getHeadersPublic_H5('share_url'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,234)
        writeDataYaml(key1='nodeId',vlue1=r.json()['data']['catalogue'][0]['id'])

    def test_120(self):
        '''确认营期配置是否课程'''
        r = self.obj.post(235, data=setFreeCamp_p4(), headers=getHeadersPublic_H5('share_url'))
        mylog.info('result：%s' % r.json())
        self.isContent(r, 235)

if __name__ == "__main__":
    unittest.main()
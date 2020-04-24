#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/10/30 14:38

import unittest
import re,urllib
import requests
from common import readExcel
from base.method import *
from page.xiaoe import *

class TestMarketBuy(unittest.TestCase):
    '''营销中心支付下单'''
    def setUp(self):
        self.excel = readExcel.OperationExcel()
        self.obj = Method()
        self.asser = IsContent()

    def requesData(self,row):
        return self.excel.getRequestData(row)

    def isContent(self, r, row):
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 0)
        self.assertTrue(self.asser.isContent(row=row,str1=r.text))

    def test_001(self):
        '''新建裂变海报图文'''
        r = self.obj.post(10,data=setNewgraphic01(row=10,title='Pay_裂变海报图文'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,10)

    def test_002(self):
        '''获取图文列表'''
        time.sleep(3)
        r = self.obj.method(11,data=self.requesData(11),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,11)
        writeDataYaml(key1='resource_id',vlue1=r.json()['data']['list'][0]['resource_id'])

    def test_003(self):
        '''创建裂变海报'''
        time.sleep(3)
        r = self.obj.post(12,data=setCreateFission(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,12)

    def test_004(self):
        '''购买裂变海报批价下单'''
        time.sleep(13)
        r = self.obj.post(13,data=setShopFission(),headers=getHeadersInfo_H5())
        self.isContent(r,13)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')

    def test_005(self):
        '''裂变海报下单支付'''
        r = self.obj.post(14,data=setJumpMode(),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,14)
        writeDataYaml(key1='pay_url',vlue1=r.json()['data']['pay_url'])

    def test_006(self):
        '''新建Pay_限时折扣图文'''
        r = self.obj.post(16,data=setNewgraphic01(row=16,title='Pay_限时折扣图文'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,16)

    def test_007(self):
        '''获取图文列表'''
        time.sleep(3)
        r = self.obj.method(17,data=self.requesData(17),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,17)
        writeDataYaml(key1='resource_id_1',vlue1=r.json()['data']['list'][0]['resource_id'])
        writeDataYaml(key1='name01',vlue1=r.json()['data']['list'][0]['title'])

    def test_008(self):
        '''新建限时折扣活动'''
        time.sleep(3)
        r = self.obj.post(18,data=setPromotion(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,18)

    def test_009(self):
        '''获取限时折扣列表'''
        time.sleep(5)
        r = self.obj.method(19,data=self.requesData(19),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,19)
        writeDataYaml(key1='activity_id',vlue1=r.json()['data']['list'][0]['activity_id'])

    def test_010(self):
        '''限时折扣批价下单'''
        time.sleep(5)
        r = self.obj.post(20,data=setShopPromotion(),headers=getHeadersInfo_H5())
        self.isContent(r,20)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')

    def test_011(self):
        '''限时折扣下单支付'''
        time.sleep(2)
        r = self.obj.post(21,data=setJumpMode_1(),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,14)

    def test_012(self):
        '''新建Pay_预约秒杀图文'''
        r = self.obj.post(23,data=setNewgraphic01(row=23,title='Pay_预约秒杀图文'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,23)

    def test_013(self):
        '''获取图文列表'''
        time.sleep(3)
        r = self.obj.method(24,params=self.requesData(24),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,24)
        writeDataYaml(key1='resource_id_2',vlue1=r.json()['data']['resourceList'][0]['id'])

    def test_014(self):
        '''新建秒杀预约活动'''
        time.sleep(1)
        r = self.obj.post(25,data=setSeckilling(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,25)
        writeDataYaml(key1='activity_id_1',vlue1=r.json()['data']['activity_id'])

    def test_015(self):
        '''预约秒杀活动'''
        r = self.obj.post(26,data=setMaatskill(),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,26)

    def test_016(self):
        '''预约后秒杀活动下单'''
        time.sleep(5)
        r = self.obj.post(27,data=setShopMaatskill(),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,27)

    def test_017(self):
        '''预约后秒杀活动下单支付'''
        r = self.obj.post(28,data=setJumpMode_2(),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,28)

    def test_018(self):
        '''新建秒杀图文'''
        r = self.obj.post(30,data=setNewgraphic01(row=30,title='Pay_秒杀图文'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,30)

    def test_019(self):
        '''获取图文列表'''
        r = self.obj.method(31,data=self.requesData(31),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,31)
        writeDataYaml(key1='resource_id_3', vlue1=r.json()['data']['list'][0]['resource_id'])
        writeDataYaml(key1='name02', vlue1=r.json()['data']['list'][0]['title'])

    def test_020(self):
        '''新建秒杀活动'''
        r = self.obj.post(32,data=setSale(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,32)
        writeDataYaml(key1='activity_id_2', vlue1=r.json()['data']['activity_id'])

    def test_021(self):
        '''秒杀活动下单'''
        time.sleep(5)
        r = self.obj.post(33,data=setShopSale(),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,33)

    def test_022(self):
        '''秒杀活动下单支付'''
        r = self.obj.post(34,data=setJumpMode_3(),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,34)

    def test_023(self):
        '''新建涨粉神器专栏'''
        r = self.obj.post(36,data=setNewColumn(row=36,title='Pay_涨粉神器专栏'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,36)

    def test_024(self):
        '''获取专栏列表'''
        time.sleep(3)
        r = self.obj.method(37,params=self.requesData(37),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,37)
        writeDataYaml(key1='package_id', vlue1=r.json()['data']['packageListInfo']['data'][0]['id'])
        writeDataYaml(key1='name03', vlue1=r.json()['data']['packageListInfo']['data'][0]['name'])
        writeDataYaml(key1='content_url',vlue1=r.json()['data']['packageListInfo']['data'][0]['content_url'])

    def test_025(self):
        '''获取活动商品专栏列表'''
        r = self.obj.method(38,data=self.requesData(38),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,38)

    def test_026(self):
        '''新建涨粉神器'''
        r = self.obj.post(39,data=setRoseArtifact(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,39)

    def test_027(self):
        '''获取涨粉神器列表'''
        time.sleep(3)
        r = self.obj.method(40,data=self.requesData(40),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,40)
        writeDataYaml(key1='activity_id_3',vlue1=r.json()['data']['activity_list'][0]['activity_id'])

    def test_028(self):
        '''生成涨粉神器海报'''
        r = self.obj.post(41,data=setArtifactPoster(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,41)

    def test_029(self):
        '''涨粉神器批价下单'''
        r = self.obj.post(42,data=setShopArtifact(),headers=getHeadersInfo_H5())
        self.isContent(r,42)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')

    def test_030(self):
        '''涨粉神器下单支付'''
        time.sleep(2)
        r = self.obj.post(43,data=setShopArtifact_a(),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,43)

    def test_031(self):
        '''涨粉神器优惠券批价下单'''
        time.sleep(2)
        r = self.obj.post(44,data=setShopArtifact_coupon(),headers=getHeadersInfo_H5())
        self.isContent(r,44)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_1',vlue1=r.json()['data']['coupon']['valid'][0]['cu_id'])

    def test_032(self):
        '''涨粉神器优惠券下单支付'''
        time.sleep(2)
        r = self.obj.post(45,data=setShopArtifact_coupon_a(),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,45)

    def test_033(self):
        '''查看涨粉神器专栏内容'''
        r = self.obj.post(46,data=setViewArtifact(),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,46)

    """def test_034(self):
        '''新建好友助力专栏-1'''
        r = self.obj.post(48, data=setNewColumn(row=48, title='Pay_好友助力专栏'), headers=getHeadersInfo())
        self.isContent(r,48)

    def test_035(self):
        '''获取专栏列表'''
        time.sleep(3)
        r = self.obj.method(49,params=self.requesData(49),headers=getHeadersInfo())
        self.isContent(r,49)
        writeDataYaml(key1='package_id_1', vlue1=r.json()['data']['packageListInfo']['data'][0]['id'])
        writeDataYaml(key1='name04', vlue1=r.json()['data']['packageListInfo']['data'][0]['name'])
        writeDataYaml(key1='content_url_1',vlue1=r.json()['data']['packageListInfo']['data'][0]['content_url'])

    def test_036(self):
        '''获取活动商品专栏列表'''
        r = self.obj.method(50,data=self.requesData(50),headers=getHeadersInfo())
        self.isContent(r,50)

    def test_037(self):
        '''新建好友助力活动-1'''
        time.sleep(3)
        r = self.obj.post(51,data=setNewFriends(),headers=getHeadersInfo())
        self.isContent(r,51)
        writeDataYaml(key1='activity_id_4',vlue1=r.json()['data']['activity_id'])

    def test_038(self):
        '''发起好友助力'''
        time.sleep(10)
        r = self.obj.post(52,data=setSponFriends(),headers=getHeadersInfo_H5())
        self.isContent(r,52)

    def test_039(self):
        '''给好友助力'''
        time.sleep(3)
        r = self.obj.post(53,data=setSponFriends_a(),headers=getHeadersInfo_H5_VIP())
        self.isContent(r,53)

    def test_040(self):
        '''获取好友助力详情'''
        r = self.obj.post(54,data=setSponFriends_b(),headers=getHeadersInfo_H5())
        print(r.json())
        self.isContent(r,54)

    def test_041(self):
        '''领取好友助力课程'''
        r = self.obj.post(55,data=setSponFriends_c(),headers=getHeadersInfo_H5())
        print(r.text)
        self.isContent(r,55)

    def test_042(self):
        '''查看好友助力专栏内容'''
        r = self.obj.post(56,data=setSponFriends_d(),headers=getHeadersInfo_H5())
        print(r.text)
        self.isContent(r,56)

    def test_043(self):
        '''新建好友助力专栏-2'''
        r = self.obj.post(57, data=setNewColumn(row=57, title='Pay_好友助力专栏'), headers=getHeadersInfo())
        self.isContent(r,57)

    def test_044(self):
        '''获取专栏列表'''
        time.sleep(3)
        r = self.obj.method(58,params=self.requesData(58),headers=getHeadersInfo())
        self.isContent(r,58)
        writeDataYaml(key1='package_id_2', vlue1=r.json()['data']['packageListInfo']['data'][0]['id'])
        writeDataYaml(key1='name05', vlue1=r.json()['data']['packageListInfo']['data'][0]['name'])
        writeDataYaml(key1='content_url_2',vlue1=r.json()['data']['packageListInfo']['data'][0]['content_url'])

    def test_045(self):
        '''获取活动商品专栏列表'''
        r = self.obj.method(59,data=self.requesData(59),headers=getHeadersInfo())
        self.isContent(r,59)

    def test_056(self):
        '''新建好友助力活动-2'''
        time.sleep(3)
        r = self.obj.post(60,data=setNewFriends(),headers=getHeadersInfo())
        self.isContent(r,60)
        writeDataYaml(key1='activity_id_5',vlue1=r.json()['data']['activity_id'])

    def test_057(self):
        '''好友助力批价下单'''
        r = self.obj.post(61,data=setShopFriends(),headers=getHeadersInfo_H5())
        self.isContent(r,61)

    def test_058(self):
        '''好友助力下单支付'''
        time.sleep(2)
        r = self.obj.post(62, data=setShopFriends_a(), headers=getHeadersInfo_H5())
        self.isContent(r, 62)

    def test_059(self):
        '''好友助力优惠券批价下单'''
        r = self.obj.post(63, data=setShopFriends_coupon(), headers=getHeadersInfo_H5())
        self.isContent(r, 63)
        writeDataYaml(key1='cu_id_2', vlue1=r.json()['data']['coupon']['valid'][0]['cu_id'])

    def test_060(self):
        '''好友助力优惠券下单支付'''
        time.sleep(2)
        r = self.obj.post(64, data=setShopFriends_coupon_a(), headers=getHeadersInfo_H5())
        self.isContent(r, 64)

    def test_061(self):
        '''查看好友助力专栏内容'''
        r = self.obj.post(65,data=setSponFriends_g(),headers=getHeadersInfo_H5())
        self.isContent(r,65)"""

    def test_062(self):
        '''新建拼团图文-1'''
        r = self.obj.post(67, data=setNewgraphic01(row=67, title='Pay_拼团图文'), headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r, 67)

    def test_063(self):
        '''获取图文列表'''
        time.sleep(3)
        r = self.obj.method(68,params=self.requesData(68),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,68)
        writeDataYaml(key1='resource_id_4',vlue1=r.json()['data']['resourceList'][0]['id'])
        writeDataYaml(key1='name06',vlue1=r.json()['data']['resourceList'][0]['title'])
        writeDataYaml(key1='content_url_3',vlue1=r.json()['data']['resourceList'][0]['pageUrl'])

    def test_064(self):
        '''创建拼团-1'''
        r = self.obj.post(69,data=setGroup(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,69)

    def test_065(self):
        '''获取拼团列表'''
        time.sleep(10)
        r = self.obj.method(70,data=self.requesData(70),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,70)
        writeDataYaml(key1='team_buy_id',vlue1=r.json()['data'][0]['team_buy_id'])

    def test_066(self):
        '''团长发起拼团'''
        r = self.obj.post(71,headers=getHeadersGroup_head())
        self.assertEqual(r.json()['msg'],'\u7528\u6237\u5df2\u7ed1\u5b9a\u89d2\u8272\u8eab\u4efd')

    def test_068(self):
        '''团长拼团下单支付'''
        time.sleep(60)
        r = self.obj.post(73,data=setShopGroup_head_a(),headers=getHeadersGroup_head())
        mylog.info('result：%s' % r.json())
        self.isContent(r,73)

    def test_069(self):
        '''团长查看拼团详情'''
        time.sleep(3)
        r = self.obj.post(74,data=setShopGroup_head_a1(),headers=getHeadersGroup_head())
        mylog.info('result：%s' % r.json())
        self.isContent(r,74)
        writeDataYaml(key1='task_id',vlue1=r.json()['data']['marketing_activity']['marketing_info']['6']['task_id'])

    def test_070(self):
        '''团员参与拼团'''
        r = self.obj.post(75,data=setShopGroup_member(),headers=getHeadersGroup_member())
        mylog.info('result：%s' % r.json())
        self.isContent(r,75)

    def test_071(self):
        '''团员拼团下单支付'''
        r = self.obj.post(76,data=setShopGroup_member_a(),headers=getHeadersGroup_member())
        mylog.info('result：%s' % r.json())
        self.isContent(r,76)

    def test_072(self):
        '''新建拼团图文-2'''
        r = self.obj.post(77, data=setNewgraphic01(row=77, title='Pay_拼团图文'), headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r, 77)

    def test_073(self):
        '''获取图文列表'''
        time.sleep(3)
        r = self.obj.method(78,params=self.requesData(78),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,78)
        writeDataYaml(key1='resource_id_5',vlue1=r.json()['data']['resourceList'][0]['id'])
        writeDataYaml(key1='name07',vlue1=r.json()['data']['resourceList'][0]['title'])
        writeDataYaml(key1='content_url_4',vlue1=r.json()['data']['resourceList'][0]['pageUrl'])

    def test_074(self):
        '''创建拼团-2'''
        r = self.obj.post(79,data=setGroup_coupon(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,79)

    def test_075(self):
        '''查看拼团详情'''
        time.sleep(3)
        r = self.obj.post(80,data=setGroup_coupon_1(),headers=getHeadersGroup_head())
        mylog.info('result：%s' % r.json())
        self.isContent(r,80)

    def test_076(self):
        '''拼团原价批价下单'''
        r = self.obj.post(81,data=setShopGroup_coupon(),headers=getHeadersInfo_H5())
        self.isContent(r,81)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')

    def test_077(self):
        '''拼团原价下单支付'''
        r = self.obj.post(82,data=setShopGroup_coupon_1(),headers=getHeadersGroup_head())
        mylog.info('result：%s' % r.json())
        self.isContent(r,82)

    def test_078(self):
        '''拼团原价优惠券批价下单'''
        r = self.obj.post(83,data=setShopGroup_coupon_2(),headers=getHeadersGroup_head())
        self.isContent(r,83)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='cu_id_2',vlue1=r.json()['data']['optimal_coupon']['cu_id'])

    def test_079(self):
        '''拼团原价优惠券下单支付'''
        time.sleep(5)
        r = self.obj.post(84,data=setShopGroup_coupon_3(),headers=getHeadersGroup_head())
        mylog.info('result：%s' % r.json())
        self.isContent(r,84)

    def test_080(self):
        '''查看拼团原价图文内容'''
        r = self.obj.post(85,data=setShopGroup_coupon_4(),headers=getHeadersGroup_head())
        mylog.info('result：%s' % r.json())
        self.isContent(r,85)

    def test_081(self):
        '''新建推广员图文'''
        r = self.obj.post(87, data=setNewgraphic01(row=87, title='Pay_推广员图文'), headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r, 87)
        writeDataYaml(key1='resource_id_6',vlue1=r.json()['data']['resource_id'])

    def test_082(self):
        '''更新推广员邀请比例'''
        time.sleep(3)
        r = self.obj.post(88,data=setPromoter(),headers=getHeaderPromoter_b())
        mylog.info('result：%s' % r.json())
        self.isContent(r,88)

    def test_083(self):
        '''推广员下级批价下单'''
        time.sleep(3)
        r = self.obj.post(89,data=setShopPromoter(),headers=getHeaderPromoter_h5())
        #mylog.info('result：%s' % r.json())
        self.isContent(r,89)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')

    def test_084(self):
        '''推广员下级下单支付'''
        time.sleep(3)
        r = self.obj.post(90,data=setShopPromoter_1(),headers=getHeaderPromoter_h5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,90)

    def test_085(self):
        '''创建优惠券'''
        r = self.obj.post(91,data=setCreateCoupon(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,91)

    def test_086(self):
        '''获取优惠劵列表'''
        r = self.obj.post(92,data=self.requesData(92),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,92)
        writeDataYaml(key1='cou_id',vlue1=r.json()['data']['list'][0]['id'])

    def test_087(self):
        '''用户领取优惠券'''
        time.sleep(3)
        r = self.obj.post(93,data=setReceiveCoupon(),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,93)

    def test_088(self):
        '''新建邀请码图文'''
        r = self.obj.post(94, data=setNewgraphic01(row=94, title='Pay_邀请码图文'), headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r, 94)

    def test_089(self):
        '''获取图文列表'''
        time.sleep(3)
        r = self.obj.method(95,params=self.requesData(95),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,95)
        writeDataYaml(key1='resource_id_7',vlue1=r.json()['data']['resourceList'][0]['id'])
        writeDataYaml(key1='name08',vlue1=r.json()['data']['resourceList'][0]['title'])
        writeDataYaml(key1='content_url_5',vlue1=r.json()['data']['resourceList'][0]['pageUrl'])

    def test_090(self):
        '''新建邀请码'''
        r = self.obj.post(96,data=setRequestCode(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.assertTrue(self.asser.isContent(row=96, str1=r.text))

    def test_091(self):
        '''获取邀请码列表'''
        time.sleep(2)
        r = self.obj.post(97,data=self.requesData(97),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,97)
        writeDataYaml(key1='bid',vlue1=r.json()['data']['list'][0]['id'])

    def test_092(self):
        '''获取邀请码使用记录列表'''
        r = self.obj.post(98,data=setRequestCode1(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.assertEqual(r.json()['code'],0)
        writeDataYaml(key1='yqm_id', vlue1=r.json()['data']['list'][0]['code'])

    def test_093(self):
        '''使用邀请码'''
        r = self.obj.post(99,data=setRequestCode_u(),headers=getHeaderPromoter_h5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,99)

    def test_094(self):
        '''获取使用邀请码状态'''
        time.sleep(2)
        r = self.obj.post(100,data=setRequestCode_u1(),headers=getHeaderPromoter_h5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,100)

    def test_095(self):
        '''获取邀请码微信群发送图片'''
        url = OperationExcel().getUrl(101)%getRead(key1='bid')
        r = requests.get(url,headers=getHeadersInfo(),verify=False)

    def test_096(self):
        '''下载邀请码_非office2003'''
        r = self.obj.post(102,data=setRequestCode_u2(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,102)

    def test_097(self):
        '''下载邀请码_office2003'''
        r = self.obj.post(103,data=setRequestCode_u3(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,103)

    def test_098(self):
        '''查看邀请码图文内容'''
        r = self.obj.post(104,data=urllib.parse.urlencode(setRequestCode_u4()).encode(encoding='UTF8'),headers=getHeaderPromoter_h5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,104)

    def test_099(self):
        '''新建兑换码图文'''
        r = self.obj.post(106, data=setNewgraphic01(row=106, title='Pay_兑换码图文'), headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r, 106)

    def test_100(self):
        '''获取图文列表'''
        time.sleep(3)
        r = self.obj.method(107,params=self.requesData(107),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,107)
        writeDataYaml(key1='resource_id_8',vlue1=r.json()['data']['resourceList'][0]['id'])
        writeDataYaml(key1='name09',vlue1=r.json()['data']['resourceList'][0]['title'])
        writeDataYaml(key1='content_url_6',vlue1=r.json()['data']['resourceList'][0]['pageUrl'])

    def test_101(self):
        '''新建兑换码'''
        r = self.obj.post(108,data=setCDkey(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,108)

    def test_102(self):
        '''获取兑换码列表'''
        r = self.obj.get(109,params=self.requesData(109),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,109)
        writeDataYaml(key1='batch_id',vlue1=r.json()['data']['data'][0]['batch_id'])
        writeDataYaml(key1='activity_id_5',vlue1=r.json()['data']['data'][0]['activity_id'])

    def test_103(self):
        '''获取兑换码使用记录列表'''
        r = self.obj.get(110,params=setCDkey_u(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,110)
        writeDataYaml(key1='redeem_code',vlue1=r.json()['data']['code_list'][0]['redeem_code'])

    def test_104(self):
        '''进入兑换码页面'''
        r = self.obj.post(111,data=setCDkey_u1(),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,111)

    def test_105(self):
        '''使用兑换码'''
        time.sleep(5)
        r = self.obj.post(112,data=setCDkey_u2(),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,112)

    def test_106(self):
        '''获取使用兑换码列表'''
        r = self.obj.method(113,data=self.requesData(113),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,113)

    def test_107(self):
        '''查看兑换码图文内容'''
        r = self.obj.post(114,data=setCDkey_u3(),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,114)

if __name__ == "__main__":
    unittest.main(verbosity=2)
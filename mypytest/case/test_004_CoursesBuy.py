#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/12/11 18:13

import pytest
import re,urllib,json
import requests
from common.readJson import OperationJson
from base.method import *
from page.xiaoe import *
import allure

@allure.feature("03、在线课程管理模块")
class TestCoursesBuy:
    obj = Method()
    asser = IsContent()
    jsda = OperationJson()

    def isContent(self, r, row):
        assert r.status_code == 200
        assert r.json()['code'] == 0
        assert self.asser.isContent(row=row,str1=r.text)

    def test_001(self):
        '''B端新建图文'''
        r = self.obj.web_post(8,data=setNewGraphic(row=8,title='Pay_新建图文'),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,8)
        writeDataYaml(key1='dw_resource_id',vlue1=r.json()['data']['resource_id'])

    def test_002(self):
        '''获取B端图文列表'''
        r = self.obj.web_get(9,params=self.jsda.getRequestsData(9),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,9)
        writeDataYaml(key1='dw_content_url',vlue1=r.json()['data']['resourceList'][0]['pageUrl'])

    def test_003(self):
        '''C端进入图文详情页'''
        r = self.obj.h5_post(10,data=setXqpublic(row=10,keyid='dw_resource_id',pageurl='dw_content_url'),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,10)

    def test_004(self):
        '''购买图文批价下单'''
        time.sleep(5)
        r = self.obj.h5_post(11,data=setBuyPublic(row=11,keyid='dw_resource_id'),headers=getHeadersInfo_H5())
        self.isContent(r,11)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')
        writeDataYaml(key1='dw_cu_id',vlue1=r.json()['data']['coupon']['valid'][0]['cu_id'])

    def test_005(self):
        '''购买图文下单支付'''
        r = self.obj.h5_post(12,data=setBuyPublic(row=12,keyid='dw_resource_id'),headers=getHeadersPublic_H5('dw_content_url'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,12)

    def test_006(self):
        '''购买图文优惠券下单支付'''
        r = self.obj.h5_post(13,data=setCouponPublic(row=13,keyid='dw_resource_id',cuid='dw_cu_id'),headers=getHeadersPublic_H5('dw_content_url'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,13)

    def test_007(self):
        '''购买后确认图文内容'''
        r = self.obj.h5_post(14,data=setXqpublic(row=14,keyid='dw_resource_id',pageurl='dw_content_url'),headers=getHeadersPublic_H5('dw_content_url'))
        mylog.info('result：%s' % r.json())
        self.isContent(r,14)

if __name__ == '__main__':
    pytest.main(['-s','-v','test_004_CoursesBuy.py::TestCoursesBuy'])

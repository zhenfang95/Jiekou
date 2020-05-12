#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/10/30 14:38

import pytest
from base.method import *
from page.xiaoe import *
import allure

@allure.feature("02、营销中心模块002")
class TestMarketBuy:
    jsda = OperationJson()
    obj = Method()
    asser = IsContent()

    def isContent(self, r, row):
        assert r.status_code == 200
        assert r.json()['code'] == 0
        assert self.asser.isContent(row=row,str1=r.text)

    def test_001(self):
        '''新建裂变海报图文'''
        r = self.obj.web_post(row=3,data=setNewGraphic(row=3,title='Pay_裂变海报图文'),headers=getHeadersInfo())
        ## mylog.info('result：%s' % r.json())
        self.isContent(r,3)

    def test_002(self):
        '''获取图文列表'''
        time.sleep(3)
        r = self.obj.web_get(row=4,params=self.jsda.getRequestsData(4),headers=getHeadersInfo())
        print(r.text)
        #mylog.info('result：%s' % r.json())
        self.isContent(r,4)
        writeDataYaml(key1='resource_id',vlue1=r.json()['data']['resourceList'][0]['id'])

    def test_003(self):
        '''创建裂变海报'''
        time.sleep(3)
        r = self.obj.web_post(row=5,data=setCreateFission(),headers=getHeadersInfo())
        mylog.info('result：%s' % r.json())
        self.isContent(r,5)

    def test_004(self):
        '''购买裂变海报批价下单'''
        time.sleep(5)
        r = self.obj.h5_post(row=6,data=setShopFission(),headers=getHeadersInfo_H5())
        self.isContent(r,6)
        mylog.info('result：PASS--响应数据过多，结果暂不打印')

    def test_005(self):
        '''裂变海报下单支付'''
        r = self.obj.h5_post(row=7,data=setJumpMode(),headers=getHeadersInfo_H5())
        mylog.info('result：%s' % r.json())
        self.isContent(r,7)

if __name__ == '__main__':
    pytest.main(['-s','-v','test_003_MarketBuy.py::TestMarketBuy'])

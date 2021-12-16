#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @time:2020/8/27 14:30

import pytest,allure,requests
from common.readExcel import OperationExcel
from common import readYaml,readMySQL
from common.reData import *
from page.CB_requestData import *
from common.rsa_sign import *
from common.logs import *

ml = OperationExcel('CB')
yl = readYaml
db = readMySQL

headers = {"Content-Type":"application/json"}

@allure.feature('03、供城巴接口')   #在报告中添加用例标题
class TestCB:
    @allure.story('1、AR数据下载接口')
    @pytest.mark.parametrize('row,name',CB_arData,ids=CB_arDataName)   #ids是增加用例标题
    def test_01_arData(self,row,name):
        '''AR数据下载接口'''
        mylog.info('执行测试用例[%s],url=%s'%(name,yl.getFixedData(key1='CB_arData_url')))
        # 请求参数加签
        sign_data = tng_signdata_rsa(yl.getFixedData(key1='rsa_private_key'),getTestdata_CB(row))
        mylog.info('请求值:[%s]'%sign_data)
        r = requests.post(url=yl.getFixedData(key1='CB_arData_url'),data=sign_data,headers=headers)
        mylog.info('返回值:[%s]'%r.json())
        assert ml.getExpect(row) in r.text
        mylog.info('Result: PASS，文本检查点：%s'%ml.getExpect(row))

    @allure.story('2、城巴交易数据下载')
    @pytest.mark.parametrize('row,name',CB_txnDownload,ids=CB_txnDownloadName)   #ids是增加用例标题
    def test_02_txnDownload(self,row,name):
        '''城巴交易数据下载'''
        mylog.info('执行测试用例[%s],url=%s'%(name,yl.getFixedData(key1='CB_txnDownload_url')))
        # 请求参数加签
        sign_data = tng_signdata_rsa(yl.getFixedData(key1='rsa_private_key'),getTestdata_CB(row))
        mylog.info('请求值:[%s]'%sign_data)
        r = requests.post(url=yl.getFixedData(key1='CB_txnDownload_url'),data=sign_data,headers=headers)
        mylog.info('返回值:[%s]'%r.json())
        assert ml.getExpect(row) in r.text
        mylog.info('Result: PASS，文本检查点：%s'%ml.getExpect(row))

    @allure.story('3、城巴订单退款')
    @pytest.mark.parametrize('row,name',CB_refund,ids=CB_refundName)   #ids是增加用例标题
    def test_03_refund(self,row,name):
        '''城巴订单退款'''
        mylog.info('执行测试用例[%s],url=%s'%(name,yl.getFixedData(key1='CB_refund_url')))
        # 请求参数加签
        sign_data = tng_signdata_rsa(yl.getFixedData(key1='rsa_private_key'),getTestdata_CB(row))
        mylog.info('请求值:[%s]'%sign_data)
        r = requests.post(url=yl.getFixedData(key1='CB_refund_url'),data=sign_data,headers=headers)
        mylog.info('返回值:[%s]'%r.json())
        assert ml.getExpect(row) in r.text
        mylog.info('Result: PASS，文本检查点：%s'%ml.getExpect(row))

if __name__ == '__main__':
    pytest.main(['-s','-v','test_003_CB.py::TestCB'])
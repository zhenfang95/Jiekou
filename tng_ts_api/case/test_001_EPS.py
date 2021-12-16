#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @time:2020/8/27 17:07

import pytest,allure,requests
from common.readExcel import OperationExcel
from common import readYaml,readMySQL
from common.reData import *
from page.EPS_requestData import *
from common.rsa_sign import *
from common.logs import *

ml = OperationExcel('EPS')
yl = readYaml
db = readMySQL

headers = {"Content-Type":"application/json"}

@allure.feature('01、供德卡EPS接口')   #在报告中添加用例标题
class TestEPS:
    @allure.story('1、获取乘车码公钥')
    @pytest.mark.parametrize('row,name',EPS_getPublicKey,ids=EPS_getPublicKeyName)   #ids是增加用例标题
    def test_01_getPublicKey(self,report_del,row,name):
        '''获取乘车码公钥'''
        mylog.info('执行测试用例[%s],url=%s'%(name,yl.getFixedData(key1='EPS_getPublicKey_url')))
        # 请求参数加签
        sign_data = tng_signdata_rsa(yl.getFixedData(key1='rsa_private_key'),getTestdata_EPS(row))
        mylog.info('请求值:[%s]'%sign_data)
        r = requests.post(url=yl.getFixedData(key1='EPS_getPublicKey_url'),data=sign_data,headers=headers)
        mylog.info('返回值:[%s]'%r.json())
        assert ml.getExpect(row) in r.text
        mylog.info('Result: PASS，文本检查点：%s'%ml.getExpect(row))

    @allure.story('2、获取CAPK和AID数据查询')
    @pytest.mark.parametrize('row,name',EPS_getTapCardKey,ids=EPS_getTapCardKeyName)   #ids是增加用例标题
    def test_02_getTapCardKey(self,row,name):
        '''获取CAPK和AID数据查询'''
        mylog.info('执行测试用例[%s],url=%s'%(name,yl.getFixedData(key1='EPS_getTapCardKey_url')))
        # 请求参数加签
        sign_data = tng_signdata_rsa(yl.getFixedData(key1='rsa_private_key'),getTestdata_EPS(row))
        mylog.info('请求值:[%s]'%sign_data)
        r = requests.post(url=yl.getFixedData(key1='EPS_getTapCardKey_url'),data=sign_data,headers=headers)
        mylog.info('返回值:[%s]'%r.json())
        assert ml.getExpect(row) in r.text
        mylog.info('Result: PASS，文本检查点：%s'%ml.getExpect(row))

    @allure.story('3、AR汇总数据上传')
    @pytest.mark.parametrize('row,name',EPS_arSummaryUpload,ids=EPS_arSummaryUploadName)   #ids是增加用例标题
    def test_03_getTapCardKey(self,row,name):
        '''AR汇总数据上传'''
        mylog.info('执行测试用例[%s],url=%s'%(name,yl.getFixedData(key1='EPS_arSummaryUpload_url')))
        # 请求参数加签
        sign_data = tng_signdata_rsa(yl.getFixedData(key1='rsa_private_key'),getTestdata_EPS(row))
        mylog.info('请求值:[%s]'%sign_data)
        r = requests.post(url=yl.getFixedData(key1='EPS_arSummaryUpload_url'),data=sign_data,headers=headers)
        mylog.info('返回值:[%s]'%r.json())
        assert ml.getExpect(row) in r.text
        mylog.info('Result: PASS，文本检查点：%s'%ml.getExpect(row))

    @allure.story('4、设备事件日志上传')
    @pytest.mark.parametrize('row,name',EPS_eventLogs,ids=EPS_eventLogsName)   #ids是增加用例标题
    def test_04_eventLogs(self,row,name):
        '''设备事件日志上传'''
        mylog.info('执行测试用例[%s],url=%s'%(name,yl.getFixedData(key1='EPS_eventLogs_url')))
        # 请求参数加签
        sign_data = tng_signdata_rsa_List(yl.getFixedData(key1='rsa_private_key'),getTestdata_EPS(row),'logsList')
        mylog.info('请求值:[%s]'%sign_data)
        r = requests.post(url=yl.getFixedData(key1='EPS_eventLogs_url'),data=sign_data,headers=headers)
        mylog.info('返回值:[%s]'%r.json())
        assert ml.getExpect(row) in r.text
        mylog.info('Result: PASS，文本检查点：%s'%ml.getExpect(row))

if __name__ == '__main__':
    pytest.main(['-s','-v','test_001_EPS.py::TestEPS'])
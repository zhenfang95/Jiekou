#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/8/11 16:34

import shutil,os
import pytest,allure,requests,json
from common.readExcel import OperationExcel
from common import readYaml,readMySQL
from common.reData import *
from page.FCS_requestData import *
from common.rsa_sign import *
from common.logs import *

ml = OperationExcel('FCS')
yl = readYaml
db = readMySQL

headers = {"Content-Type":"application/json"}

@allure.feature('02、FCS计费系统接口')   #在报告中添加用例标题
class TestFCS:
    @allure.story('1、行程交易订单获取接口')
    @pytest.mark.parametrize('row,name',FCS_txnGet,ids=FCStxnGetName)   #ids是增加用例标题
    def test_01_txnGet(self,row,name):
        '''FCS行程交易订单获取接口'''
        mylog.info('执行测试用例[%s],url=%s'%(name,yl.getFixedData(key1='FCS_txnGet_url')))
        # 请求参数加签
        sign_data = tng_signdata_rsa(yl.getFixedData(key1='rsa_private_key'),getTestdata_FCS(row))
        mylog.info('请求值:[%s]'%sign_data)
        r = requests.post(url=yl.getFixedData(key1='FCS_txnGet_url'),data=sign_data,headers=headers)
        mylog.info('返回值:[%s]'%r.json())
        if ml.getRequestData(row) == '{"正确参数":"正确参数请求"}':
            assert ml.getExpect(row) in r.text
            mylog.info('Result: PASS，文本检查点：%s'%ml.getExpect(row))
            try:
                txnid = db.Mysql("select txn_id from tra_trip_order where txn_type = 1 and status = 1 and mch_id = 10645")
                yl.writeDataYaml(key1='txnId_1', vlue1=txnid[0]['txn_id'])
                yl.writeDataYaml(key1='txnId_2', vlue1=txnid[1]['txn_id'])
                yl.writeDataYaml(key1='txnId_3', vlue1=txnid[2]['txn_id'])
                yl.writeDataYaml(key1='txnId_4', vlue1=txnid[3]['txn_id'])
                yl.writeDataYaml(key1='txnId_5', vlue1=txnid[4]['txn_id'])
                mylog.info('获取交易行程订单号:\ntxn_id_1={0}\ntxn_id_2={1}\ntxn_id_3={2}\ntxn_id_4={3}\ntxn_id_5={4}'.format(txnid[0]['txn_id'],txnid[1]['txn_id'],txnid[2]['txn_id'],txnid[3]['txn_id'],txnid[4]['txn_id']))
            except Exception as e:
                mylog.error('获取行程订单号失败，mysql中没有符合条件的行程订单号->%s'%e)
        else:
            assert ml.getExpect(row) in r.text
            mylog.info('Result: PASS，文本检查点：%s'%ml.getExpect(row))

    @allure.story('2、设置行程订单金额接口')
    @pytest.mark.parametrize('row,name',FCS_setFare,ids=FCSsetFareName)
    def test_02_setFare(self,row,name):
        '''FCS设置行程订单金额接口'''
        if name == '行程分段收费模式--返利' or name == '设置行程订单-分段收费模式':
            time.sleep(10)
        mylog.info('执行测试用例[%s],url=%s'%(name,yl.getFixedData(key1='FCS_setFare_url')))
        # 请求参数加签
        sign_data = tng_signdata_rsa_List(yl.getFixedData(key1='rsa_private_key'),getTestdata_FCS(row),'txnList')
        mylog.info('请求值:[%s]' % sign_data)
        r = requests.post(url=yl.getFixedData(key1='FCS_setFare_url'), data=sign_data, headers=headers)
        mylog.info('返回值:[%s]' % r.json())
        assert ml.getExpect(row) in r.text
        mylog.info('Result: PASS，文本检查点：%s' % ml.getExpect(row))

    @allure.story('3、FCS票价调整接口')
    @pytest.mark.parametrize('row,name',FCS_adjustFare,ids=FCSadjustFareName)
    def test_03_adjustFare(self,row,name):
        '''FCS票价调整接口'''
        if ml.getRequestData(row) == '{"正确参数":"正确参数请求"}':
            time.sleep(15)
        mylog.info('执行测试用例[%s],url=%s'%(name,yl.getFixedData(key1='FCS_adjustFare_url')))
        # 请求参数加签
        sign_data = tng_signdata_rsa_List(yl.getFixedData(key1='rsa_private_key'),getTestdata_FCS(row),'txnList')
        mylog.info('请求值:[%s]' % sign_data)
        r = requests.post(url=yl.getFixedData(key1='FCS_adjustFare_url'), data=sign_data, headers=headers)
        mylog.info('返回值:[%s]' % r.json())
        assert ml.getExpect(row) in r.text
        mylog.info('Result: PASS，文本检查点：%s' % ml.getExpect(row))

    @allure.story('4、FCS日结数据查询接口')
    @pytest.mark.parametrize('row,name',FCS_settlementSummary,ids=FCS_settlementSummaryName)
    def test_04_settlementSummary(self,row,name):
        '''FCS日结数据查询接口'''
        mylog.info('执行测试用例[%s],url=%s'%(name,yl.getFixedData(key1='FCS_settlementSummary_url')))
        # 请求参数加签
        sign_data = tng_signdata_rsa(yl.getFixedData(key1='rsa_private_key'),getTestdata_FCS(row))
        mylog.info('请求值:[%s]' % sign_data)
        r = requests.post(url=yl.getFixedData(key1='FCS_settlementSummary_url'), data=sign_data, headers=headers)
        mylog.info('返回值:[%s]' % r.json())
        assert ml.getExpect(row) in r.text
        mylog.info('Result: PASS，文本检查点：%s' % ml.getExpect(row))

    @allure.story('5、FCS设备事件日志查询接口')
    @pytest.mark.parametrize('row,name',FCS_eventsLog,ids=FCS_eventsLogName)
    def test_05_eventsLog(self,row,name):
        '''FCS设备事件日志查询接口'''
        mylog.info('执行测试用例[%s],url=%s'%(name,yl.getFixedData(key1='FCS_eventsLog_url')))
        # 请求参数加签
        sign_data = tng_signdata_rsa(yl.getFixedData(key1='rsa_private_key'),getTestdata_FCS(row))
        mylog.info('请求值:[%s]' % sign_data)
        r = requests.post(url=yl.getFixedData(key1='FCS_eventsLog_url'), data=sign_data, headers=headers)
        mylog.info('返回值:[%s]' % r.json())
        assert ml.getExpect(row) in r.text
        mylog.info('Result: PASS，文本检查点：%s' % ml.getExpect(row))

if __name__ == '__main__':
    pytest.main(['-s','-v','test_002_FCS.py::TestFCS'])

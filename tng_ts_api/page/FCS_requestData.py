#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/8/12 16:56

import json,time
from common.readExcel import OperationExcel
from common import readYaml
from common.reData import *

ml = OperationExcel("FCS")
yl = readYaml

def getTestdata_FCS(row):
    #处理请求参数
    case_data = json.loads(ml.getRequestData(row))
    case_key=list(case_data.keys())[0]
    if ml.getCaseType(row) == 'A':
        request_data = yl.getFixedData(key1='requestData_txnGet')
        if case_key == '正确参数':
            pass
        elif case_key == 'traceNum':
            request_data['traceNum'] = case_data['traceNum']
        elif case_key == 'numPassId':
            request_data['numPassId'] = case_data['numPassId']
        else:
            print('/txnGet接口请求参数错误，请检查测试用例')

    elif ml.getCaseType(row) == 'B':
        request_data = yl.getFixedData(key1='requestData_setFare')
        request_data['txnList'][0]['txnId'] = yl.getRelyData(key1='txnId_1')
        if case_key == '正确参数':
            pass
        elif case_key == '分段收费':
            request_data['txnList'][0]['fareType'] = 'Possible_rebate'
            request_data['txnList'][0]['txnId'] = yl.getRelyData(key1='txnId_2')
        elif case_key == '返利':
            request_data['txnList'][0]['txnId'] = yl.getRelyData(key1='txnId_3')
            request_data['txnList'][0]['originalTxnId'] = yl.getRelyData(key1='txnId_2')
            request_data['txnList'][0]['fareType'] = 'Possible_rebate'
            request_data['txnList'][0]['busFare'] = '-10'
        elif case_key == 'traceNum':
            request_data['traceNum'] = case_data['traceNum']
        elif case_key == 'numTxn':
            request_data['numTxn'] = case_data['numTxn']
        elif case_key == 'busFare':
            request_data['txnList'][0]['busFare'] = case_data['busFare']
            if case_data['busFare'] == 0:
                request_data['txnList'][0]['txnId'] = yl.getRelyData(key1='txnId_4')
        elif case_key == 'busFare_fenduan':
            request_data['txnList'][0]['fareType'] = 'Possible_rebate'
            request_data['txnList'][0]['busFare'] = case_data['busFare_fenduan']
            if case_data['busFare_fenduan'] == 0:
                request_data['txnList'][0]['txnId'] = yl.getRelyData(key1='txnId_5')
        elif case_key == 'calTime':
            request_data['txnList'][0]['calTime'] = case_data['calTime']
        elif case_key == 'fareType':
            request_data['txnList'][0]['fareType'] = case_data['fareType']
        elif case_key == 'txnId':
            request_data['txnList'][0]['txnId'] = case_data['txnId']
        elif case_key == 'originalTxnId':
            request_data['txnList'][0]['originalTxnId'] = case_data['originalTxnId']
        else:
            print('/setFare接口请求参数错误，请检查测试用例')

    elif ml.getCaseType(row) == 'C':
        request_data = yl.getFixedData(key1='requestData_adjustFare')
        request_data['txnList'][0]['adjustTxnId'] = str(int(time.time()))
        request_data['txnList'][0]['txnId'] = yl.getRelyData(key1='txnId_1')
        if case_key == '正确参数':
            pass
        elif case_key == 'traceNum':
            request_data['traceNum'] = case_data['traceNum']
        elif case_key == 'numTxn':
            request_data['numTxn'] = case_data['numTxn']
        elif case_key == 'adjustTxnId':
            request_data['txnList'][0]['adjustTxnId'] = case_data['adjustTxnId']
        elif case_key == 'txnAmt':
            request_data['txnList'][0]['txnAmt'] = case_data['txnAmt']
        elif case_key == 'txnId':
            request_data['txnList'][0]['txnId'] = case_data['txnId']
        else:
            print('/adjustFare接口请求参数错误，请检查测试用例')

    elif ml.getCaseType(row) == 'D':
        request_data = yl.getFixedData(key1='requestData_settlementSummary')
        if case_key == '正确参数':
            pass
        elif case_key == 'beginTime':
            request_data['beginTime'] = case_data['beginTime']
        elif case_key == 'endTime':
            request_data['endTime'] = case_data['endTime']
        elif case_key == 'deviceId':
            request_data['deviceId'] = case_data['deviceId']
        elif case_key == 'pspId':
            request_data['pspId'] = case_data['pspId']
        elif case_key == 'businessDate':
            request_data['businessDate'] = case_data['businessDate']
        else:
            print('/settlementSummary接口请求参数错误，请检查测试用例')

    elif ml.getCaseType(row) == 'E':
        request_data = yl.getFixedData(key1='requestData_eventsLog')
        if case_key == '正确参数':
            pass
        elif case_key == 'beginTime':
            request_data['beginTime'] = case_data['beginTime']
        elif case_key == 'endTime':
            request_data['endTime'] = case_data['endTime']
        elif case_key == 'deviceId':
            request_data['deviceId'] = case_data['deviceId']
        elif case_key == 'logId':
            request_data['logId'] = case_data['logId']
        elif case_key == 'logType':
            request_data['logType'] = case_data['logType']
        elif case_key == 'pageNum':
            request_data['pageNum'] = case_data['pageNum']
        elif case_key == 'pageSize':
            request_data['pageSize'] = case_data['pageSize']
        elif case_key == 'businessDate':
            request_data['businessDate'] = case_data['businessDate']
        else:
            print('/eventsLog接口请求参数错误，请检查测试用例')
    else:
        print('哈哈哈……')
    return request_data

#print(getTestdata_FCS(10))


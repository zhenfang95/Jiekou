#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @time:2020/8/27 14:35

import json,time
from common.readExcel import OperationExcel
from common import readYaml
from common.reData import *

execl = OperationExcel("CB")
yl = readYaml

def getTestdata_CB(row):
    #global request_data
    case_data = json.loads(execl.getRequestData(row))
    case_key=list(case_data.keys())[0]
    if execl.getCaseType(row) == 'A':
        request_data = yl.getFixedData(key1='requestData_arData')
        if case_key == '正确参数':
            pass
        elif case_key == 'deviceId':
            request_data['deviceId'] = case_data['deviceId']
        elif case_key == 'beginTime':
            request_data['beginTime'] = case_data['beginTime']
        elif case_key == 'endTime':
            request_data['endTime'] = case_data['endTime']
        else:
            print('/arData接口请求参数错误，请检查测试用例')
    elif execl.getCaseType(row) == 'B':
        request_data = yl.getFixedData(key1='requestData_txnDownload')
        if case_key == '正确参数':
            pass
        elif case_key == 'deviceId':
            request_data['deviceId'] = case_data['deviceId']
        elif case_key == 'beginTime':
            request_data['beginTime'] = case_data['beginTime']
        elif case_key == 'endTime':
            request_data['endTime'] = case_data['endTime']
        elif case_key == 'timeType':
            request_data['timeType'] = case_data['timeType']
        elif case_key == 'status':
            request_data['status'] = case_data['status']
        elif case_key == 'pspId':
            request_data['pspId'] = case_data['pspId']
        elif case_key == 'settleStatus':
            request_data['settleStatus'] = case_data['settleStatus']
        elif case_key == 'pageNum':
            request_data['pageNum'] = case_data['pageNum']
        elif case_key == 'pageSize':
            request_data['pageSize'] = case_data['pageSize']
        else:
            print('/txnDownload接口请求参数错误，请检查测试用例')
    elif execl.getCaseType(row) == 'C':
        request_data = yl.getFixedData(key1='requestData_refund')
        request_data['rtxnId'] = str(int(time.time()))
        request_data['txnId'] = yl.getRelyData(key1='txnId_1')
        if case_key == '正确参数':
            pass
        elif case_key == 'rtxnId':
            request_data['rtxnId'] = case_data['rtxnId']
        elif case_key == 'txnId':
            request_data['txnId'] = case_data['txnId']
        elif case_key == 'refundAmt':
            request_data['refundAmt'] = case_data['refundAmt']
        elif case_key == 'remark':
            request_data['remark'] = case_data['remark']
        else:
            print('/txnDownload接口请求参数错误，请检查测试用例')
    else:
        print('哈哈哈……')
    return request_data

#print(getTestdata_CB(7))


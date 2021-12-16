#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @time:2020/8/27 16:59

import json,time
from common.readExcel import OperationExcel
from common import readYaml
from common.reData import *

execl = OperationExcel("EPS")
yl = readYaml

def getTestdata_EPS(row):
    #处理请求参数
    case_data = json.loads(execl.getRequestData(row))
    case_key=list(case_data.keys())[0]
    if execl.getCaseType(row) == 'A':
        request_data = yl.getFixedData(key1='requestData_getPublicKey')
        if case_key == '正确参数':
            pass
        elif case_key == 'appId':
            request_data['appId'] = case_data['appId']
        elif case_key == 'charset':
            request_data['charset'] = case_data['charset']
        elif case_key == 'messageId':
            request_data['messageId'] = case_data['messageId']
        elif case_key == 'signType':
            request_data['signType'] = case_data['signType']
        elif case_key == 'reqTime':
            request_data['reqTime'] = case_data['reqTime']
        elif case_key == 'guestId':
            request_data['guestId'] = case_data['guestId']
        elif case_key == 'version':
            request_data['version'] = case_data['version']
        elif case_key == 'sign':
            request_data['sign'] = case_data['sign']
        elif case_key == 'keyType':
            request_data['keyType'] = case_data['keyType']
        else:
            print('/getPublicKey接口请求参数错误，请检查测试用例')
    elif execl.getCaseType(row) == 'B':
        request_data = yl.getFixedData(key1='requestData_getTapCardKey')
        if case_key == '正确参数':
            pass
        else:
            print('/getPublicKey接口请求参数错误，请检查测试用例')
    elif execl.getCaseType(row) == 'C':
        request_data = yl.getFixedData(key1='requestData_arSummaryUpload')
        request_data['date'] = time.strftime("%Y%m%d",time.localtime(time.time()))
        if case_key == '正确参数':
            pass
        elif case_key == 'deviceId':
            request_data['deviceId'] = case_data['deviceId']
        elif case_key == 'time':
            request_data['time'] = case_data['time']
        elif case_key == 'date':
            request_data['date'] = case_data['date']
        elif case_key == 'busNum':
            request_data['busNum'] = case_data['busNum']
        elif case_key == 'advanceAmt':
            request_data['advanceAmt'] = case_data['advanceAmt']
        elif case_key == 'transactionNum':
            request_data['transactionNum'] = case_data['transactionNum']
        elif case_key == 'totalEvent':
            request_data['totalEvent'] = case_data['totalEvent']
        else:
            print('/getPublicKey接口请求参数错误，请检查测试用例')
    elif execl.getCaseType(row) == 'D':
        request_data = yl.getFixedData(key1='requestData_eventLogs')
        request_data['logsList'][0]['logTime'] = time.strftime("%Y%m%d-%H%M%S",time.localtime(time.time()))
        if case_key == '正确参数':
            pass
        elif case_key == 'logCounts':
            request_data['logCounts'] = case_data['logCounts']
        elif case_key == 'deviceId':
            request_data['logsList'][0]['deviceId'] = case_data['deviceId']
        elif case_key == 'logId':
            request_data['logsList'][0]['logId'] = case_data['logId']
        elif case_key == 'logType':
            request_data['logsList'][0]['logType'] = case_data['logType']
        elif case_key == 'logTime':
            request_data['logsList'][0]['logTime'] = case_data['logTime']
        elif case_key == 'remark':
            request_data['logsList'][0]['remark'] = case_data['remark']
        else:
            print('/getPublicKey接口请求参数错误，请检查测试用例')
    return request_data

#print(getTestdata_EPS(11))


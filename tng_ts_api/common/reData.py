#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/8/11 16:34

from common.readExcel import OperationExcel

#获取FCS测试用例行数及名称
execl_FCS = OperationExcel('FCS')
numId_FCS = execl_FCS.getRows() + 1
#行程交易订单获取
FCS_txnGet = []
FCStxnGetName = []
#设置行程订单金额
FCS_setFare = []
FCSsetFareName = []
#票价调整
FCS_adjustFare = []
FCSadjustFareName = []
#日结数据查询
FCS_settlementSummary = []
FCS_settlementSummaryName = []
#设备事件日志查询接口
FCS_eventsLog = []
FCS_eventsLogName = []

for i in range(2,numId_FCS):
    if execl_FCS.getCaseType(i) == 'A':
        name = execl_FCS.getCaseName(i)
        FCS_txnGet.append((i,name))
        FCStxnGetName.append(name)
    elif execl_FCS.getCaseType(i) == 'B':
        name = execl_FCS.getCaseName(i)
        FCS_setFare.append((i, name))
        FCSsetFareName.append(name)
    elif execl_FCS.getCaseType(i) == 'C':
        name = execl_FCS.getCaseName(i)
        FCS_adjustFare.append((i, name))
        FCSadjustFareName.append(name)
    elif execl_FCS.getCaseType(i) == 'D':
        name = execl_FCS.getCaseName(i)
        FCS_settlementSummary.append((i, name))
        FCS_settlementSummaryName.append(name)
    elif execl_FCS.getCaseType(i) == 'E':
        name = execl_FCS.getCaseName(i)
        FCS_eventsLog.append((i, name))
        FCS_eventsLogName.append(name)
    else:
        pass

#获取CB(城巴)测试用例行数及名称
execl_CB = OperationExcel('CB')
numId_CB = execl_CB.getRows() + 1
#AR数据下载
CB_arData = []
CB_arDataName = []
#交易数据下载
CB_txnDownload = []
CB_txnDownloadName = []
#订单退款
CB_refund = []
CB_refundName = []

for i in range(2,numId_CB):
    if execl_CB.getCaseType(i) == 'A':
        name = execl_CB.getCaseName(i)
        CB_arData.append((i,name))
        CB_arDataName.append(name)
    elif execl_CB.getCaseType(i) == 'B':
        name = execl_CB.getCaseName(i)
        CB_txnDownload.append((i,name))
        CB_txnDownloadName.append(name)
    elif execl_CB.getCaseType(i) == 'C':
        name = execl_CB.getCaseName(i)
        CB_refund.append((i,name))
        CB_refundName.append(name)
    else:
        pass

#获取EPS测试用例行数及名称
execl_EPS = OperationExcel('EPS')
numId_EPS = execl_EPS.getRows() + 1
#获取乘车码公钥
EPS_getPublicKey = []
EPS_getPublicKeyName = []
#获取CAPK和AID数据查询
EPS_getTapCardKey = []
EPS_getTapCardKeyName = []
#AR汇总数据上传
EPS_arSummaryUpload = []
EPS_arSummaryUploadName = []
#设备事件日志上传
EPS_eventLogs = []
EPS_eventLogsName = []

for i in range(2,numId_EPS):
    if execl_EPS.getCaseType(i) == 'A':
        name = execl_EPS.getCaseName(i)
        EPS_getPublicKey.append((i,name))
        EPS_getPublicKeyName.append(name)
    elif execl_EPS.getCaseType(i) == 'B':
        name = execl_EPS.getCaseName(i)
        EPS_getTapCardKey.append((i,name))
        EPS_getTapCardKeyName.append(name)
    elif execl_EPS.getCaseType(i) == 'C':
        name = execl_EPS.getCaseName(i)
        EPS_arSummaryUpload.append((i,name))
        EPS_arSummaryUploadName.append(name)
    elif execl_EPS.getCaseType(i) == 'D':
        name = execl_EPS.getCaseName(i)
        EPS_eventLogs.append((i,name))
        EPS_eventLogsName.append(name)
    else:
        pass

#print(EPS_getPublicKey)



#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @time:2019/10/21 16:23

from common.readYaml import *
from page.xiaoeHeaders import *
import yaml,random,time,json,base64
from common.readExcel import OperationExcel
from common.readJson import OperationJson

def writeDataYaml(title='pydata',key1=None,vlue1=None):
    '''动态参数写入yaml文件'''
    with open(data_dir(fileName='DynamicData.yaml'),'r', encoding="utf-8") as f:
        content = yaml.load(f,Loader=yaml.FullLoader)
        # 修改yml文件中的参数
        content[title][key1] = vlue1
    with open(data_dir(fileName='DynamicData.yaml'), 'w', encoding="utf-8") as nf:
        yaml.dump(content, nf)

def getBuserToken():
    '''获取B端b_user_token'''
    token=getDynamicData(key1='b_user_token')
    return 'b_user_token='+token

def getLaravelSession():
    '''获取B端laravel_session'''
    session=getDynamicData(key1='laravel_session')
    return 'laravel_session='+session

def getKoToken():
    '''获取H5 ko_token'''
    ko_token=getFixedData(key1='ko_token')
    return 'ko_token='+ko_token

def getKoToken_VIP():
    '''获取H5 ko_token'''
    ko_token=getFixedData(key1='ko_token_VIP')
    return 'ko_token='+ko_token

def getHeadersInfo():
    '''B端登录请求头'''
    headers = getHeadersValue()
    headers['cookie']=getBuserToken()+';'+getLaravelSession()
    return headers

def getHeadersInfo_H5():
    '''H5登录请求头'''
    headers = getHeadersValue_H5()
    headers['cookie']=getKoToken()
    return headers

def setStep():
    dict1 = OperationJson().getRequestsData(2)
    dict1['app_id'] = getFixedData(key1='app_id')
    return dict1

def setNewGraphic(row,title):
    '''新建图文请求参数'''
    s ='ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789'
    ss = random.sample(s,6)
    sj = "".join(ss)
    dict1 = OperationJson().getRequestsData(row)
    dict1['params[title]'] = title+sj
    dict1['params[start_at]'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return dict1

def setCreateFission():
    dict1 = OperationJson().getRequestsData(5)
    dict1['activity_name'] = 'Pay_裂变海报'+str(random.randint(1,99))
    dict1['start_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+5))
    dict1['end_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+2505600))
    dict1['goods_info[0][resource_id]'] = getDynamicData(key1='resource_id')
    dict1['goods_info[0][goods_code]'] = getDynamicData(key1='resource_id')
    dict1['goods_info[0][resource_name]'] = 'Pay_裂变海报图文'+"".join(random.sample('ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789',6))
    return dict1

def setShopFission():
    dict1 = OperationJson().getRequestsData(6)
    dict1['bizData[resource_id]'] = getDynamicData(key1='resource_id')
    return dict1

def setJumpMode():
    dict1 = OperationJson().getRequestsData(7)
    dict1['bizData[resource_id]'] = getDynamicData(key1='resource_id')
    dict1['bizData[pre_get_info][resource_id]'] = getDynamicData(key1='resource_id')
    dict1['bizData[referer][resource_id]'] = getDynamicData(key1='resource_id')
    return dict1

def setBuyPublic(row,keyid):
    dict1 = OperationJson().getRequestsData(row)
    dict1['bizData[resource_id]'] = getDynamicData(key1=keyid)
    return dict1

def setCouponPublic(row,keyid,cuid):
    dict1 = OperationJson().getRequestsData(row)
    dict1['bizData[resource_id]'] = getDynamicData(key1=keyid)
    dict1['bizData[cu_id]'] = getDynamicData(key1=cuid)
    dict1['bizData[pre_get_info][resource_id]'] = getDynamicData(key1=keyid)
    dict1['bizData[referer][resource_id]'] = getDynamicData(key1=keyid)
    dict1['bizData[referer][app_id]'] = getFixedData(key1='app_id')
    return dict1

def setXqpublic(row,keyid,pageurl):
    dict1 = OperationJson().getRequestsData(row)
    dict1['bizData[resource_id]'] = getDynamicData(key1=keyid)
    dict1['bizData[target_url]'] = getDynamicData(key1=pageurl).split('/')[4]
    return dict1
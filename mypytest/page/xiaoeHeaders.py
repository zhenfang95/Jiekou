#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/10/24 14:52

from common.readYaml import *
import base64,json

def getHeadersValue():
    '''登录请求头'''
    headers={
        'Accept':'application/json, text/plain, */*',
        'Content-Type':'application/x-www-form-urlencoded',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    return headers

def getHeadersValue_H5():
    '''H5登录请求头'''
    headers={
        'Accept': 'application/json, text/plain, */*',
        'Content-Type':'application/x-www-form-urlencoded',
        'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044428 Mobile Safari/537.36 MMWEBID/4134 MicroMessenger/6.7.3.1360(0x2607033D) NetType/WIFI Language/zh_CN Process/tools'
    }
    return headers

def getHeadersPublic_H5(pagurl):
    '''带url参数的公共请求头'''
    headers={
        'Host':	'wxdd198a901fa24220.h5.xiaoe-tech.com',
        'Connection':'keep-alive',
        'Origin':'https://wxdd198a901fa24220.h5.xiaoe-tech.com',
        'User-Agent':'Mozilla/5.0 (Linux; Android 9; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044506 Mobile Safari/537.36 MMWEBID/4134 MicroMessenger/7.0.3.1400(0x2700033B) Process/tools NetType/WIFI Language/zh_CN',
        'Content-Type':'application/x-www-form-urlencoded',
        'Accept':'application/json,text/plain, */*',
        'Referer':'https://wxdd198a901fa24220.h5.xiaoe-tech.com/content_page/%s'%getDynamicData(key1=pagurl).split('/')[4],
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cookie':'ko_token=%s'%getFixedData(key1='ko_token')
    }
    return headers

def getHeaderJson():
    '''json格式请求头'''
    headers={
        'Accept':'application/json, text/plain, */*',
        'Content-Type':'application/json;charset=UTF-8',
        'User-Agent':'Mozilla/5.0(Windows NT 6.1; WOW64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/63.0.3239.132 Safari/537.36',
        'cookie':'b_user_token=%s;laravel_session=%s'%(getDynamicData(key1='b_user_token'),getDynamicData(key1='laravel_session'))
    }
    return headers

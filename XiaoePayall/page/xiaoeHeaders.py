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

def getHeadersGroup_head():
    '''拼团专用_团长'''
    headers={'Accept': 'application/json',
        'Content-Type':'application/x-www-form-urlencoded',
        'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044428 Mobile Safari/537.36 MMWEBID/4134 MicroMessenger/6.7.3.1360(0x2607033D) NetType/WIFI Language/zh_CN Process/tools',
        'POST':'https://apprnDA0ZDw4581.h5.xiaoeknow.com/distribute/first_tobe_distributor HTTP/1.1',
        'Host':'apprnDA0ZDw4581.h5.xiaoeknow.com',
        'Origin':'https://apprnDA0ZDw4581.h5.xiaoeknow.com',
        'Referer':'https://apprnDA0ZDw4581.h5.xiaoeknow.com/content_page/%s'%getRead(key1='content_url_3').split('/')[4],
        'Cookie': 'ko_token=%s'%getRead(key1='ko_token')
    }
    return headers

def getHeadersGroup_member():
    '''拼团专用_团员'''
    headers={'Accept': 'application/json',
        'Content-Type':'application/x-www-form-urlencoded',
        'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044428 Mobile Safari/537.36 MMWEBID/4134 MicroMessenger/6.7.3.1360(0x2607033D) NetType/WIFI Language/zh_CN Process/tools',
        'POST':'https://apprnDA0ZDw4581.h5.xiaoeknow.com/distribute/first_tobe_distributor HTTP/1.1',
        'Host':'apprnDA0ZDw4581.h5.xiaoeknow.com',
        'Origin':'https://apprnDA0ZDw4581.h5.xiaoeknow.com',
        'Referer':'https://apprnDA0ZDw4581.h5.xiaoeknow.com/content_page/%s'%getRead(key1='content_url_3').split('/')[4],
        'Cookie': 'ko_token=%s'%getRead(key1='ko_token_VIP')
    }
    return headers

def getHeaderPromoter_b():
    '''推广员专用_B端'''
    headers={'POST':'https://admin.xiaoe-tech.com/drp/distribute_goods/set_proportion HTTP/1.1',
    'Host':	'admin.xiaoe-tech.com',
    'Connection':'keep-alive',
    'Content-Length':'254',
    'Origin':'https://admin.xiaoe-tech.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Content-Type':'application/json',
    'Accept':'*/*',
    'Referer':'https://admin.xiaoe-tech.com/new_distribute/saler',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cookie':'b_user_token=%s;laravel_session=%s'%(getRead(key1='b_user_token'),getRead(key1='laravel_session'))}
    return headers

def getHeaderPromoter_h5():
    '''推广员专用_H5'''
    headers={'POST':'https://apprnDA0ZDw4581.h5.xiaoeknow.com/pay/pre_get_info_v3 HTTP/1.1',
    'Host':	'apprnDA0ZDw4581.h5.xiaoeknow.com',
    'Connection':'keep-alive',
    'Content-Length':'347',
    'Origin':'https://apprnDA0ZDw4581.h5.xiaoeknow.com',
    'User-Agent':'Mozilla/5.0 (Linux; Android 9; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044506 Mobile Safari/537.36 MMWEBID/4134 MicroMessenger/7.0.3.1400(0x2700033B) Process/tools NetType/WIFI Language/zh_CN',
    'Content-Type':'application/x-www-form-urlencoded',
    'Accept':'application/json',
    'Referer':'https://apprnDA0ZDw4581.h5.xiaoeknow.com/content_page/%s'%getRead(key1='content_url_4').split('/')[4],
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cookie':'ko_token=%s'%getRead(key1='ko_token')}
    return headers

def getSvip_h5():
    '''超级会员_H5'''
    headers={"POST":"https://wxdd198a901fa24220.h5.xiaoe-tech.com/pay/pre_get_info_v3 HTTP/1.1",
        "Host":"wxdd198a901fa24220.h5.xiaoe-tech.com",
        "Connection":"keep-alive",
        "Content-Length":"339",
        "Accept":"application/json",
        "Origin":"https://wxdd198a901fa24220.h5.xiaoe-tech.com",
        "X-Requested-With":"XMLHttpRequest",
        "User-Agent":"Mozilla/5.0 (Linux; Android 9; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044904 Mobile Safari/537.36 MMWEBID/4949 MicroMessenger/7.0.7.1521(0x27000736) Process/tools NetType/WIFI Language/zh_CN",
        "Content-Type":"application/x-www-form-urlencoded",
        "Referer":"https://wxdd198a901fa24220.h5.xiaoe-tech.com/content_page/%s"%getRead(key1='pageUrl13').split('/')[4],
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-CN,en-US;q=0.9",
        "Cookie":"ko_token=%s" %getRead(key1='ko_token_VIP')}
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
        'Referer':'https://wxdd198a901fa24220.h5.xiaoe-tech.com/content_page/%s'%getRead(key1=pagurl).split('/')[4],
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cookie':'ko_token=%s'%getRead(key1='ko_token')
    }
    return headers

def getHeadersLive_H5():
    '''直播H5请求头'''
    headers={
        'Accept': 'application/json, text/plain, */*',
        'Content-Type':'application/x-www-form-urlencoded',
        'Referer':'https://apprnDA0ZDw4581.h5.xiaoeknow.com/content_page/%s'%getRead(key1='alive_room').split('/')[4],
        'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044428 Mobile Safari/537.36 MMWEBID/4134 MicroMessenger/6.7.3.1360(0x2607033D) NetType/WIFI Language/zh_CN Process/tools',
        'Cookie': 'ko_token=%s'%getRead(key1='ko_token')
    }
    return headers

def getHeaderJson():
    '''json格式请求头'''
    headers={
        'Accept':'application/json, text/plain, */*',
        'Content-Type':'application/json;charset=UTF-8',
        'User-Agent':'Mozilla/5.0(Windows NT 6.1; WOW64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/63.0.3239.132 Safari/537.36',
        'cookie':'b_user_token=%s;laravel_session=%s'%(getRead(key1='b_user_token'),getRead(key1='laravel_session'))
    }
    return headers

def getHeaderWXB_App():
    '''吴晓波app'''
    headers={
        'Content-Type': 'application/json'
    }
    return headers

def getHeaderActivity_H5():
    '''活动管理H5支付'''
    data={"count":1,"ticket_scale":1,"ticket_price":1,"sku_id":getRead(key1='sku_id'),"is_teamBuy":0,"ticket_id":getRead(key1='ticket_id'),"type":8,"resource_type":9,"resource_id":getRead(key1='activity_id_9'),"product_id":"","app_id":getRead(key1='app_id')}
    pydata = str(base64.b64encode(json.dumps(data).encode()),'utf8')
    headers={
        'Host':	'wxdd198a901fa24220.h5.xiaoe-tech.com',
        'Connection':'keep-alive',
        'Origin':'https://wxdd198a901fa24220.h5.xiaoe-tech.com',
        'User-Agent':'Mozilla/5.0 (Linux; Android 9; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044506 Mobile Safari/537.36 MMWEBID/4134 MicroMessenger/7.0.3.1400(0x2700033B) Process/tools NetType/WIFI Language/zh_CN',
        'Content-Type':'application/x-www-form-urlencoded',
        'Accept':'application/json',
        'Referer':'https://wxdd198a901fa24220.h5.xiaoe-tech.com/content_page/{0}?is_pay_page=1'.format(pydata),
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cookie':'ko_token=%s'%getRead(key1='ko_token')}
    return headers
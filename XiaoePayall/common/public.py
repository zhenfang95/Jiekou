#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/9/16 10:10

import os

def data_dir(path='data',fileName=None):
    '''测试文件存放目录'''
    data = os.path.join(os.path.dirname(os.path.dirname(__file__)),path,fileName)
    return data

def get_cwd(path):
    '''根目录路径'''
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),path)




'''领取优惠劵'''
"""
import requests,time

url='https://wxdd198a901fa24220.h5.xiaoe-tech.com/addMyCoupon/v3'
da={"bizData[id]":"cou_5e6f245101ed8-fOfAZ0"}
headers={
        'Accept': 'application/json, text/plain, */*',
        'Content-Type':'application/x-www-form-urlencoded',
        'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044428 Mobile Safari/537.36 MMWEBID/4134 MicroMessenger/6.7.3.1360(0x2607033D) NetType/WIFI Language/zh_CN Process/tools',
        'cookie':'ko_token=9bd4b09d2febb36e896a75456b909cc2'}
a=0
while a<100:
    requests.packages.urllib3.disable_warnings()
    r = requests.post(url=url,data=da,headers=headers,verify=False)
    a +=1
    time.sleep(5)
    print(r.json())
"""
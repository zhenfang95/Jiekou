#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/10/24 19:27

import yaml
from common.public import *

def getRead(title='pydata',key1=None):
    '''读取yaml文件数据'''
    readfile=open(data_dir(fileName='page_data.yaml'),"r",encoding="utf-8")
    dict1=yaml.load(readfile,Loader=yaml.FullLoader)   #以字典类型读取文件
    data=dict1[title].get(key1)   #通过key值获取内容
    readfile.close() #关闭yaml文件
    return data

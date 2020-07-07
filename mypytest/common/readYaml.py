#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/10/24 19:27

import yaml
from common.public import *

def getDynamicData(title='pydata',key1=None):
    '''读取yaml文件数据'''
    readfile=open(data_dir(fileName='DynamicData.yaml'),"r",encoding="utf-8")
    dict1=yaml.load(readfile,Loader=yaml.FullLoader)   #以字典类型读取文件
    data=dict1[title].get(key1)   #通过key值获取内容
    readfile.close() #关闭yaml文件
    return data

def getFixedData(title='pydata',key1=None):
    '''读取yaml文件数据'''
    readfile=open(data_dir(fileName='FixedData.yaml'),"r",encoding="utf-8")
    dict1=yaml.load(readfile,Loader=yaml.FullLoader)   #以字典类型读取文件
    data=dict1[title].get(key1)   #通过key值获取内容
    readfile.close() #关闭yaml文件
    return data

def writeDataYaml(title='pydata',key1=None,vlue1=None):
    '''动态参数写入yaml文件'''
    with open(data_dir(fileName='DynamicData.yaml'),'r', encoding="utf-8") as f:
        content = yaml.load(f,Loader=yaml.FullLoader)
        # 修改yml文件中的参数
        content[title][key1] = vlue1
    with open(data_dir(fileName='DynamicData.yaml'), 'w', encoding="utf-8") as nf:
        yaml.dump(content, nf)

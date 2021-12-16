#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/8/11 16:34

import yaml,os

def gettData_dir(title):
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', title)
    return data_dir

def getFixedData(title='pydata',key1=None):
    '''读取yaml文件数据'''
    readfile=open(gettData_dir('FixedData.yaml'),"r",encoding="utf-8")
    dict1=yaml.load(readfile,Loader=yaml.FullLoader)   #以字典类型读取文件
    data=dict1[title].get(key1)   #通过key值获取内容
    readfile.close() #关闭yaml文件
    return data

def getRelyData(title='pydata',key1=None):
    readfile = open(gettData_dir('RelyData.yaml'),'r',encoding='utf-8')
    dict1 = yaml.load(readfile,Loader=yaml.FullLoader)
    data = dict1[title].get(key1)
    readfile.close()
    return data

def writeDataYaml(title='pydata',key1=None,vlue1=None):
    '''参数写入yaml文件'''
    with open(gettData_dir('RelyData.yaml'),'r', encoding="utf-8") as f:
        content = yaml.load(f,Loader=yaml.FullLoader)
        # 修改yml文件中的参数
        content[title][key1] = vlue1
    with open(gettData_dir('RelyData.yaml'), 'w', encoding="utf-8") as nf:
        yaml.dump(content, nf)


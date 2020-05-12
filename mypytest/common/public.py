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

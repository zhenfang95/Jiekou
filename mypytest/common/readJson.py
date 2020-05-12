#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/5/11 16:38
# @author:AlexFu

import json
from common.public import *
from common.readExcel import OperationExcel

class OperationJson:
	def __init__(self):
		self.excel=OperationExcel()

	def getReadJson(self):
		'''从json文件读取数据'''
		with open(data_dir(fileName='requestData.json'),encoding='utf-8') as fp:
			#反序列化，把json字符串转换为python数据类型
			data = json.load(fp)
			return data

	def getRequestsData(self,row):
		'''获取请求参数'''
		#序列化，把python数据类型转换为字典类型
		pydata=json.dumps(self.getReadJson()[self.excel.getRequestData(row=row)])
		return json.loads(pydata)


#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/10/21 16:05

import requests
from common.readExcel import OperationExcel
from common.logs import mylog
import warnings

operationExcel = OperationExcel()

class Method:
	def __init__(self):
		self.excel=OperationExcel()
		requests.packages.urllib3.disable_warnings()
		warnings.simplefilter('ignore',ResourceWarning)

	def post(self,row,data=None,headers=None):
		try:
			r=requests.post(
				url=self.excel.getUrl(row),
				data=data,
				headers=headers,
				verify=False)
			mylog.info('---%s---，Method：post' %(self.excel.getCaseName(row)))
			return r
		except Exception as e:
			mylog.error('接口%s请求错误,%s'%(self.excel.getCaseName(row),e))
			print(e)
			raise  RuntimeError('接口请求发生未知的错误')

	def get(self,row,params=None,headers=None):
		try:
			r=requests.get(url=self.excel.getUrl(row),
						params=params,
						headers=headers,
						verify=False)
			mylog.info('---%s---，Method：get' %(self.excel.getCaseName(row)))
			return r
		except Exception as e:
			mylog.error('接口%s请求错误,%s'%(self.excel.getCaseName(row),e))
			raise RuntimeError('接口请求发生未知错误')

	def method(self,row,data=None,params=None,headers=None):
		method=self.excel.getMethod(row)
		if method == 'post':
			r=requests.post(
				url=self.excel.getUrl(row),
				data=eval(data),
				headers=headers,
				verify=False)
			mylog.info('---%s---，Method：post' %(self.excel.getCaseName(row)))
			return r
		elif method == 'get':
			r=requests.get(
				url=self.excel.getUrl(row),
				params=eval(params),
				headers=headers,
				verify=False)
			mylog.info('---%s---，Method：get' %(self.excel.getCaseName(row)))
			return r
		else:
			pass
			mylog.error('接口请求方式错误')


#通过预期结果断言
class IsContent:
	def __init__(self):
		self.excel = OperationExcel()

	def isContent(self,row,str1):
		flag = None
		if self.excel.getExpect(row=row) in str1:
			flag = True
		else:
			flag = False
		return flag



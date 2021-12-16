#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/8/11 16:34

import os,openpyxl,xlrd
from xlutils.copy import copy
from common.excel_data import *
from common.logs import *

class OperationExcel:
    def __init__(self,sheet):
        self.data = os.path.join(os.path.dirname(os.path.dirname(__file__)),'data','caseTest.xlsx')
        self.db = openpyxl.load_workbook(self.data)
        self.sheet = self.db[sheet]
        # self.db = xlrd.open_workbook(self.data)
        # self.sheet = self.db.sheet_by_name(sheet)

    def getRows(self):
        '''获取行数'''
        return self.sheet.max_row

    def getCell(self,row,col):
        '''获取文件内容'''
        return self.sheet.cell(row=row,column=col).value

    def getCaseID(self,row):
        '''获取caseid'''
        return self.getCell(row,getCaseID())

    def getCaseName(self,row):
        '''获取用例名称'''
        return self.getCell(row,getCaseName())

    def getMethod(self,row):
        '''获取请求方式'''
        return self.getCell(row,getMethod())

    def getRequestData(self,row):
        '''获取请求参数'''
        return self.getCell(row,getRequest_Data())

    def getExpect(self,row):
        '''获取预期结果'''
        return self.getCell(row,getExpect())

    def getCaseType(self,row):
        '''获取用例类型'''
        return self.getCell(row,getCaseType())

    def getResult(self,row):
        '''获取实际结果'''
        return self.getCell(row,getResult())

    # def writeResult(self, row, content):
    #     '''测试结果写到文件中'''
    #     try:
    #         col = getResult()
    #         #work = xlrd.open_workbook(os.path.join(os.path.dirname(os.path.dirname(__file__)),'data','caseTest.xlsx'))  # 打开表
    #         #old_content = copy(work)  # 利用xlutils.copy下的copy函数复制
    #         old_content = copy(self.db)
    #         #ws = old_content.get_sheet(3)  # 获取表单0
    #         self.sheet.write(row, col, content)  ##改变（row,col）的值
    #         old_content.save(os.path.join(os.path.dirname(os.path.dirname(__file__)),'data','caseTest.xlsx'))  # 保存文件
    #         mylog.info('测试结果写入excel成功，写入结果：%s' %content)
    #
    #     except Exception as e:
    #         mylog.error('测试结果写入excel失败,原因：%s' % e)

#print(OperationExcel('FCS').getCaseName(6))
#print(OperationExcel('AA').writeResult(3,'pass'))
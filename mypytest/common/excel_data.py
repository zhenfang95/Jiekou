#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/9/16 10:51

class ExcelVariable:
    caseID = 0
    caseName = 1
    method = 2
    url = 3
    data = 4
    expect = 5
    result = 6

def getCaseID():
    return ExcelVariable.caseID

def getCaseName():
    return ExcelVariable.caseName

def getMethod():
    return ExcelVariable.method

def getUrl():
    return ExcelVariable.url

def getRequest_Data():
    return ExcelVariable.data

def getExpect():
    return ExcelVariable.expect

def getResult():
    return ExcelVariable.result


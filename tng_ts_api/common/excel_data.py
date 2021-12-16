#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/8/11 16:34

class ExcelVariable:
    caseID = 1
    caseName = 2
    method = 3
    data = 4
    expect = 5
    caseType = 6
    result = 7

def getCaseID():
    return ExcelVariable.caseID

def getCaseName():
    return ExcelVariable.caseName

def getMethod():
    return ExcelVariable.method

def getResult():
    return ExcelVariable.result

def getRequest_Data():
    return ExcelVariable.data

def getExpect():
    return ExcelVariable.expect

def getCaseType():
    return ExcelVariable.caseType


#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/10/21 16:34

import unittest
from base.method import *
from common import readExcel
from page.xiaoe import *

class TestLogin(unittest.TestCase):
    '''登录系统'''
    def setUp(self):
        self.obj = Method()
        self.asser = IsContent()
        self.excel = readExcel.OperationExcel()

    def statusCode(self, r):
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 0)

    def isContent(self, r, row):
        self.statusCode(r=r)
        self.assertTrue(self.asser.isContent(row=row, str1=r.text))

    def test_001(self):
        '''登录系统验证'''
        r = self.obj.post(1,data=eval(self.excel.getRequestData(1)),headers=getHeadersValue())
        mylog.info('result：%s' %r.json())
        self.isContent(r,1)
        writeDataYaml(key1='b_user_token',vlue1=r.cookies['b_user_token'])
        writeDataYaml(key1='laravel_session',vlue1=r.cookies['laravel_session'])

    def test_002(self):
        '''选择店铺'''
        r = self.obj.method(2,params=self.excel.getRequestData(2),headers=getHeadersInfo())
        mylog.info('result：%s' %r.json())
        self.isContent(r,2)

if __name__ == "__main__":
    unittest.main(verbosity=2)
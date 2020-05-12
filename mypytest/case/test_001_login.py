#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/10/21 16:34

import pytest
from page.xiaoe import *
from base.method import *
from common.readJson import OperationJson
import allure

@allure.feature('01、登录模块')   #在报告中添加用例标题
class TestLogin:
    obj = Method()
    asser = IsContent()
    jsda = OperationJson()

    def isContent(self, r, row):
        assert r.status_code == 200
        assert r.json()['code'] == 0
        assert self.asser.isContent(row=row, str1=r.text)

    def test_001(self):
        '''登录系统验证'''
        r = self.obj.web_post(row=1,data=self.jsda.getRequestsData(1),headers=getHeadersValue())
        mylog.info('result：%s' %r.json())
        self.isContent(r,1)
        writeDataYaml(key1='b_user_token',vlue1=r.cookies['b_user_token'])
        writeDataYaml(key1='laravel_session',vlue1=r.cookies['laravel_session'])

    def test_002(self):
        '''选择店铺'''
        r = self.obj.web_get(row=2,params=setStep(),headers=getHeadersInfo())
        mylog.info('result：%s' %r.json())
        self.isContent(r,2)

if __name__ == '__main__':
    pytest.main(['-s','-v','test_001_login.py::TestLogin'])
#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/8/11 17:07

# 执行：pytest --alluredir ./report/allure_raw
# 打开报告：allure serve report/allure_raw

import shutil
import pytest
from common.logs import *

@pytest.fixture(scope="module")
def report_del():
    # 删除旧报告文件
    mylog.info('开始清空测试报告文件……')
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'report\\allure_raw')
    if os.path.exists(path):  # 检查是否文件存在
        shutil.rmtree(path)  # 删除目录
        os.mkdir(path)  # 创建目录
        mylog.info('已清空报告文件 %s' % path)
    else:
        mylog.error('no such file:allure_raw')
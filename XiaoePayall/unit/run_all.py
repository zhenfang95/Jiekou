#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/11/28 16:05

import sys,os
dir_path=os.path.dirname(os.path.abspath(__file__))
gwd_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,gwd_path)
sys.path.insert(0,dir_path)
import unittest
from common import HTMLTestRunner
from common.public import *
from unit import myEmail

def run_case():
    #加载测试用例
    suite=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(start_dir=get_cwd('case'),
                                                 pattern='test_*.py',
                                                 top_level_dir=None)
    for test in discover:
        for test_case in test:
            suite.addTest(test_case)

    #生成测试报告
    filename=os.path.join(get_cwd('report'),'支付主流程接口自动化测试报告.html')
    fp=open(filename,'wb')
    runner= HTMLTestRunner.HTMLTestRunner(stream=fp,
                                          verbosity=2,
                                          title='支付主流程接口自动化测试报告',
                                          description='测试结果')
    runner.run(suite)
if __name__ == '__main__':
    run_case()
    myEmail.mail()

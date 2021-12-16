#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @time:2020/8/19 17:20

import logging
import time,os

get_cwd = os.path.join(os.path.dirname(os.path.dirname(__file__)))

def get_log():
    # 创建一个logger
    logger = logging.getLogger('Tng_ts')
    logger.setLevel(logging.DEBUG)
    # 设置日志存放路径，日志文件名
    # 获取本地时间，转换为设置的格式
    rq = time.strftime('%Y%m%d', time.localtime(time.time()))
    # 设置所有日志的存放路径
    all_log_path = os.path.join(get_cwd,'logs/')
    # 设置日志文件名
    all_log_name = all_log_path + 'tng_ts_' + rq + '.log'

    # 创建handler
    # 创建一个handler写入所有日志
    fh = logging.FileHandler(all_log_name,encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    # 创建一个handler输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # 定义日志输出格式
    # 以时间-日志器名称-日志级别-日志内容的形式展示
    all_log_formatter = logging.Formatter('%(asctime)s - [%(name)s] - %(levelname)s ->%(message)s')
    # 将定义好的输出形式添加到handler
    fh.setFormatter(all_log_formatter)
    ch.setFormatter(all_log_formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger

mylog=get_log()


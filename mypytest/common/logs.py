#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @time:2019/11/28 17:35

import logging
import time
from common.public import *

def get_log():
    # 创建一个logger
    logger = logging.getLogger('TestLog')
    logger.setLevel(logging.DEBUG)

    # 设置日志存放路径，日志文件名
    # 获取本地时间，转换为设置的格式
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    # 设置所有日志和错误日志的存放路径
    path = get_cwd('logs')
    all_log_path = os.path.join(path,'all_log/')
    # 设置日志文件名
    all_log_name = all_log_path + rq + '.log'

    # 创建handler
    # 创建一个handler写入所有日志
    fh = logging.FileHandler(all_log_name,encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    # 创建一个handler输出到控制台
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.DEBUG)

    # 定义日志输出格式
    # 以时间-日志器名称-日志级别-日志内容的形式展示
    all_log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # 将定义好的输出形式添加到handler
    fh.setFormatter(all_log_formatter)
    #ch.setFormatter(all_log_formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    #logger.addHandler(ch)
    return logger

mylog=get_log()
# def debug_log(message):
#     get_log().debug(message)
#
# def info_log(message):
#     get_log().info(message)
#
# def warn_log(message):
#     get_log().warning(message)
#
# def eroor_log(message):
#     get_log().error(message)


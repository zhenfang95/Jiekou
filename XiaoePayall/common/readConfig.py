#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/9/27 17:37

import configparser
from common.public import *

config_path=data_dir(fileName='config.ini')
config=configparser.ConfigParser()
config.read(config_path)

smtp_server=config.get("email","smtp_server")
port=config.get("email","port")
sender=config.get("email","sender")
psw=config.get("email","psw")
receiver=config.get("email","receiver")
username=config.get("email","username")

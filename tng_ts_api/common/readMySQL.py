#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/8/11 16:34

import pymysql

def Mysql(sql):
    try:
        conn = pymysql.connect(host='192.168.1.66',
                            port=3306,
                            user='tng_citybus_test',
                            passwd='tng_citybus123',
                            db='tng_citybus_test',
                            cursorclass=pymysql.cursors.DictCursor)   #以字典形式取数据
    except Exception as e:
        return e.args
    else:
        cur = conn.cursor()
        cur.execute(sql)
        data=cur.fetchall()
        return data
    finally:
        cur.close()
        conn.close()

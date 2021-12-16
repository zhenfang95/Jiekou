#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/8/11 17:13

import json,base64
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from urllib.parse import urlencode

def tng_signdata_rsa(private_key,sign_data):
    sign_data.pop('sign')  #删除字段sign
    data_sort = dict(sorted(sign_data.items(),key=lambda x:x[0],reverse=False))  #对字典进行从小到大排序
    #sign_data_url = urlencode(data_sort).encode('utf-8')
    sign_data_1 = dictstr(data_sort).encode('utf-8')   #把待加密数据转成QueryString的格式
    private_keyBytes = base64.b64decode(private_key)
    priKey = RSA.importKey(private_keyBytes)
    signer = PKCS1_v1_5.new(priKey)
    hash_obj = SHA256.new()
    hash_obj.update(sign_data_1)
    #hash_obj.update(sign_data_url)
    signature = base64.b64encode(signer.sign(hash_obj))
    sign = signature.decode("utf-8")
    sign_data['sign'] = sign
    return json.dumps(sign_data)

def dictstr(dict1):
    ss = []
    for key,value in dict1.items():
        if value == "":
            pass
        else:
            k = key
            v = str(value)
            a = k + '=' + v
            ss.append(a)
            ss.append('&')
    del ss[-1]
    return "".join(ss)

#带内嵌列表的参数加签
def tng_signdata_rsa_List(private_key,sign_data,redata_list):
    listda = sign_data[redata_list]
    sign_data_1 = dictstr_List(sign_data[redata_list][0])
    sign_data[redata_list] = sign_data_1
    sign_data.pop('sign')  #删除字段sign
    data_sort = dict(sorted(sign_data.items(),key=lambda x:x[0],reverse=False))  #对字典进行从小到大排序
    sign_data_2 = dictstr(data_sort).encode('utf-8')
    private_keyBytes = base64.b64decode(private_key)
    priKey = RSA.importKey(private_keyBytes)
    signer = PKCS1_v1_5.new(priKey)
    hash_obj = SHA256.new()
    hash_obj.update(sign_data_2)
    signature = base64.b64encode(signer.sign(hash_obj))
    sign = signature.decode("utf-8")
    sign_data['sign'] = sign
    sign_data[redata_list] = listda
    return json.dumps(sign_data)

def dictstr_List(dict1):
    data_sort = dict(sorted(dict1.items(), key=lambda x:x[0], reverse=False))
    ss = []
    for key,value in data_sort.items():
        if value == "":
            pass
        else:
            k = key
            v = str(value)
            a = k + '=' + v
            ss.append(a)
            ss.append('&')
    del ss[-1]
    return "[{" + "".join(ss) + "}]"




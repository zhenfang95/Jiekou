#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @time:2019/10/21 16:23

from common.readYaml import *
from page.xiaoeHeaders import *
import yaml,random,time,json,base64
from common.readExcel import OperationExcel

def writeDataYaml(title='pydata',key1=None,vlue1=None):
    '''动态参数写入yaml文件'''
    with open(data_dir(fileName='page_data.yaml'),'r', encoding="utf-8") as f:
        content = yaml.load(f,Loader=yaml.FullLoader)
        # 修改yml文件中的参数
        content[title][key1] = vlue1
    with open(data_dir(fileName='page_data.yaml'), 'w', encoding="utf-8") as nf:
        yaml.dump(content, nf)

def getBuserToken():
    '''获取B端b_user_token'''
    token=getRead(key1='b_user_token')
    return 'b_user_token='+token

def getLaravelSession():
    '''获取B端laravel_session'''
    session=getRead(key1='laravel_session')
    return 'laravel_session='+session

def getCookieSessionId():
    '''获取H5 session_id'''
    cookiesession=getRead(key1='cookie_session_id')
    return 'cookie_session_id='+cookiesession

def getCookieSessionId_VIP():
    '''获取H5 session_id'''
    cookiesession=getRead(key1='cookie_session_id_VIP')
    return 'cookie_session_id='+cookiesession

def getKoToken():
    '''获取H5 ko_token'''
    ko_token=getRead(key1='ko_token')
    return 'ko_token='+ko_token

def getKoToken_VIP():
    '''获取H5 ko_token'''
    ko_token=getRead(key1='ko_token_VIP')
    return 'ko_token='+ko_token

def getHeadersInfo():
    '''B端登录请求头'''
    headers = getHeadersValue()
    headers['cookie']=getBuserToken()+';'+getLaravelSession()
    return headers

def getHeadersInfo_H5():
    '''H5登录请求头'''
    headers = getHeadersValue_H5()
    headers['cookie']=getKoToken()
    return headers

def getHeadersInfo_H5_VIP():
    '''H5登录请求头_讲师'''
    headers = getHeadersValue_H5()
    headers['cookie']=getKoToken_VIP()
    return headers

def getserverOrderId1():
    return getRead(key1='serverOrder_id1')

def getserverOrderId2():
    return getRead(key1='serverOrder_id2')

def setNewgraphic01(row,title):
    '''新建图文请求参数'''
    s ='ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789'
    ss = random.sample(s,6)
    sj = "".join(ss)
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['params[title]'] = title+sj
    dict1['params[start_at]'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return dict1

def setNewColumn(row,title):
    '''新建专栏请求参数'''
    s ='ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789'
    ss = random.sample(s,6)   #从s中随机取6个值
    sj = "".join(ss)
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['params[name]'] = title+sj
    return dict1

def setNewLive(row,title):
    '''新建直播请求参数'''
    s ='ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789'
    ss = random.sample(s,6)
    sj = "".join(ss)
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['params[title]'] = title+sj
    dict1['params[start_at]'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    dict1['params[zb_start_at]'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return dict1

def setEditLive(row,title,alive_id):
    '''再次编辑直播'''
    s ='ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789'
    ss = random.sample(s,6)
    sj = "".join(ss)
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['params[title]'] = title+sj
    dict1['params[start_at]'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    dict1['params[zb_start_at]'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    dict1['params[id]'] = getRead(key1=alive_id)
    dict1['lead[app_id]'] = getRead(key1='app_id')
    dict1['lead[resource_id]'] = getRead(key1=alive_id)
    return dict1

def setEditagain(row,title,resource_id):
    '''再次编辑图文'''
    s = 'ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789'
    ss = random.sample(s, 6)
    sj = "".join(ss)
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['params[title]'] = title + sj
    dict1['params[start_at]'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    dict1['params[id]'] = getRead(key1=resource_id)
    dict1['lead[app_id]'] = getRead(key1='app_id')
    dict1['lead[resource_id]'] = getRead(key1=resource_id)
    return dict1

def setEditColumn(row,title,resource_id):
    '''再次编辑专栏'''
    s = 'ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789'
    ss = random.sample(s, 6)
    sj = "".join(ss)
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['params[name]'] = title + sj
    dict1['params[id]'] = getRead(key1=resource_id)
    dict1['lead[app_id]'] = getRead(key1='app_id')
    dict1['lead[resource_id]'] = getRead(key1=resource_id)
    return dict1

def setCreateFission():
    dict1 = json.loads(OperationExcel().getRequestData(12))
    dict1['activity_name'] = 'Pay_裂变海报'+str(random.randint(1,99))
    dict1['start_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+5))
    dict1['end_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+2505600))
    dict1['goods_info[0][resource_id]'] = getRead(key1='resource_id')
    dict1['goods_info[0][goods_code]'] = getRead(key1='resource_id')
    dict1['goods_info[0][resource_name]'] = 'Pay_裂变海报图文'+"".join(random.sample('ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789',6))
    return dict1

def setShopFission():
    dict1 = json.loads(OperationExcel().getRequestData(13))
    dict1['bizData[resource_id]'] = getRead(key1='resource_id')
    return dict1

def setJumpMode():
    dict1 = json.loads(OperationExcel().getRequestData(14))
    dict1['bizData[resource_id]'] = getRead(key1='resource_id')
    dict1['bizData[pre_get_info][resource_id]'] = getRead(key1='resource_id')
    dict1['bizData[referer][resource_id]'] = getRead(key1='resource_id')
    return dict1

def setBase64JM(pydata):
    '''base64加密处理'''
    data = pydata.encode()
    dict1 = str(base64.b64encode(data),'utf8')
    return dict1

def setPromotion():
    dict1 = json.loads(OperationExcel().getRequestData(18))
    dict1['activity_name'] = 'Pay_限时折扣'+str(random.randint(1,99))
    dict1['start_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+3))
    dict1['end_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+2505600))
    dict1['goods_list[0][resource_id]'] = getRead(key1='resource_id_1')
    dict1['goods_list[0][goods_code]'] = getRead(key1='resource_id_1')
    dict1['goods_list[0][resource_name]'] = getRead(key1='name01')
    return dict1

def setShopPromotion():
    dict1 = json.loads(OperationExcel().getRequestData(20))
    dict1['bizData[resource_id]'] = getRead(key1='resource_id_1')
    dict1['bizData[activity_id]'] = getRead(key1='activity_id')
    return dict1

def setJumpMode_1():
    dict1 = json.loads(OperationExcel().getRequestData(21))
    dict1['bizData[resource_id]'] = getRead(key1='resource_id_1')
    dict1['bizData[activity_id]'] = getRead(key1='activity_id')
    dict1['bizData[pre_get_info][resource_id]'] = getRead(key1='resource_id_1')
    dict1['bizData[pre_get_info][activity_id]'] = getRead(key1='activity_id')
    dict1['bizData[referer][resource_id]'] = getRead(key1='resource_id_1')
    return dict1

def setSeckilling():
    dict1 = json.loads(OperationExcel().getRequestData(25))
    dict1['activity_name'] = 'Pay_预约秒杀'+str(random.randint(1,99))
    dict1['start_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+60))
    dict1['end_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+2505600))
    dict1['goods_info[id]'] = getRead(key1='resource_id_2')
    dict1['goods_info[resource_id]'] = getRead(key1='resource_id_2')
    return dict1

def setMaatskill():
    dict1 = json.loads(OperationExcel().getRequestData(26))
    dict1['bizData[activity_id]'] = getRead(key1='activity_id_1')
    return dict1

def setShopMaatskill():
    dict1 = json.loads(OperationExcel().getRequestData(27))
    dict1['bizData[resource_id]'] = getRead(key1='resource_id_2')
    dict1['bizData[activity_id]'] = getRead(key1='activity_id_1')
    return dict1

def setJumpMode_2():
    dict1 = json.loads(OperationExcel().getRequestData(28))
    dict1['bizData[resource_id]'] = getRead(key1='resource_id_2')
    dict1['bizData[activity_id]'] = getRead(key1='activity_id_1')
    dict1['bizData[pre_get_info][resource_id]'] = getRead(key1='resource_id_2')
    dict1['bizData[pre_get_info][activity_id]'] = getRead(key1='activity_id_1')
    dict1['bizData[referer][resource_id]'] = getRead(key1='resource_id_2')
    return dict1

def setSale():
    dict1 = json.loads(OperationExcel().getRequestData(32))
    dict1['activity_name'] = 'Pay_秒杀活动'+str(random.randint(1,99))
    dict1['start_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+2))
    dict1['end_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+2505600))
    dict1['goods_info[id]'] = getRead(key1='resource_id_3')
    dict1['goods_info[resource_id]'] = getRead(key1='resource_id_3')
    dict1['goods_info[title]'] = getRead(key1='name02')
    return dict1

def setShopSale():
    dict1 = json.loads(OperationExcel().getRequestData(33))
    dict1['bizData[resource_id]'] = getRead(key1='resource_id_3')
    dict1['bizData[activity_id]'] = getRead(key1='activity_id_2')
    return dict1

def setJumpMode_3():
    dict1 = json.loads(OperationExcel().getRequestData(34))
    dict1['bizData[resource_id]'] = getRead(key1='resource_id_3')
    dict1['bizData[activity_id]'] = getRead(key1='activity_id_2')
    dict1['bizData[pre_get_info][resource_id]'] = getRead(key1='resource_id_3')
    dict1['bizData[pre_get_info][activity_id]'] = getRead(key1='activity_id_2')
    dict1['bizData[referer][resource_id]'] = getRead(key1='resource_id_3')
    return dict1

def setRoseArtifact():
    dict1 = json.loads(OperationExcel().getRequestData(39))
    dict1['activity_name'] = 'Pay_涨粉神器'+str(random.randint(1,99))
    dict1['resource_id'] = getRead(key1='package_id')
    dict1['resource_name'] = getRead(key1='name03')
    dict1['start_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    dict1['end_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+2505600))
    dict1['key_words'] = random.randint(1,9999)
    return dict1

def setArtifactPoster():
    dict1 = json.loads(OperationExcel().getRequestData(41))
    dict1['activity_id'] = getRead(key1='activity_id_3')
    dict1['goods_code'] = getRead(key1='package_id')
    return dict1

def setShopArtifact():
    dict1 = json.loads(OperationExcel().getRequestData(42))
    dict1['bizData[product_id]'] = getRead(key1='package_id')
    dict1['bizData[resource_id]'] = getRead(key1='package_id')
    return dict1

def setShopArtifact_a():
   dict1 = json.loads(OperationExcel().getRequestData(43))
   dict1['bizData[resource_id]'] = getRead(key1='package_id')
   dict1['bizData[pre_get_info][product_id]'] = getRead(key1='package_id')
   dict1['bizData[pre_get_info][resource_id]'] = getRead(key1='package_id')
   dict1['bizData[referer][product_id]'] = getRead(key1='package_id')
   return dict1

def setShopArtifact_coupon():
    dict1 = json.loads(OperationExcel().getRequestData(44))
    dict1['bizData[product_id]'] = getRead(key1='package_id')
    dict1['bizData[resource_id]'] = getRead(key1='package_id')
    return dict1

def setShopArtifact_coupon_a():
   dict1 = json.loads(OperationExcel().getRequestData(45))
   dict1['bizData[resource_id]'] = getRead(key1='package_id')
   dict1['bizData[cu_id]'] = getRead(key1='cu_id_1')
   dict1['bizData[pre_get_info][product_id]'] = getRead(key1='package_id')
   dict1['bizData[pre_get_info][resource_id]'] = getRead(key1='package_id')
   dict1['bizData[referer][product_id]'] = getRead(key1='package_id')
   return dict1

def setViewArtifact():
    dict22 = json.loads(OperationExcel().getRequestData(46))
    dict22['bizData[product_id]'] = getRead(key1='package_id')
    dict22['bizData[target_url]'] = getRead(key1='content_url').split('/')[4] #以符号“/”拆分字符串，获取第五位字符
    return dict22

def setNewFriends():
    dict1 = json.loads(OperationExcel().getRequestData(51))
    dict1['activity_name'] = 'Pay_好友助力'+str(random.randint(1,99))
    dict1['goods_info[0][resource_id]'] = getRead(key1='package_id_1')
    dict1['goods_info[0][resource_name]'] = getRead(key1='name04')
    dict1['start_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    dict1['end_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+2505600))
    dict1['goods_info[0][goods_code]'] = getRead(key1='package_id_1')
    return dict1

def setNewFriends_a():
    dict1 = json.loads(OperationExcel().getRequestData(60))
    dict1['activity_name'] = 'Pay_好友助力'+str(random.randint(1,99))
    dict1['goods_info[0][resource_id]'] = getRead(key1='package_id_2')
    dict1['goods_info[0][resource_name]'] = getRead(key1='name05')
    dict1['start_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    dict1['end_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+2505600))
    dict1['goods_info[0][goods_code]'] = getRead(key1='package_id_2')
    return dict1

def setSponFriends():
   dict1 = json.loads(OperationExcel().getRequestData(52))
   dict1['bizData[activity_id]'] = getRead(key1='activity_id_4')
   dict1['bizData[goods_code]'] = getRead(key1='package_id_1')
   return dict1

def setSponFriends_a():
   dict1 = json.loads(OperationExcel().getRequestData(53))
   dict1['bizData[activity_id]'] = getRead(key1='activity_id_4')
   dict1['bizData[goods_code]'] = getRead(key1='package_id_1')
   dict1['bizData[upvote_user_id]'] = getRead(key1='upvote_user_id')
   dict1['bizData[user_id]'] = getRead(key1='user_id')
   return dict1

def setSponFriends_b():
   dict1 = json.loads(OperationExcel().getRequestData(54))
   dict1['bizData[activity_id]'] = getRead(key1='activity_id_4')
   dict1['bizData[goods_code]'] = getRead(key1='package_id_1')
   dict1['bizData[upvote_user_id]'] = getRead(key1='upvote_user_id')
   return dict1

def setSponFriends_c():
    dict1 = json.loads(OperationExcel().getRequestData(55))
    dict1['bizData[resource_id]'] = getRead(key1='package_id_1')
    dict1['bizData[product_id]'] = getRead(key1='package_id_1')
    dict1['bizData[activity_id]'] = getRead(key1='activity_id_4')
    return dict1

def setSponFriends_d():
    dict1 = json.loads(OperationExcel().getRequestData(56))
    dict1['bizData[resource_id]'] = getRead(key1='package_id_1')
    dict1['bizData[product_id]'] = getRead(key1='package_id_1')
    dict1['bizData[target_url]'] = getRead(key1='content_url_1').split('/')[4]
    return dict1

def setShopFriends():
    dict1 = json.loads(OperationExcel().getRequestData(61))
    dict1['bizData[product_id]'] = getRead(key1='package_id_2')
    dict1['bizData[resource_id]'] = getRead(key1='package_id_2')
    return dict1

def setShopFriends_a():
    dict1 = json.loads(OperationExcel().getRequestData(62))
    dict1['bizData[resource_id]'] = getRead(key1='package_id_2')
    return dict1

def setShopFriends_coupon():
    dict1 = json.loads(OperationExcel().getRequestData(63))
    dict1['bizData[product_id]'] = getRead(key1='package_id_2')
    dict1['bizData[resource_id]'] = getRead(key1='package_id_2')
    return dict1

def setShopFriends_coupon_a():
    dict1 = json.loads(OperationExcel().getRequestData(64))
    dict1['bizData[resource_id]'] = getRead(key1='package_id_2')
    dict1['bizData[cu_id]'] = getRead(key1='cu_id_1')
    return dict1

def setSponFriends_g():
    dict1 = json.loads(OperationExcel().getRequestData(65))
    dict1['bizData[resource_id]'] = getRead(key1='package_id_2')
    dict1['bizData[product_id]'] = getRead(key1='package_id_2')
    dict1['bizData[target_url]'] = getRead(key1='content_url_2').split('/')[4]
    return dict1

def setGroup():
    dict1 = json.loads(OperationExcel().getRequestData(69))
    dict1['resource_name'] = getRead(key1='name06')
    dict1['resource_id'] = getRead(key1='resource_id_4')
    dict1['start_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+1))
    dict1['stop_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+2505600))
    return dict1

def setShopGroup_head_a():
    dict1 = json.loads(OperationExcel().getRequestData(73))
    dict1['bizData[resource_id]'] = getRead(key1='resource_id_4')
    dict1['bizData[product_id]'] = getRead(key1='resource_id_4')
    dict1['bizData[team_buy_id]'] = getRead(key1='team_buy_id')
    return dict1

def setShopGroup_head_a1():
    dict1 = json.loads(OperationExcel().getRequestData(74))
    dict1['bizData[resource_id]'] = getRead(key1='resource_id_4')
    dict1['bizData[target_url]'] = getRead(key1='content_url_3').split('/')[4]
    return dict1

def setShopGroup_member():
    dict1 = json.loads(OperationExcel().getRequestData(75))
    dict1['bizData[team_buy_id]'] = getRead(key1='team_buy_id')
    dict1['bizData[task_id]'] = getRead(key1='task_id')
    return dict1

def setShopGroup_member_a():
    dict1 = json.loads(OperationExcel().getRequestData(76))
    dict1['bizData[resource_id]'] = getRead(key1='resource_id_4')
    dict1['bizData[product_id]'] = getRead(key1='resource_id_4')
    dict1['bizData[team_buy_id]'] = getRead(key1='team_buy_id')
    dict1['bizData[team_buy_task_id]'] = getRead(key1='task_id')
    return dict1

def setGroup_coupon():
    dict1 = json.loads(OperationExcel().getRequestData(79))
    dict1['resource_name'] = getRead(key1='name07')
    dict1['resource_id'] = getRead(key1='resource_id_5')
    dict1['start_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+1))
    dict1['stop_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+2505600))
    return dict1

def setGroup_coupon_1():
    dict1 = json.loads(OperationExcel().getRequestData(80))
    dict1['bizData[resource_id]'] = getRead(key1='resource_id_5')
    dict1['bizData[target_url]'] = getRead(key1='content_url_4').split('/')[4]
    return dict1

def setShopGroup_coupon():
    dict1 = json.loads(OperationExcel().getRequestData(81))
    dict1['bizData[resource_id]'] = getRead(key1='resource_id_5')
    return dict1

def setShopGroup_coupon_1():
    dict1 = json.loads(OperationExcel().getRequestData(82))
    dict1['bizData[resource_id]'] = getRead(key1='resource_id_5')
    return dict1

def setShopGroup_coupon_2():
    dict1 = json.loads(OperationExcel().getRequestData(83))
    dict1['bizData[resource_id]'] = getRead(key1='resource_id_5')
    return dict1

def setShopGroup_coupon_3():
    dict1 = json.loads(OperationExcel().getRequestData(84))
    dict1['bizData[resource_id]'] = getRead(key1='resource_id_5')
    dict1['bizData[cu_id]'] = getRead(key1='cu_id_2')
    return dict1

def setShopGroup_coupon_4():
    dict1 = json.loads(OperationExcel().getRequestData(85))
    dict1['bizData[resource_id]'] = getRead(key1='resource_id_5')
    dict1['bizData[target_url]'] = getRead(key1='content_url_4').split('/')[4]
    return dict1

def setPromoter():
    dict1 = json.loads(OperationExcel().getRequestData(88))
    dict1['app_id'] = getRead(key1='app_id')
    dict1['goods_code'] = getRead(key1='resource_id_6')
    dict2 = json.dumps(dict1)
    return dict2

def setShopPromoter():
    dict1 = json.loads(OperationExcel().getRequestData(89))
    dict1['bizData[resource_id]'] = getRead(key1='resource_id_6')
    return dict1

def setShopPromoter_1():
    dict1 = json.loads(OperationExcel().getRequestData(90))
    dict1['bizData[resource_id]'] = getRead(key1='resource_id_6')
    return dict1

def setCreateCoupon():
    dict1 = json.loads(OperationExcel().getRequestData(91))
    dict1['title'] = 'Pay_优惠券' + str(random.randint(1, 99))
    dict1['valid_at'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    dict1['invalid_at'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 2505600))
    return dict1

def setReceiveCoupon():
    dict1 = json.loads(OperationExcel().getRequestData(93))
    dict1['bizData[id]'] = getRead(key1='cou_id')
    return dict1

def setRequestCode():
    dict1 = json.loads(OperationExcel().getRequestData(96))
    dict1['params[name]'] = 'Pay_邀请码' + str(random.randint(1, 99))
    dict1['params[card_title]'] = 'Pay_邀请码' + str(random.randint(1, 99))
    dict1['params[start_at]'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    dict1['params[stop_at]'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 2505600))
    dict1['params[target_name]'] = getRead(key1='name08')
    dict1['params[resource_id]'] = getRead(key1='resource_id_7')
    return dict1

def setRequestCode1():
    dict1 = json.loads(OperationExcel().getRequestData(98))
    dict1['batch_id'] = getRead(key1='bid')
    return dict1

def setRequestCode_u():
    dict1 = json.loads(OperationExcel().getRequestData(99))
    dict1['bizData[invite_code]'] = getRead(key1='yqm_id')
    return dict1

def setRequestCode_u1():
    dict1 = json.loads(OperationExcel().getRequestData(100))
    dict1['bizData[invite_code]'] = getRead(key1='yqm_id')
    return dict1

def setRequestCode_u2():
    dict1 = json.loads(OperationExcel().getRequestData(102))
    dict1['id'] = getRead(key1='bid')
    return dict1

def setRequestCode_u3():
    dict1 = json.loads(OperationExcel().getRequestData(103))
    dict1['id'] = getRead(key1='bid')
    return dict1

def setRequestCode_u4():
    dict1 = json.loads(OperationExcel().getRequestData(104))
    dict1['bizData[resource_id]'] = getRead(key1='resource_id_7')
    dict1['bizData[target_url]'] = getRead(key1='content_url_5').split('/')[4]
    return dict1

def setCDkey():
    dict1 = json.loads(OperationExcel().getRequestData(108))
    dict1['title']= 'Pay_兑换码' + str(random.randint(1, 99))
    dict1['start_at'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 2))
    dict1['end_at'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 2505600))
    dict1['resource'][0]['resource_name']  = getRead(key1='name09')
    dict1['resource'][0]['resource_id'] = getRead(key1='resource_id_8')
    #dict1['coupon'][0]['title'] = 'Pay_兑优惠券' + str(random.randint(1, 99))
    dict2 = json.dumps(dict1)
    dict3 = {}
    dict3['content'] = dict2
    return dict3

def setCDkey_u():
    dict1 = json.loads(OperationExcel().getRequestData(110))
    dict1['activity_id'] = getRead(key1='activity_id_5')
    dict1['batch_id'] = getRead(key1='batch_id')
    return dict1

def setCDkey_u1():
    dict1 = json.loads(OperationExcel().getRequestData(111))
    dict1['bizData[invite_code]'] = getRead(key1='redeem_code')
    return dict1

def setCDkey_u2():
    dict1 = json.loads(OperationExcel().getRequestData(112))
    dict1['bizData[redeem_code]'] = getRead(key1='redeem_code')
    return dict1

def setCDkey_u3():
    dict1 = json.loads(OperationExcel().getRequestData(114))
    dict1['bizData[resource_id]'] = getRead(key1='resource_id_8')
    dict1['bizData[target_url]'] = getRead(key1='content_url_6').split('/')[4]
    return dict1

def setSvip():
    dict1 = json.loads(OperationExcel().getRequestData(120))
    dict1['bizData[product_id]'] = getRead(key1='svip_id')
    dict1['bizData[resource_id]'] = getRead(key1='resource_id_9')
    return dict1

def setSvip_1():
    dict1 = json.loads(OperationExcel().getRequestData(121))
    dict1['bizData[resource_id]'] = getRead(key1='resource_id_9')
    dict1['bizData[product_id]'] = getRead(key1='svip_id')
    dict1['bizData[pre_get_info][product_id]'] = getRead(key1='svip_id')
    dict1['bizData[pre_get_info][resource_id]'] = getRead(key1='resource_id_9')
    return dict1

def setBuyPublic(row,keyid):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['bizData[resource_id]'] = getRead(key1=keyid)
    return dict1

def setCouponPublic(row,keyid,cuid):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['bizData[resource_id]'] = getRead(key1=keyid)
    dict1['bizData[cu_id]'] = getRead(key1=cuid)
    dict1['bizData[pre_get_info][resource_id]'] = getRead(key1=keyid)
    dict1['bizData[referer][resource_id]'] = getRead(key1=keyid)
    dict1['bizData[referer][app_id]'] = getRead(key1='app_id')
    return dict1

def setXqpublic(row,keyid,pageurl):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['bizData[resource_id]'] = getRead(key1=keyid)
    dict1['bizData[target_url]'] = getRead(key1=pageurl).split('/')[4]
    return dict1

def setLivepublic(row,keyid):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['bizData[resource_id]'] = getRead(key1=keyid)
    dict1['bizData[pre_get_info][resource_id]'] = getRead(key1=keyid)
    return dict1

def setLiveCoupublic(row,keyid,cuid):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['bizData[resource_id]'] = getRead(key1=keyid)
    dict1['bizData[cu_id]'] = getRead(key1=cuid)
    dict1['bizData[pre_get_info][resource_id]'] = getRead(key1=keyid)
    return dict1

def setLivey1():
    dict1 = json.loads(OperationExcel().getRequestData(156))
    dict1['params[0][alive_id]'] = getRead(key1='alive_id_01')
    dict1['params[0][user_id]'] = getRead(key1='user_id')
    dict1['alive_id'] = getRead(key1='alive_id_01')
    return dict1

def setLivey2():
    dict1 = json.loads(OperationExcel().getRequestData(159))
    dict1['bizData[alive_id]'] = getRead(key1='alive_id_01')
    dict1['bizData[app_id]'] = getRead(key1='app_id')
    dict1['bizData[user_id]'] = getRead(key1='user_id')
    dict1['bizData[room_id]'] = getRead(key1='room_id')
    #获取本地时间转换成时间戳
    dict1['bizData[comment_id]'] = 'e2fdc8b1bda5c731406168'+str(int(time.mktime(time.strptime(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'%Y-%m-%d %H:%M:%S'))))
    return dict1

def setLivey3():
    dict1 = json.loads(OperationExcel().getRequestData(160))
    dict1['bizData[alive_id]'] = getRead(key1='alive_id_01')
    dict1['bizData[user_id]'] = getRead(key1='upvote_user_id')
    dict1['bizData[rewarded_user_id]'] = getRead(key1='user_id')
    return dict1

def setspColumn():
    dict1 = json.loads(OperationExcel().getRequestData(204))
    dict1['resource_list[0][resource_id]'] = getRead(key1='resource_id_10')
    dict1['package_id'] = getRead(key1='resource_id_14')
    return dict1

def setXqpublic_a(row,keyid,pageurl):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['bizData[product_id]'] = getRead(key1=keyid)
    dict1['bizData[target_url]'] = getRead(key1=pageurl).split('/')[4]
    return dict1

def setBuyPublic_a(row,keyid):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['bizData[resource_id]'] = getRead(key1=keyid)
    dict1['bizData[product_id]'] = getRead(key1=keyid)
    return dict1

def setColumnPublic(row,keyid):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['bizData[resource_id]'] = getRead(key1=keyid)
    dict1['bizData[pre_get_info][product_id]'] = getRead(key1=keyid)
    dict1['bizData[pre_get_info][resource_id]'] = getRead(key1=keyid)
    dict1['bizData[referer][product_id]'] = getRead(key1=keyid)
    dict1['bizData[referer][app_id]'] = getRead(key1='app_id')
    return dict1

def setColumnPublic_c(row,keyid,cuid):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['bizData[resource_id]'] = getRead(key1=keyid)
    dict1['bizData[cu_id]'] = getRead(key1=cuid)
    dict1['bizData[pre_get_info][product_id]'] = getRead(key1=keyid)
    dict1['bizData[pre_get_info][resource_id]'] = getRead(key1=keyid)
    dict1['bizData[referer][product_id]'] = getRead(key1=keyid)
    dict1['bizData[referer][app_id]'] = getRead(key1='app_id')
    return dict1

def setspColumn_a():
    dict1 = json.loads(OperationExcel().getRequestData(212))
    dict1['resource_list[0][resource_id]'] = getRead(key1='resource_id_14')
    dict1['package_id'] = getRead(key1='resource_id_15')
    return dict1

def setColumn_pub(row,keyid):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['bizData[resource_id]'] = getRead(key1=keyid)
    dict1['bizData[pre_get_info][product_id]'] = getRead(key1=keyid)
    dict1['bizData[pre_get_info][resource_id]'] = getRead(key1=keyid)
    return dict1

def setColumn_pub_c(row,keyid,cuid):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['bizData[resource_id]'] = getRead(key1=keyid)
    dict1['bizData[cu_id]'] = getRead(key1=cuid)
    dict1['bizData[pre_get_info][product_id]'] = getRead(key1=keyid)
    dict1['bizData[pre_get_info][resource_id]'] = getRead(key1=keyid)
    return dict1

def setVip1():
    dict1 = json.loads(OperationExcel().getRequestData(219))
    dict1['resource_list[0][resource_id]'] = getRead(key1='resource_id_10')
    dict1['package_id'] = getRead(key1='resource_id_16')
    return dict1

def setVip2():
    dict1 = json.loads(OperationExcel().getRequestData(220))
    dict1['resource_list[0][resource_id]'] = getRead(key1='resource_id_14')
    dict1['package_id'] = getRead(key1='resource_id_16')
    return dict1

def setFreeCamp():
    sj = "".join(random.sample('ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789', 6))
    dict1 = json.loads(OperationExcel().getRequestData(227))
    dict1['app_id'] = getRead(key1='app_id')
    dict1['camp_id'] = getRead(key1='CampId')
    dict1['title'] = 'Pay_训练营免费营期'+sj
    dict1['enrollment_start_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    dict1['enrollment_stop_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+2505600))
    dict1['lesson_start_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    dict1['lesson_stop_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+2505600))
    dict2=json.dumps(dict1)
    return dict2

def setFreeCamp_p():
    sj = "".join(random.sample('ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789', 6))
    dict1 = json.loads(OperationExcel().getRequestData(228))
    dict1['app_id'] = getRead(key1='app_id')
    dict1['camp_id'] = getRead(key1='CampId')
    dict1['title'] = 'Pay_训练营免费营期'+sj
    dict1['enrollment_start_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    dict1['enrollment_stop_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+2505600))
    dict1['lesson_start_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    dict1['lesson_stop_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+2505600))
    dict1['nodes'][0]['children'][0]['resource_id'] = getRead(key1='resource_id_10')
    dict1['resource_ids_after'][getRead(key1='resource_id_10')] = 1
    dict2=json.dumps(dict1)
    return dict2

def setFreeCamp_p0():
    dict1 = json.loads(OperationExcel().getRequestData(229))
    dict1['camp_id'] = getRead(key1='CampId')
    return dict1

def setFreeCamp_p1():
    dict1 = json.loads(OperationExcel().getRequestData(230))
    dict1['bizData[product_id]'] = getRead(key1='term_id')
    return dict1

def setFreeCamp_p2():
    dict1 = json.loads(OperationExcel().getRequestData(231))
    dict1['bizData[product_id]'] = getRead(key1='term_id')
    dict1['bizData[resource_id]'] = getRead(key1='resource_id_17')
    return dict1

def setFreeCamp_p3():
    dict1 = json.loads(OperationExcel().getRequestData(234))
    dict1['bizData[termId]'] = getRead(key1='term_id')
    return dict1

def setFreeCamp_p4():
    dict1 = json.loads(OperationExcel().getRequestData(235))
    dict1['bizData[termId]'] = getRead(key1='term_id')
    dict1['bizData[nodeId]'] = getRead(key1='nodeId')
    return dict1

def setNewFace():
    sj = "".join(random.sample('ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789', 6))
    dict1 = json.loads(OperationExcel().getRequestData(237))
    dict1['title'] = 'Pay_体验课'+sj
    dict1['params[start_at]'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return dict1

def setFace_buy(row,keyid1,keyid2):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['bizData[sku_id]'] = getRead(key1=keyid1)
    dict1['bizData[resource_id]'] = getRead(key1=keyid2)
    return dict1

def setFace_buy02():
    dict1 = json.loads(OperationExcel().getRequestData(240))
    dict1['bizData[sku_id]'] = getRead(key1='goods_code_01')
    dict1['bizData[resource_id]'] = getRead(key1='course_offline_id_01')
    dict1['bizData[pre_get_info][sku_id]'] = getRead(key1='goods_code_01')
    dict1['bizData[pre_get_info][resource_id]'] = getRead(key1='course_offline_id_01')
    dict1['bizData[edu_student_info][student_id]'] = getRead(key1='student_id')
    return dict1

def setFace_buy03():
    dict1 = json.loads(OperationExcel().getRequestData(241))
    dict1['bizData[sku_id]'] = getRead(key1='goods_code_01')
    dict1['bizData[resource_id]'] = getRead(key1='course_offline_id_01')
    dict1['bizData[pre_get_info][sku_id]'] = getRead(key1='goods_code_01')
    dict1['bizData[pre_get_info][resource_id]'] = getRead(key1='course_offline_id_01')
    dict1['bizData[edu_student_info][student_id]'] = getRead(key1='student_id')
    dict1['bizData[cu_id]'] = getRead(key1='cu_id_16')
    return dict1

def setNewCourse(row,name,title):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['course_name'] = name+str(random.randint(1, 99))
    dict1['chapter_info'][0]['title'] = title+str(random.randint(1, 99))
    dict2 = json.dumps(dict1)
    return dict2

def setNewFacehour(row,title,couid):
    sj = "".join(random.sample('ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789',6))
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['title'] = title+sj
    dict1['course_id'] = getRead(key1=couid)
    dict2 = json.dumps(dict1)
    return dict2

def setFaceBuy_hsb(row,skid,reid,couid):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['bizData[sku_id]'] = getRead(key1=skid)
    dict1['bizData[resource_id]'] = getRead(key1=reid)
    dict1['bizData[pre_get_info][sku_id]'] = getRead(key1=skid)
    dict1['bizData[pre_get_info][resource_id]'] = getRead(key1=reid)
    dict1['bizData[edu_student_info][student_id]'] = getRead(key1='student_id')
    dict1['bizData[edu_student_info][course_id]'] = getRead(key1=couid)
    return dict1

def setFaceBuy_hsb_c(row,skid,reid,cosid,cu_id):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['bizData[sku_id]'] = getRead(key1=skid)
    dict1['bizData[resource_id]'] = getRead(key1=reid)
    dict1['bizData[pre_get_info][sku_id]'] = getRead(key1=skid)
    dict1['bizData[pre_get_info][resource_id]'] = getRead(key1=reid)
    dict1['bizData[edu_student_info][student_id]'] = getRead(key1='student_id')
    dict1['bizData[edu_student_info][course_id]'] = getRead(key1=cosid)
    dict1['bizData[cu_id]'] = getRead(key1=cu_id)
    return dict1

def setNewFaceClass():
    dict1 = json.loads(OperationExcel().getRequestData(255))
    dict1['title'] = 'Pay_班级80'+str(random.randint(1, 99))
    dict1['course_id'] = getRead(key1='course_id_03')
    dict1['begin_time'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    dict1['end_time'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+2505600))
    dict2 = json.dumps(dict1)
    return dict2

def setFaceClass():
    sj = "".join(random.sample('ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789', 6))
    dict1 = json.loads(OperationExcel().getRequestData(256))
    dict1['title'] = 'Pay_正式课-班级售卖'+sj
    dict1['course_id'] = getRead(key1='course_id_03')
    dict1['formal_course']['spec'][0]['spec_value'][0] = getRead(key1='class_id')
    dict1['formal_course']['spec'][0]['class_info']['class_id'] = getRead(key1='class_id')
    dict1['formal_course']['spec'][0]['class_info']['class_name'] = getRead(key1='class_name')
    dict1['formal_course']['spec'][0]['class_info']['class_begin_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    dict1['formal_course']['spec'][0]['class_info']['class_end_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+2505600))
    dict1['formal_course']['spec'][0]['unit_desc'][0] = getRead(key1='class_name')
    dict2 = json.dumps(dict1)
    return dict2

def setCalendarclock():
    sj = "".join(random.sample('ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789', 6))
    dict1 = json.loads(OperationExcel().getRequestData(262))
    dict1['title'] = 'Pay_日历打卡'+sj
    dict1['org_content'][0]['id'] = '1547'+str(int(time.time()*1000))
    dict1['activity_start_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    dict1['activity_stop_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+2505600))
    return dict1

def setCalendarBuy(row,keyid):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['bizData[resource_id]'] = getRead(key1=keyid)
    return dict1

def setCalendarBuy_c(row,keyid,cuid):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['bizData[resource_id]'] = getRead(key1=keyid)
    dict1['bizData[cu_id]'] = getRead(key1=cuid)
    return dict1

def setTaskclock():
    sj = "".join(random.sample('ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789', 6))
    dict1 = json.loads(OperationExcel().getRequestData(267))
    dict1['work_list'][0]['org_content'][0]['id'] = '1547'+str(int(time.time()*1000))
    dict1['work_list'][0]['start_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    dict1['work_list'][0]['stop_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+2505600))
    dict1['title'] = 'Pay_作业打卡'+sj
    dict1['org_content'][0]['id'] = '1547'+str(int(time.time()*1000)+1)
    dict2 = json.dumps(dict1)
    return dict2

def setPassclock():
    sj = "".join(random.sample('ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789', 6))
    dict1 = json.loads(OperationExcel().getRequestData(272))
    dict1['title'] = 'Pay_作业打卡'+sj
    dict1['org_content'][0]['id'] = '1547'+str(int(time.time()*1000))
    dict1['class_hour_list'][0]['org_content'][0]['id'] = '1547'+str(int(time.time()*1000)+1)
    dict2 = json.dumps(dict1)
    return dict2

def setNewTeaching():
    sj = "".join(random.sample('ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789', 6))
    dict1 = json.loads(OperationExcel().getRequestData(277))
    dict1['params[title]'] = 'Pay_教辅周边商品'+sj
    return dict1

def setTeaching(row,keyid):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['bizData[resource_id]'] = getRead(key1=keyid)
    return dict1

def setNewCommunity():
    sj = "".join(random.sample('ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789', 6))
    dict1 = json.loads(OperationExcel().getRequestData(281))
    dict1['title'] = 'Pay_社群'+sj
    return dict1

def setCommunity():
    dict1 = json.loads(OperationExcel().getRequestData(283))
    dict1['bizData[resource_id]'] = getRead(key1='com_id')
    return dict1

def setAnswers():
    dict1 = json.loads(OperationExcel().getRequestData(285))
    dict1['id'] = getRead(key1='q_id')
    return dict1

def setAnswersUser():
    dict1 = json.loads(OperationExcel().getRequestData(286))
    dict1['answerer_id'] = getRead(key1='user_id')
    return dict1

def setAnswers_u(row):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['bizData[product_id]'] = getRead(key1='q_id')
    return dict1

def setAnswers_u1():
    dict1 = json.loads(OperationExcel().getRequestData(289))
    dict1['bizData[product_id]'] = getRead(key1='q_id')
    dict1['bizData[answerer_id]'] = getRead(key1='user_id')
    return dict1

def setAnswers_u2(row,keyid):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['bizData[resource_id]'] = getRead(key1=keyid)
    return dict1

def setNewActivity():
    sj = "".join(random.sample('ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789', 6))
    dict1 = json.loads(OperationExcel().getRequestData(293))
    dict1['params[title]'] = 'Pay_活动管理'+sj
    dict1['params[activity_start_at]'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    dict1['params[activity_end_at]'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+2505600))
    return dict1

def setActivity():
    dict1 = json.loads(OperationExcel().getRequestData(296))
    dict1['bizData[id]'] = getRead(key1='activity_id_9')
    return dict1

def setActivity_o():
    dict1 = json.loads(OperationExcel().getRequestData(297))
    dict1['bizData[resource_id]'] = getRead(key1='activity_id_9')
    dict1['bizData[sku_id]'] = getRead(key1='sku_id')
    return dict1

def setActivity_p():
    field_content='[[{"name":"姓名","content":"自动化测试机器人","required":"true","type":2},{"name":"手机号码","content":"18814480943","required":"true","type":1}]]'
    dict1 = json.loads(OperationExcel().getRequestData(298))
    dict1['bizData[resource_id]'] = getRead(key1='activity_id_9')
    dict1['bizData[sku_id]'] = getRead(key1='sku_id')
    dict1['bizData[ticket_id]'] = getRead(key1='ticket_id')
    dict1['bizData[pre_get_info][resource_id]'] = getRead(key1='activity_id_9')
    dict1['bizData[pre_get_info][sku_id]'] = getRead(key1='sku_id')
    dict1['bizData[field_content]'] = field_content
    return dict1

def setActivity_c():
    field_content = '[[{"name":"姓名","content":"自动化测试机器人","required":"true","type":2},{"name":"手机号码","content":"18814480943","required":"true","type":1}]]'
    dict1 = json.loads(OperationExcel().getRequestData(299))
    dict1['bizData[resource_id]'] = getRead(key1='activity_id_9')
    dict1['bizData[cu_id]'] = getRead(key1='cu_id_23')
    dict1['bizData[sku_id]'] = getRead(key1='sku_id')
    dict1['bizData[ticket_id]'] = getRead(key1='ticket_id')
    dict1['bizData[pre_get_info][resource_id]'] = getRead(key1='activity_id_9')
    dict1['bizData[pre_get_info][sku_id]'] = getRead(key1='sku_id')
    dict1['bizData[field_content]'] = field_content
    return dict1

def setWXZapp_01(row):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['shop_id'] = getRead(key1='shop_id')
    dict1['uuid'] = getRead(key1='uuid')
    dict1['app_id'] = getRead(key1='shop_id')
    dict1['api_token'] = getRead(key1='api_token')
    dict1['user_id'] = getRead(key1='Appuser_id')
    dict2=json.dumps(dict1)
    return dict2

def setWXZapp_02():
    dict1 = json.loads(OperationExcel().getRequestData(303))
    dict1['shop_id'] = getRead(key1='shop_id')
    dict1['uuid'] = getRead(key1='uuid')
    dict1['app_id'] = getRead(key1='shop_id')
    dict1['api_token'] = getRead(key1='api_token')
    dict1['user_id'] = getRead(key1='Appuser_id')
    return dict1

def setWXZapp_03(row):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['shop_id'] = getRead(key1='shop_id')
    dict1['uuid'] = getRead(key1='uuid')
    dict1['app_id'] = getRead(key1='shop_id')
    dict1['api_token'] = getRead(key1='api_token')
    dict1['user_id'] = getRead(key1='Appuser_id')
    return dict1

def setWXZapp_04(row):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['shop_id'] = getRead(key1='shop_id')
    dict1['uuid'] = getRead(key1='uuid')
    dict1['app_id'] = getRead(key1='shop_id')
    dict1['api_token'] = getRead(key1='api_token')
    dict1['user_id'] = getRead(key1='Appuser_id')
    dict1['buz_data']['product_id'] = getRead(key1='APP_svip_id')
    dict1['buz_data']['resource_id'] = getRead(key1='APP_resource_id')
    dict2=json.dumps(dict1)
    return dict2

def setWXZapp_05():
    dict1 = json.loads(OperationExcel().getRequestData(310))
    dict1['shop_id'] = getRead(key1='shop_id')
    dict1['resource_id'] = getRead(key1='APP_goods_id')
    dict1['uuid'] = getRead(key1='uuid')
    dict1['app_id'] = getRead(key1='shop_id')
    dict1['api_token'] = getRead(key1='api_token')
    dict1['user_id'] = getRead(key1='Appuser_id')
    dict2=json.dumps(dict1)
    return dict2

def setWXZapp_06(row):
    dict1 = json.loads(OperationExcel().getRequestData(row))
    dict1['shop_id'] = getRead(key1='shop_id')
    dict1['uuid'] = getRead(key1='uuid')
    dict1['app_id'] = getRead(key1='shop_id')
    dict1['api_token'] = getRead(key1='api_token')
    dict1['user_id'] = getRead(key1='Appuser_id')
    dict1['buz_data']['resource_type'] = getRead(key1='APP_goods_type')
    dict1['buz_data']['product_id'] = getRead(key1='APP_goods_id')
    dict1['buz_data']['resource_id'] = getRead(key1='APP_goods_id')
    dict2=json.dumps(dict1)
    return dict2
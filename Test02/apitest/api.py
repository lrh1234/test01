# -*- coding: utf-8 -*-
# 2022/7/21 17:39
import requests
'''
url:http://trip.imooc.zhaeedu.com/api
url_regis:http://trip.imooc.zhaedu.com/api//accounts/user/register/   
url_login:http://trip.imooc.zhaedu.com/api//accounts/user/login/
url_view:"http://trip.imooc.zhaedu.com/api//accounts/user/detail/"
    
'''
phone = "13770001231"       # API测试数据
nick = "渴望力量"
password = "123456"


# 注册账户API
url_regis = "http://trip.imooc.zhaedu.com/api/accounts/user/register/"    # 注册API
data_regis = {"username": phone, "nickname": nick, "password": password}    # 定义注册API传入信息
res_regis = requests.post(url=url_regis, data=data_regis)
print(res_regis.text)





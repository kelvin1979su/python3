#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#    Life is short , you need Python !!!
#    Kelvin® kelvin.su@qq.com , Version 1.0 for Python 3.7.2 2019-05-20
'''
    在Windows 10 专业版 + Python 3.7.2 测试没问题
    在CentOS 7.6 1810 + Python3.7.3 测试没问题
'''

import time
import hmac

#用户帐号存放位置
user_pass_conf = open('/home/config/user.conf')
while 1:
    line = user_pass_conf.readline()
    if not line:
        break
    line = line.split(',')
    Username = line[1]
    Password = line[2].replace("\r\n","").replace("\n","")

times=2    #记录用户输入帐号次数

while times >= 0:
    input_name = input("请输入帐号：")
    input_passwd = input("请输入密码：")
    
    #将输入的口令转换成MD5加密文件
    change = hmac.new('kelvin'.encode('utf-8'))
    change.update(input_passwd.encode('utf-8'))
    change_passwd=change.hexdigest()
       
    #当输入的帐号及口令正确，提示登录和日期，程序结束
    if Username==input_name and Password==change_passwd:
        print(Username, "登陆成功！现在日期是", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        break
    #当输入的帐号和密码为空时，提示不能为空，并提示还有几次剩余次数
    elif input_passwd=="" or input_name=="":
        print("帐号或密码不能为空！")
        print("还有"+str(times)+"次机会！\n")
    #当输入的帐号和密码不为空，且次数不等于0提示错误，并提示还有几次剩余次数
    else:
        if times != 0:
            print("\n帐号或密码输入错误")
            print("还有"+str(times)+"次机会！\n")
        else:
            print("当前三次输入错误，程序结束！")
    times-=1

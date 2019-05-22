#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#    Life is short , you need Python !!!
#    Kelvin® kelvin.su@qq.com , Version 1.0 for Python 3.7.2 2019-5-19
#    加密算法模块
'''
    在 Windows 10 专业版 + Pythone 3.7.2 环境下测试成功
    在 CentOS 7.6 1810 + Python 3.7.3 环境下测试成功
'''
import hashlib

input_text = input("请输入：")

#MD5加密
hash = hashlib.md5()
hash.update(input_text.encode('utf-8'))
print("MD5密文：",hash.hexdigest())

#sha1加密
hash = hashlib.sha1()
hash.update(input_text.encode('utf-8'))
print("sha1密文：",hash.hexdigest())

#sha256加密
hash = hashlib.sha256()
hash.update(input_text.encode('utf-8'))
print("sha256密文：",hash.hexdigest())

#sha384加密
hash = hashlib.sha384()
hash.update(input_text.encode('utf-8'))
print("sha384密文：",hash.hexdigest())

#sha512加密
hash = hashlib.sha512()
hash.update(input_text.encode('utf-8'))
print("sha512密文：",hash.hexdigest())

#自定义key加密
#以上加密算法虽然很厉害，但仍然存在缺陷，通过撞库可以反解。所以必要对加密算法中添加自定义key再来做加密
hash = hashlib.md5('kelvin'.encode('utf-8'))
hash.update(input_text.encode('utf-8'))
print("自定义key密文：",hash.hexdigest())

#hmac加密
import hmac
h = hmac.new('python'.encode('utf-8'))
h.update(input_text.encode('utf-8'))
print("hmac密文：",h.hexdigest())

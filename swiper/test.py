import json
import pickle
from django.core.cache import cache

'''
小结
1.获取短信验证码
获取验证码，通过json字符串返回
2.通过验证码登录注册
（1）需要用手机和验证码登录注册 登录时去创建用户模型models 没有这个用户则去注册这个用户并登录
所以我们需要用到这个模型models
（2）通过前后端端分离 使用用rander_json返回（也就是用http这个文件返回 因为经常要用到 
json.dunmps()把对象转为字典）
2.如何取到发给手机的验证码
通过cache保存对象到内存当中 然后反序列化读取出来

'''

class A:
    name = 'hl'
    # def __init__(self,age):
    #     self.age = age

def add(self,a,b):
    return a+b
A.add = add
b = A()
print(b.add(1,2))
# a = A(19)
# print(a.age)


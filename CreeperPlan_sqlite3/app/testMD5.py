#! CreeperPlan   python
#  44719
# -*- coding: utf-8 -*-
# @Time    : 2022/6/29 9:56
# @Author  : 傑君
# @File    : testMD5.py
# @Software: PyCharm
import hashlib

name='pjj'
passwd='123456'

m=hashlib.md5()
m.update('我是'.encode('utf-8'))
m.update(passwd.encode('utf-8'))
m.update('你爹'.encode('utf-8'))
res=m.hexdigest()
print(res)
import difflib

i="abcdqweret"
j="123456789"
print(float(round(difflib.SequenceMatcher(None, i, j).quick_ratio(), 2)))


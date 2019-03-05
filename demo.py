#！/usr/bin/evn python3
# encoding: utf-8  

""" 
@author: 周广坤 
@license: Apache Licence  
@contact: 1140110922@qq.com 
@site:  
@software: PyCharm 
@file: demo.py 
@time: 2019/3/5 8:31 
"""
import re
data = '['"http://finance.sina.cn/2019-03-05/detail-ihsxncvf9859761.d.html"']'
a = re.findall('([a-z]+\://[a-zA-Z0-9\./-]+)',data)
print(a)
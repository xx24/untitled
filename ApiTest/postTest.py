# ！/usr/bin/python
#author:xx


import requests
import json

data={}
header={}
response=requests.post(url='https://www.lagou.com/zhaopin/',
                       data=data,
                       header=header)
'''以json格式显示，ensure_ascii=False作用是显示中文'''
print(json.dumps(response.json(),indent=True,ensure_ascii=False))
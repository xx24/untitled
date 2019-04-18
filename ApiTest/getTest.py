# ！/usr/bin/python
#author:xx

import requests

user={'search_text':'小飞象','cat':1002}
# response=requests.get(url='https://movie.douban.com/',params=user)
# print(response.status_code)
# # print(response.text)
# print(response.content.decode('utf-8'))


'''在6s内得到响应，否则提示连接超时'''
# response2=requests.get('http://www.baidu.com',time=6)
# print(response2.text)


r3=requests.get(url='https://www.12306.cn/mormhweb/',verify=False)
print(r3.content.decode('utf-8'))
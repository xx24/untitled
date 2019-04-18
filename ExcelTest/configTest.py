# ！/usr/bin/python
#author:xx

import configparser
import os

def dirfile(filename=None):
	return os.path.join(os.path.dirname(__file__),filename)

def getlinux():
	list=[]
	config = configparser.ConfigParser()
	config.read(dirfile('config.ini'))
	ip = config.get('linux', 'ip')
	port = config.get('linux', 'port')
	username = config.get('linux', 'username')
	password = config.get('linux', 'password')
	'''获取配置文件中所有节点'''
	print(config.sections())
	'''获取linux节点下所有内容'''
	print(config.options('linux'))
	'''检查节点下是否存在某内容'''
	config.has_option('linux','ip')
	list.append(ip)
	list.append(port)
	list.append(username)
	list.append(password)
	return list

print(getlinux())

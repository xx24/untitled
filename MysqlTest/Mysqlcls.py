# ！/usr/bin/python
#author:xx

import pymysql

class MysqlHelp:
	def conn(self):
		conn=pymysql.connect(
			host='127.0.0.1',
			user='root',
			password='Xx.675737',
			db='user'
		)
		return conn

	def get_one(self,sql,params):
		cur=self.conn().cursor()
		cur.execute(sql,params)
		result=cur.fetchone()
		return result

def checkValid(username,password):
	opera=MysqlHelp()
	sql='select * from info where username=%s and password=%s'
	params=(username,password)
	result=opera.get_one(sql=sql,params=params)
	return result

def info():
	username=input('输入用户名：\n')
	password=input('请输入密码：\n')
	resule=checkValid(username=username,password=password)
	if resule:
		print('login success')
	else:print('login failed')

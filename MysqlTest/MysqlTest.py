# ！/usr/bin/python
#author:xx

import pymysql

'''查询'''
def connsqlSearch():
	try:
		con = pymysql.connect(
			host='127.0.0.1',
			user='root',
			password='Xx.675737',
			database='user'
		)
	except Exception as e:
		print(e.args)
	else:
		cur=con.cursor()
		sql='select * from info'
		'''执行sql语句'''
		cur.execute(sql)

		'''查询结果就一条时使用，返回单个元祖'''
		data1=cur.fetchone()
		'''如果查询结果有多个，返回多条结果'''
		data=cur.fetchall()
		print(data)
	finally:
		cur.close()
		con.close()


'''新增'''
def insertSql():
	try:
		con = pymysql.connect(
			host='127.0.0.1',
			user='root',
			password='Xx.675737',
			database='user'
		)
	except Exception as e:
		print(e.args)
	else:
		cur = con.cursor()
		sql = 'insert into info values (%s,%s,%s,%s)'
		'''添加多条数据用executemany，添加一条数据用execute'''
		params=[
			(6,'xx',12,'拱墅区'),
			(4, 'xx', 12, '拱墅区'),
			(5, 'xx', 12, '拱墅区')
		]
		'''执行sql语句'''
		cur.executemany(sql,params)
		con.commit()
	finally:
		cur.close()
		con.close()

insertSql()
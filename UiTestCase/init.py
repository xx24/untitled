# ！/usr/bin/python
#author:xx

import unittest
from selenium import webdriver

class Init(unittest.TestCase):
	'''打开浏览器'''
	@classmethod
	def setUpClass(cls) -> None:
		cls.driver=webdriver.Chrome()
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(30)
		cls.driver.get('http://www.baidu.com')

	'''关闭浏览器'''
	@classmethod
	def tearDownClass(cls) -> None:
		cls.driver.quit()
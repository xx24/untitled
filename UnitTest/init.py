# ！/usr/bin/python
#author:xx


import unittest
from selenium import webdriver

class Init(unittest.TestCase):

	def setUp(self) -> None:
		self.driver=webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.driver.get('http://www.baidu.com')

	def tearDown(self) -> None:
		self.driver.quit()

# ！/usr/bin/python
#author:xx

import unittest
from UiTestCase.init import *

class BaiduSearch(Init):
	def test_enable(self):
		'''百度首页输入框是否可编辑'''
		input1=self.driver.find_element_by_id('kw')
		self.assertTrue(input1.is_enabled())

	def test_search(self):
		'''断言输入值是否等于期望值'''
		input2=self.driver.find_element_by_id('kw')
		input2.send_keys('selenium')
		self.driver.find_element_by_id('su').click()
		self.assertEqual(input2.get_attribute('value'),'selenium')

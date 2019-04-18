# ！/usr/bin/python
#author:xx

import unittest
from UnitTest.init import *

class BaiduAssert(Init):

	'''断言两个 值与类型是否都相等'''
	def baiduTitle(self):
		self.assertEqual(self.driver.title,'百度一下，你就知道')

	'''断言结果是否为true'''
	def baiduInput(self):
		input1=self.driver.find_element_by_id('kw')
		self.assertTrue(input1.is_enabled())

	'''断言期望结果是否包含在实际结果中'''
	def baiduTitleIn(self):
		self.assertIn('百度',self.driver.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)
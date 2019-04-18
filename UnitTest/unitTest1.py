# ！/usr/bin/python
#author:xx

import unittest
from UnitTest.init import *

class BaiduSearch(Init):
	def test_search(self):
		self.driver.find_element_by_id('kw').send_keys('你好')

if __name__ == '__main__':
    unittest.main(verbosity=2)
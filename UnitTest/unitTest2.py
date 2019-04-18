# ！/usr/bin/python
#author:xx


import unittest
from UnitTest.init import *
from selenium import webdriver


class BaiduLink(Init):

	@unittest.skip('该功能已删除')
	def test_news(self):
		self.driver.find_element_by_link_text('新闻').click()

	def test_map(self):
		self.driver.find_element_by_link_text('地图').click()



if __name__ == '__main__':
    unittest.main(verbosity=2)

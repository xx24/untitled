# ！/usr/bin/python
#author:xx

import unittest
from UiTestCase.init import *

class BaiduLink(Init):
	def test_news(self):
		'''百度首页新闻链接是否正常跳转'''
		self.driver.find_element_by_link_text('新闻').click()
		self.assertEqual(self.driver.current_url,'http://news.baidu.com/')
		self.driver.back()

	def test_map(self):
		'''百度首页地图链接是否正常跳转'''
		self.driver.find_element_by_link_text('地图').click()
		self.assertEqual(self.driver.current_url, 'https://map.baidu.com/@13376484.03,3517857.39,12z')

		self.driver.back()
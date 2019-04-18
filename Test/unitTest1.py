# ！/user/bin/python
# ! -*- coding:utf-8 -*-


import unittest
from selenium import webdriver

class f1(unittest.TestCase):

	def setUp(self) -> None:
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.driver.get('http://www.baidu.com')

	def tearDown(self) -> None:
		self.driver.quit()

	def test_001(self):
		self.driver.find_element_by_link_text('新闻').click()

	def test_002(self):
		self.driver.find_element_by_link_text('地图').click()

if __name__ == '__main__':
    unittest.main(verbosity=2)
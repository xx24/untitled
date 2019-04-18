# ！/user/bin/python
# ! -*- coding:utf-8 -*-


import unittest
from selenium import webdriver


class baiduTest(unittest.TestCase):
	@classmethod
	def setUpClass(cls) -> None:
		cls.driver=webdriver.Chrome()
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(30)
		cls.driver.get('http://www.baidu.com')

	@classmethod
	def tearDownClass(cls) -> None:
		cls.driver.quit()

	def test_001(self):
		self.driver.find_element_by_link_text('新闻').click()
		self.driver.back()

	def test_002(self):
		self.driver.find_element_by_link_text('地图').click()
		self.driver.back()

	def test_input(self):
		self.driver.find_element_by_id('kw').send_keys('nihao')


'''分别add各个测试用例'''
# if __name__ == '__main__':
#     suit=unittest.TestSuite()
#     suit.addTest(baiduTest('test_002'))
#     suit.addTest(baiduTest('test_001'))
#     unittest.TextTestRunner(verbosity=2).run(suit)

'''add测试类'''
# if __name__ == '__main__':
#     suit=unittest.TestSuite()
#     suit.addTest(baiduTest)
#     unittest.TextTestRunner(verbosity=2).run(suit)


'''加载测试类执行'''
if __name__ == '__main__':
    suit=unittest.TestLoader().loadTestsFromTestCase(baiduTest)
    unittest.TextTestRunner(verbosity=2).run(suit)

'''如果存在多个测试类需要执行，就可加载整个模块执行'''
if __name__ == '__main__':
    suit=unittest.TestLoader().loadTestsFromModule('unitTestCls.py')
    unittest.TextTestRunner(verbosity=2).run(suit)

# ！/usr/bin/python
#author:xx

import unittest
import os
import HtmlTestRunner
import time

def allTests():
	suit=unittest.TestLoader().discover(
		start_dir=os.path.dirname(__file__),
		pattern='test_baidu*.py',
		top_level_dir=None)
	return suit

def getNowTime():
	return time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))

def run():
	HtmlTestRunner.HTMLTestRunner(report_title='自动化测试报告',descriptions='自动化测试报告详情').run(allTests())


if __name__ == '__main__':
    run()
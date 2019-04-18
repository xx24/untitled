# ！/usr/bin/python
#author:xx

import requests
import ddt
import unittest
from UiTestCase.init import *

url='https://www.lagou.com/jobs/positionAjax.json?city=%E6%9D%AD%E5%B7%9E&needAddtionalResult=false'
def getHeader():
	headers={
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Cookie':'user_trace_token=20190409192716-1fe5f6ca-9504-4287-bd21-f5c9da143a90; _ga=GA1.2.917802722.1554809237; LGUID=20190409192717-6e499cac-5aba-11e9-a1c1-525400f775ce; WEBTJ-ID=20190417112744-16a29560570a1-00699219c1c27a-366c7e04-1296000-16a29560571cbf; _gid=GA1.2.742014307.1555471665; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1554809247,1554809268,1554809284,1555471665; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216a2956ad9dcb-0bb20b4116ecff-366c7e04-1296000-16a2956ad9e1c9%22%2C%22%24device_id%22%3A%2216a2956ad9dcb-0bb20b4116ecff-366c7e04-1296000-16a2956ad9e1c9%22%7D; sajssdk_2015_cross_new_user=1; LG_LOGIN_USER_ID=ffb718aaad4ef6cd9bba855947431acc8f1682a675e2699f; _putrc=348FBE08DDEFBC70; JSESSIONID=ABAAABAAAGFABEF05259146F8BFE3B7EBB349B31F3A6AD8; login=true; unick=%E5%A4%8F%E9%9C%9E; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=6; gate_login_token=08a3528557a3a4324e327c545c35abf63d6477baad7eeb04; index_location_city=%E6%9D%AD%E5%B7%9E; TG-TRACK-CODE=index_search; X_MIDDLE_TOKEN=ce9a69eb262f192ce596bca173b664a0; _gat=1; LGSID=20190417134029-4f250e19-60d3-11e9-938d-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588%3Fcity%3D%25E6%259D%25AD%25E5%25B7%259E%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588%3Fcity%3D%25E6%259D%25AD%25E5%25B7%259E%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; X_HTTP_TOKEN=19e4b5015ac2c45f0469745551d9353668cc5e8d96; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1555479640; LGRID=20190417134040-55bce554-60d3-11e9-888b-525400f775ce; SEARCH_ID=31bcaefd93ef449394e6a0c2c4ab207e',
		'Referer':'https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?city=%E6%9D%AD%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput=',
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
	return headers

# @ddt.ddt
class LaGou(unittest.TestCase):
	# @ddt.data([1, 2, 3])
	# @ddt.unpack
	def test_lagou(self, page=2):
		r = requests.post(
			url=url,
			headers=getHeader(),
			data={'first': False, 'pn': page, 'kd': '测试工程师'})
		self.assertEqual(r.json()['success'],False)

if __name__ == '__main__':
    unittest.main(verbosity=2)
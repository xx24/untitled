# ！/usr/bin/python
#author:xx


import csv
import requests
#
# '''以列表格式读取'''
# def resdCseTest():
# 	with open('csv.csv','r') as f:
# 		reader=csv.reader(f)
# 		next(reader)
# 		for item in reader:
# 			print(list(item))
#
#
# '''以字典格式读取'''
# def readcevDict():
# 	with open('csv.csv','r') as f:
# 		reader=csv.DictReader(f)
# 		for item in reader:
# 			print(dict(item))


url='https://www.lagou.com/jobs/positionAjax.json?city=%E6%9D%AD%E5%B7%9E&needAddtionalResult=false'
def getHeader():
	headers={
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Cookie':'user_trace_token=20190409192716-1fe5f6ca-9504-4287-bd21-f5c9da143a90; _ga=GA1.2.917802722.1554809237; LGUID=20190409192717-6e499cac-5aba-11e9-a1c1-525400f775ce; WEBTJ-ID=20190417112744-16a29560570a1-00699219c1c27a-366c7e04-1296000-16a29560571cbf; _gid=GA1.2.742014307.1555471665; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1554809247,1554809268,1554809284,1555471665; LGSID=20190417112744-c3c952c1-60c0-11e9-881d-525400f775ce; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=sp0.baidu.com; PRE_SITE=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZNKw_0R9kB0FNkUs0_MUuT00000P7aZNC000005Q0k9_.THL0oUhY1x60UWdBmy-bIfK15yDLPhR1nWIWnj0snWcYmH60IHYzrjI7nHuAnYc3n17jnbn4PH0Yf1TLnbf1nDcsnWDLwfK95gTqFhdWpyfqn1czPjRYPWbvPausThqbpyfqnHm0uHdCIZwsT1CEQLILIz4_myIEIi4WUvYEUZ0EpZwVUaqsULPGIA-EUB4CIAd_5LNYUNq1ULNzmvRqUNqWu-qWTZwxmh7GuZNxTAPBI0KWThnqPHDYnHD%26tpl%3Dtpl_11534_19713_15764%26l%3D1511867089%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E3%252580%252591-%252520%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E5%2525AE%25259E%2525E6%252597%2525B6%2525E6%25259B%2525B4%2525E6%252596%2525B0%21%2526xp%253Did%28%252522m3224546964_canvas%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D210%26ie%3Dutf-8%26f%3D8%26tn%3Dbaidu%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26oq%3Dpython%2525E8%2525AF%2525BB%2525E5%25258F%252596csv%2525E6%252596%252587%2525E4%2525BB%2525B6%26rqlang%3Dcn%26inputT%3D750925%26bs%3Dpython%25E8%25AF%25BB%25E5%258F%2596csv%25E6%2596%2587%25E4%25BB%25B6; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fposition.html%3Futm_source%3Dm_cf_cpt_baidu_pcbt; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216a2956ad9dcb-0bb20b4116ecff-366c7e04-1296000-16a2956ad9e1c9%22%2C%22%24device_id%22%3A%2216a2956ad9dcb-0bb20b4116ecff-366c7e04-1296000-16a2956ad9e1c9%22%7D; sajssdk_2015_cross_new_user=1; LG_LOGIN_USER_ID=ffb718aaad4ef6cd9bba855947431acc8f1682a675e2699f; _putrc=348FBE08DDEFBC70; JSESSIONID=ABAAABAAAGFABEF05259146F8BFE3B7EBB349B31F3A6AD8; login=true; unick=%E5%A4%8F%E9%9C%9E; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=6; gate_login_token=08a3528557a3a4324e327c545c35abf63d6477baad7eeb04; index_location_city=%E6%9D%AD%E5%B7%9E; TG-TRACK-CODE=index_search; X_MIDDLE_TOKEN=ce9a69eb262f192ce596bca173b664a0; _gat=1; X_HTTP_TOKEN=19e4b5015ac2c45f6581745551d9353668cc5e8d96; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1555471857; LGRID=20190417113057-3675a89b-60c1-11e9-881d-525400f775ce; SEARCH_ID=92df604a2f3646a2a8172d3dbbe32bcd',
		'Referer':'https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?city=%E6%9D%AD%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput=',
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
	return headers

def lagou(page=2):
	positions = []
	r=requests.post(
		url=url,
		headers=getHeader(),
		data={'first':'False','pn':page,'kd':'测试工程师'})
	for i in range(15):
		city=r.json()['content']['positonResult']['result'][i]['city']
		companyFullName=r.json()['content']['positonResult']['result'][i]['companyFullName']
		workYear=r.json()['content']['positonResult']['result'][i]['workYear']
		salary=r.json()['content']['positonResult']['result'][i]['salary']
		companyLabelList=r.json()['content']['positonResult']['result'][i]['companyLabelList']
		position = {
			'城市':city,
			'公司名称':companyFullName,
			'工作年限':workYear,
			'薪资':salary,
			'公司标签':companyLabelList}
	    positions.append(position)
	return positions


def writeCsv():
	headers={'城市','公司名称','工作年限','薪资','公司标签'}
	with open('lagou.csv','a',newline='',encoding='gdk') as f:
		writer=csv.DictWriter(f,headers)
		writer.writeheader()
	'''将1到30页的数据'写入csv文件'''
	for item in range(1,31):
		positions=lagou(item)
		writer.writerows(positions)


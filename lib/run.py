# coding=utf-8

# import re
# from spider import Spider

# url = 'http://shouji.baidu.com/software/503_board_100_01/list_2.html'
# pattern = re.compile(r'''<span[^>]*quickdown[^>]*
# 						 data-tj="[a-z]+_(\d+)[^>]*		# 应用Id
# 						 data_name="([^"]+)"[^>]*			# 应用名
# 						 data_package="([^"]+)"[^>]* 		# 包名
# 						 data_versionname="([^"]+)"[^>]*	# 版本号
# 						 data_icon="([^"]+)"[^>]*			# 图标
# 						 >''', re.X)
# data = {'start': 0, 'num': 2, 'xhr': 1}
# def urlGenerator():
# 	url = 'http://shouji.baidu.com/software/503_board_100_01/list_%d.html'
# 	for i in range(5):
# 		yield url % (i + 1)

# spider = Spider(pattern, urlGenerator())
# result = spider.fetch()
# print(result)

from mysql import DbMysql

conf = {
	'host': 'localhost',
	'user': 'root',
	'passwd': '1234',
	'db': 'test'
}

db = DbMysql(**conf)
res = db.table('tb_1').update({'name': 'xiaolv2'}, {'name': 'xiaolv'})
print(res)
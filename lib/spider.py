# coding=utf-8

import urllib.request as r
import urllib.parse as p

class Spider(object):

	# 构造函数
	def __init__(self, pattern=None, url=None):
		self.__pattern = pattern
		self.__url = url

	# 设置匹配模版
	def pattern(self, pattern):
		self.__pattern = pattern

	# 设置url生成器
	def url(self, url):
		self.__url = url

	# 抓取数据
	def fetch(self, url='', *, method='GET', data=None):
		url = url or next(self.__url)
		if (not self.__pattern or not url):
			print('pattern or url is none')
			return

		response = self.__request(url, method, data)
		return self.__pattern.findall(response)

	# 发起请求get/post
	def __request(self, url, method='GET', data=None):
		postData = None
		if (method.upper() == 'POST'):
			data = data or {}
			postData = p.urlencode(data).encode()

		response = r.urlopen(url, postData).read()
		return str(response.decode())

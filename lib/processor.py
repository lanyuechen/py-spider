# coding=utf-8

from threading import Thread
from queue import Queue

queue = Queue(10)

class ListThread(Thread):
	def run(self):
		global queue
		while True:
			# 获取数据，插入到队列中
			queue.put(res)
			# todo something
		

class DetailThread(Thread):
	def run(self):
		global queue
		while True:
			res = queue.get()
			queue.task_done()
			# todo something
			

ListThread().start()
DetailThread().start()
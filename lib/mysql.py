# coding=utf-8

import pymysql
import warnings

warnings.filterwarnings("ignore")	# 去除警告

class DbMysql(object):

	__table = ''
	__field = '*'
	__where = '1'
	__order = ''
	__limit = ''

	def __init__(self, **kw):
		self.connect(**kw)

	def connect(self, **kw):
		self.__conn = pymysql.connect(
			host = kw.get('host', 'localhost'),
			user = kw.get('user'),
			passwd = kw.get('passwd'),
			db = kw.get('db'),
			port = kw.get('port', 3306),
			charset = kw.get('charset', 'utf8'),
			cursorclass = pymysql.cursors.DictCursor
		)

	def table(self, table):
		self.__table = table
		self.__field = '*'
		self.__where = '1'
		self.__order = ''
		self.__limit = ''
		return self

	def field(self, field):
		if (type(field) is list):
			self.__field = '`' + '`, `'.join(field) + '`'
		elif (type(field) is str):
			self.__field = field
		else:
			self.__field = '*'
		return self

	def where(self, where):
		if (type(where) is dict):
			w = '1'
			for k, v in where.items():
				if (type(v) is str):
					v = "'" + v + "'"
				w += " AND `%s`=%s" % (k, v)
			self.__where = w
		elif (type(where) is str):
			self.__where = where
		else:
			self.__where = '1'
		return self

	def order(self, order):
		self.__order = order
		return self

	def limit(self, limit, skip=0):
		if (skip > 0):
			limit, skip = skip, limit
		self.__limit = '%d, %d' % (skip, limit)
		return self

	def select(self, sql=None, all=True):
		if (not sql):
			sql = "SELECT %s FROM %s WHERE %s" % (self.__field, self.__table, self.__where)
			sql += " ORDER BY " + self.__order if self.__order else ''
			sql += " LIMIT " + self.__limit if self.__limit else ''
		cur = self.__conn.cursor()
		cur.execute(sql)
		data = cur.fetchall() if all else cur.fetchone()
		cur.close()
		return data

	def selectOne(self, sql=None):
		return self.select(sql, False)

	def insert(self, data):
		keys = []
		vals = []
		for k, v in data.items():
			keys.append('`%s`' % (k))
			vals.append(self.__val(v))
		sql = "INSERT INTO %s (%s) VALUES (%s)" % (self.__table, ', '.join(keys), ', '.join(vals))
		self.execute(sql)

	def update(self, data, where=None):
		if (where):
			self.where(where)
		setData = []
		for k, v in data.items():
			setData.append("`%s`=%s" % (k, self.__val(v)))
		sql = "UPDATE %s SET %s WHERE %s" % (self.__table, ', '.join(setData), self.__where)
		self.execute(sql)

	def delete(self, where=None):
		if (where):
			self.where(where)
		sql = "DELETE FROM %s WHERE %s" % (self.__table, self.__where)

	def execute(self, sql):
		cur = self.__conn.cursor()
		cur.execute(sql)
		self.__conn.commit()
		cur.close()

	def __val(self, val):
		if (type(val) is str):
			val = "'" + val + "'"
		return val
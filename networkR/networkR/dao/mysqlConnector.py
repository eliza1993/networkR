#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb



class mysqlConnector(object):
	def __init__(self):
		pass
		
	def openDb(host = "127.0.0.1",port = 3306,user = "root",passwd = "",dbname = "Spider" ,charset='utf8'):
		"""
			打开数据库连接
		"""
		db = MySQLdb.connect(host,port,user,passwd ,dbname,charset)


	def closeDb(database = None):
		"""
			关闭数据库连接
		"""
		if not database:
			database.close()
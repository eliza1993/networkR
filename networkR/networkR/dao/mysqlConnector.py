#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb



class mysqlConnector(object):
	def __init__(self):
		pass
		
	def openDb(self,host = '127.0.0.1',user = 'root',passwd = '',dbname = 'Spider' ,charset='utf8'):
		"""
			打开数据库连接
		"""
		db = MySQLdb.connect(host,user,passwd ,dbname,charset)

		return db


	def closeDb(self,database = None):
		"""
			关闭数据库连接
		"""
		if not database:
			database.close()
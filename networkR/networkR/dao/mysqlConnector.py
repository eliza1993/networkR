#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb



class mysqlConnector(object):
	def __init__(self):
		pass
		
	def openDb(self,host = '172.16.111.87',user = 'root',passwd = '',dbname = 'Spider' ):
		"""
			打开数据库连接
		"""
		db = MySQLdb.connect(host,user,passwd,dbname,charset="utf8")

		return db


	def closeDb(self,database = None):
		"""
			关闭数据库连接
		"""
		if not database:
			database.close()
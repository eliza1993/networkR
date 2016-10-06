import MySQLdb

import mysqlConnector
class GrabSite(object):
	"""docstring for GrabSite"""

	insert_sql = "insert into "+
	"GrabSite(siteDomain,siteName,webPageCount,totalOutLinkCuont,siteStatus,siteType,createTime,startGrabTime,endGrabTime) "+
	"values(%s,%s,%d,%d,%s,%s,%s,%s,%s);"
	def __init__(self,mysqlConn):
		self.mysqlConn = mysqlConn


	def get_cursor(self):
		return mysqlConn.cursor()

	def insert_one(self,items = {}):
		if items is None:
			print 'items is None'
			return

		if len(items) != 9:
			print 'items len error'
			return

		item_value = []

		item_value.append(items['siteDomain'])
		item_value.append(items['siteName'])
		item_value.append(items['webPageCount'])
		item_value.append(items['totalOutLinkCuont'])
		item_value.append(items['siteStatus'])
		item_value.append(items['siteType'])
		item_value.append(items['createTime'])
		item_value.append(items['startGrabTime'])
		item_value.append(items['endGrabTime'])

		cursor = self.get_cursor()
		cursor.execute(insert_sql,item_value)
		conn.commit()


	def query_grab_site_by_status(self,items = {}):
		query_sql =  "select * from GrabSite where siteStatus = '%s'" % (items['siteStatus'])
		cursor = self.get_cursor()
		cursor.execute(query_sql)
		results = cursor.fetchall()
		if len(results) > 0:
			return results[0]
		return results

	def query_grab_site_by_domain(self,items = {}):
		query_sql =  "select * from GrabSite where siteDomain = '%s'" % (items['siteDomain'])
		cursor = self.get_cursor()
		cursor.execute(query_sql)
		results = cursor.fetchall()
		if len(results) > 0:
			return results[0]
		return results

	def query(self,items = []):
		pass

	def update(self,items = []):
		pass




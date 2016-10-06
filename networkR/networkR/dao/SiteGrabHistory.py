import mysqlConnector

class SiteGrabHistory(object):
	"""docstring for SiteGrabHistory"""
	def __init__(self,mysqlConn):
		self.mysqlConn = mysqlConn

	def get_cursor(self):
		return mysqlConn.cursor()
	def insert_one(self,items = []):
		insert_sql = "insert into SiteGrabHistory(siteDomain,url,grabStatus,innerPageCount,outPageCount,createTime,lastUpdateTime) "+
		"values(%s,%s,%s,%d,%d,%s,%s)"

		insert_item  = []
		insert_item.append(items['siteDomain'])
		insert_item.append(items['url'])
		insert_item.append(items['grabStatus'])
		insert_item.append(items['innerPageCount'])
		insert_item.append(items['outPageCount'])
		insert_item.append(items['createTime'])
		insert_item.append(items['lastUpdateTime'])
		cursor = self.get_cursor()
		cursor.execute(insert_sql,insert_item)
		cursor.commit()
		


	def query_by_domain_and_status(self,items = []):
		query_sql = "select * from SiteGrabHistory where siteDomain = '%s' and grabStatus = '%s' order by id asc limit 100" % (items['siteDomain'],items['grabStatus'])
		cursor = self.get_cursor()
		cursor.execute(query_sql)
		results = cursor.fetchall()
		return results


	def update(self,items = []):

		update_sql = "update SiteGrabHistory set grabStatus = '%s' ,innerPageCount = %d,outPageCount=%d,lastUpdateTime='%s'" %(items['grabStatus'],items['innerPageCount'],items['outPageCount'],items['lastUpdateTime'])
		cursor = self.get_cursor()
		cursor.execute(update_sql)
		cursor.commit()


import mysqlConnector

class SiteRelation(object):
	"""docstring for SiteRelation"""
	def __init__(self,mysqlConn):
		self.mysqlConn = mysqlConn
		

	def get_cursor(self):
		return mysqlConn.cursor()

	def insert_one(self,items = []):
		insert_sql = "insert into SiteRelation(masterSite,outLinkSite,outLinkCount,createTime,lastUpdateTime) values(%s,%s,%d,%s,%s)"
		insert_item  = []
		insert_item.append(items['masterSite'])
		insert_item.append(items['outLinkSite'])
		insert_item.append(items['outLinkCount'])
		insert_item.append(items['createTime'])
		insert_item.append(items['lastUpdateTime'])
		cursor = self.get_cursor()
		cursor.execute(insert_sql,insert_item)
		cursor.commit()


	def has_site_relation(self,items = {}):
		query_sql = "select * from SiteRelation where masterSite = '%s' and outLinkSite = '%s'"
		cursor = self.get_cursor()
		cursor.execute(query_sql)
		results = cursor.fetchAll()
		return len(results) > 0

	def function(self,items = {}):
		query_sql = "select * from SiteRelation where masterSite = '%s' and outLinkSite = '%s'"
		cursor = self.get_cursor()
		cursor.execute(query_sql)
		results = cursor.fetchAll()
		if len(results) > 0:
			result = results[0]
			count = result['outLinkCount'] +1
			update_sql = "update SiteRelation set outLinkCount = %d where masterSite = '%s' and outLinkSite = '%s'"
			cursor.execute(update_sql)
			cursor.commit()

	def query(self,items = []):
		pass

	def update(self,items = []):
		pass

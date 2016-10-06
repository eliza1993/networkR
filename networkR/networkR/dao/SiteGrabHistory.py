import datetime
from mysqlConnector import mysqlConnector

class SiteGrabHistory(object):
	"""docstring for SiteGrabHistory"""
	def __init__(self,mysqlConn):
		self.mysqlConn = mysqlConn

	def get_cursor(self):
		return self.mysqlConn.cursor()
	def insert_one(self,items = []):
		insert_sql = "insert into SiteGrabHistory(siteDomain,url,grabStatus,innerPageCount,outPageCount,createTime,lastUpdateTime) "+"values(%s,%s,%s,%s,%s,%s,%s)"

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
		self.mysqlConn.commit()
		


	def query_by_domain_and_status(self,items = []):
		query_sql = "select * from SiteGrabHistory where siteDomain = '%s' and grabStatus = '%s' order by id asc limit 100" % (items['siteDomain'],items['grabStatus'])
		cursor = self.get_cursor()
		cursor.execute(query_sql)
		results = cursor.fetchall()
		return results


	def update(self,items = []):

		update_sql = "update SiteGrabHistory set grabStatus = '%s' ,innerPageCount = %s,outPageCount=%s,lastUpdateTime='%s' where url = '%s' " %(items['grabStatus'],items['innerPageCount'],items['outPageCount'],items['lastUpdateTime'],items['url'])
		cursor = self.get_cursor()
		cursor.execute(update_sql)
		self.mysqlConn.commit()



def test_insert_one(siteGbHis):


	items = {}
	items['siteDomain'] = 'www.baidu.com'
	items['url'] = 'http://www.baidu.com'
	items['grabStatus'] = 'NEW'
	items['innerPageCount'] = 0
	items['outPageCount'] = 0
	items['createTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
	items['lastUpdateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

	siteGbHis.insert_one(items)
	

def test_query_by_domain_and_status(siteGbHis):
	items = {}
	items['siteDomain'] = 'www.baidu.com'
	items['grabStatus'] = 'NEW'

	print siteGbHis.query_by_domain_and_status(items)


def test_update(siteGbHis):
	items = {}
	items['siteDomain'] = 'www.baidu.com'
	items['url'] = 'http://www.baidu.com'
	items['grabStatus'] = 'FINSIH'
	items['innerPageCount'] = 1000
	items['outPageCount'] = 1000
	items['lastUpdateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

	siteGbHis.update(items)
	


if __name__ == '__main__':
	link = mysqlConnector()
	connect = link.openDb('172.16.111.87','root','','Spider')
	siteGbHis = SiteGrabHistory(connect)

	#test_insert_one(siteGbHis)
	test_query_by_domain_and_status(siteGbHis)
	test_update(siteGbHis)





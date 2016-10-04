import MySQLdb

from . import mysqlConnector
class GrabSite(object):
	"""docstring for GrabSite"""

	insert_sql = "insert into "+
	"GrabSite(id,siteDomain,siteName,webPageCount,totalOutLinkCuont,siteStatus,siteType,createTime,startGrabTime,endGrabTime) "+
	"values();"
	def __init__(self,mysqlConn):
		self.mysqlConn = mysqlConn
		self.cursor = mysqlConn.cursor()



	def insert(self,items = []):
		pass


	def query(self,items = []):
		pass

	def update(self,items = []):
		pass




from . import mysqlConnector

class SiteRelation(object):
	"""docstring for SiteRelation"""
	def __init__(self,mysqlConn):
		self.mysqlConn = mysqlConn
		self.cursor = mysqlConn.cursor()
		


	def insert(self,items = []):
		pass


	def query(self,items = []):
		pass

	def update(self,items = []):
		pass

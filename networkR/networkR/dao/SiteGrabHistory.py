from . import mysqlConnector

class SiteGrabHistory(object):
	"""docstring for SiteGrabHistory"""
	def __init__(self,mysqlConn):
		self.mysqlConn = mysqlConn
		self.cursor = mysqlConn.cursor()
		


	def insert(self,items = []):
		pass


	def query(self,items = []):
		pass

	def update(self,items = []):
		pass

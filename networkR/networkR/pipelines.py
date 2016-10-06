# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import datetime

from dao.SiteGrabHistory import SiteGrabHistory
from dao.SiteRelation import SiteRelation
from dao.SiteGrab import SiteGrab

class NetworkrPipeline(object):
	"""
		item:url\innerPageArr\outPageArr
	"""

	siteReDic = {}
	siteRelation = None
	siteGrabHis = None
	siteGb = None


	def __init__(self):
		self.init_site_relation()
		self.init_site_grab_his()


	def init_site_relation(self):
		mysqlConn = mysqlConnector()
        dbConn = mysqlConn.openDb('172.16.111.87','root','','Spider')
        siteGrabHis = SiteGrabHistory(dbConn)

	def init_site_grab_his(self):
		mysqlConn = mysqlConnector()
        dbConn = mysqlConn.openDb('172.16.111.87','root','','Spider')
        siteRelation = SiteRelation(dbConn)

	def init_site_grab(self):
		mysqlConn = mysqlConnector()
        dbConn = mysqlConn.openDb('172.16.111.87','root','','Spider')
        siteGb = SiteGrab(dbConn)

	def process_item(self, item, spider):
		"""
		验证 插入 更新
		"""

		if item is None:
			print 'None'
			return

		if len(item) == 0:
			print 'size is zero'
			return

		innerPageArray = item['innerPageArray']
		outPageArray = item['outPageArray']
		insertItems = {}
		
		
		for index in range(0,len(innerPageArray)):
			insertItems["grabStatus"] = 'NEW'
			insertItems["url"] = innerPageArray[i]
			insertItems["domain"] = self.get_domain(innerPageArray[i])
			insertItems['innerPageCount'] = 0
			insertItems['outPageCount'] = 0;
			insertItems['lastUpdateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			siteGrabHis.insert_one(insertItems);



		for index in range(0,len(outPageArray)):
			insertItems["grabStatus"] = 'NEW'
			insertItems["url"] = outPageArray[i]
			insertItems["domain"] = self.get_domain(outPageArray[i])
			insertItems['innerPageCount'] = 0
			insertItems['outPageCount'] = 0;
			insertItems['lastUpdateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			siteGrabHis.insert_one(insertItems);
			#建立 site relation 关系
			self.handle_site_relation(item['domain'],insertItems["domain"])



			insertItems["grabStatus"] = 'FINISH'
			insertItems["url"] = item['url']
			insertItems["domain"] = item['domain']
			insertItems['innerPageCount'] = len(innerPageArray)
			insertItems['outPageCount'] = len(outPageArray)
			insertItems['lastUpdateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
			siteGrabHis.update(insertItems);


			siteGb.update_count(insertItems)


	def get_domain(self,url):
		if 'http://' in url:
			url = url[7:]

		if 'https://' in url:
			url = url[8:]

		if '/' in url:
			index = url.index('/')
			url = url[0:index]

		return url



        


	def close_spider(self, spider):
		siteGrabHis.close


	def handle_site_relation(self,masterSite,outLinkSite):
		if self.has_site_relation(masterSite,outLinkSite):
			self.increase(masterSite,outLinkSite)
			return

		items['masterSite'] = masterSite;
		items['outLinkSite'] = outLinkSite
		items['outLinkCount'] = 0
		items['createTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
		items['lastUpdateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

		self.siteRelation.insert_one(items)


	def has_site_relation(self,masterSite,outLinkSite):
		key = masterSite + "_" + outLinkSite
		if siteReDic.has_key(key):
			return True

		items['masterSite'] = masterSite;
		items['outLinkSite'] = outLinkSite;
		return siteRelation.has_site_relation(items)

	def increase(self,masterSite,outLinkSite):
		items['masterSite'] = masterSite;
		items['outLinkSite'] = outLinkSite;

		siteRelation.increase_one(items)





if __name__ == '__main__':
	url = 'https://www.baidu.com'
	url2 = 'http://www.baidu.com'

	siteGrabHis = SiteGrabHistory(None)
	pipeline = NetworkrPipeline(siteGrabHis)
	print pipeline.get_domain(url)
	print pipeline.get_domain(url2)

	items = {}
	pipeline.process_item(items)

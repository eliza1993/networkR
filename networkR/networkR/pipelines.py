# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from dao.SiteGrabHistory import SiteGrabHistory

class NetworkrPipeline(object):
	"""
		item:url\innerPageArr\outPageArr
	"""

	def __init__(self,siteGrabHis):
		self.siteGrabHis = siteGrabHis


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
			siteGrabHis.insert(insertItems);


		for index in range(0,len(outPageArray)):
			insertItems["grabStatus"] = 'NEW'
			insertItems["url"] = outPageArray[i]
			insertItems["domain"] = self.get_domain(outPageArray[i])
			insertItems['innerPageCount'] = 0
			insertItems['outPageCount'] = 0;
			siteGrabHis.insert(insertItems);



			insertItems["grabStatus"] = 'FINISH'
			insertItems["url"] = item['url']
			insertItems["domain"] = item['domain']
			insertItems['innerPageCount'] = len(innerPageArray)
			insertItems['outPageCount'] = len(outPageArray)
			insertItems['lastUpdateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
			siteGrabHis.update(insertItems);



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




if __name__ == '__main__':
	url = 'https://www.baidu.com'
	url2 = 'http://www.baidu.com'

	siteGrabHis = SiteGrabHistory(None)
	pipeline = NetworkrPipeline(siteGrabHis)
	print pipeline.get_domain(url)
	print pipeline.get_domain(url2)

	items = {}
	pipeline.process_item(items)

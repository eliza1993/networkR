#!/usr/bin/python
# -*- coding: utf-8 -*-

from networkR.pipelines import NetworkrPipeline
from networkR.dao.SiteGrabHistory import SiteGrabHistory
from networkR.dao.mysqlConnector import mysqlConnector



def process_item_test():
	mysqlConn = mysqlConnector()
	dbConn = mysqlConn.openDb('172.16.111.87','root','','Spider')
	siteGbHis = SiteGrabHistory(dbConn)
	pipeline = NetworkrPipeline(siteGbHis)
	items = {}
	pipeline.process_item(items,None)

	mysqlConn.close(dbConn)

def get_domain_test():
	url = 'https://www.baidu.com'
	url2 = 'http://www.baidu.com'
	pipeline = NetworkrPipeline(None)
	print pipeline.get_domain(url)
	print pipeline.get_domain(url2)
	

if __name__ == '__main__':
	get_domain_test()

	process_item_test()




	







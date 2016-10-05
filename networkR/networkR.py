#!/usr/bin/python
# -*- coding: utf-8 -*-

from networkR.pipelines import NetworkrPipeline
from networkR.dao.SiteGrabHistory import SiteGrabHistory
from networkR.dao.mysqlConnector import mysqlConnector


if __name__ == '__main__':
	url = 'https://www.baidu.com'
	url2 = 'http://www.baidu.com'

	mysqlConn = mysqlConnector()
	dbConn = mysqlConn.openDb("172.16.111.87",3306,"root","","Spider")
	siteGbHis = SiteGrabHistory(dbConn)
	pipeline = NetworkrPipeline(siteGbHis)
	print pipeline.get_domain(url)
	print pipeline.get_domain(url2)

	items = {}
	pipeline.process_item(items,None)





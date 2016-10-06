import scrapy

from networkR.items import NetworkrItem
from networkR.dao.GrabSite import GrabSite
from networkR.dao.mysqlConnector import mysqlConnector
from networkR.dao.SiteGrabHistory import SiteGrabHistory

import networkR.util.UrlUtil

class NetworRSpider(scrapy.Spider):
    name = "networkr"
    allowed_domains = ["taozhanggui.com"]
    start_urls = [
        "www.taozhanggui.com"
    ]

    gbSite = None
    gbSiteHis = None


    def __init__(self):
        self.init_gb_site()
        self.init_site_grab_history()


    def start_requests():
        if start_urls and len(start_urls) > 0:
            self.handle_start_url()

        urls = self.plan_next_excute_urls()
        for url in self.start_urls:
            yield self.make_requests_from_url(url)


            

    def parse(self, response):
        if response is None:
            return

        url = handle_url(response.url)

        item = self.parse_item(url,response)


    def parse_item(self,url,response):
        item = NetworkrItem()
        item['domain'] = get_domain(url)
        item['url'] = handle_url(url)
        innerPageArray,outPageArray = self.parse_page_links(item['domain'],response)
        item['innerPageArray'] = innerPageArray
        item['outPageArray'] outPageArray

        return item



    def parse_page_links(self,domain,response):
        innerPageArray,outPageArray = [],[]

        totalLinks = []
        for aItem in response.xpath('//a'):
            link = aItem.xpath('@href').extract()
            totalLinks.append(link)
        
        for link in totalLinks:
            if domain in link:
                innerPageArray.append(handle_url(link))
            else:
                outPageArray.append(handle_url(link))

        return (innerPageArray,outPageArray)


    def handle_start_url(self):
        items = {}
        items['siteDomain'] = ''
        for url in start_urls:
            items['siteDomain'] = url;
            result = gbSite.query_grab_site_by_domain(items)
            if result is None:
                items['siteDomain'] = url
                items['siteName'] = url
                items['webPageCount'] = 0
                items['totalOutLinkCuont'] = 0
                items['siteStatus'] = 'WAIT' 
                items['siteType'] = 'seed'
                items['createTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                items['startGrabTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                items['endGrabTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                gbSite.insert_one(items)


    def init_gb_site(self):
        mysqlConn = mysqlConnector()
        dbConn = mysqlConn.openDb('172.16.111.87','root','','Spider')
        gbSite = GrabSite(dbConn)

    def init_site_grab_history(self):
        mysqlConn = mysqlConnector()
        dbConn = mysqlConn.openDb('172.16.111.87','root','','Spider')
        gbSiteHis = SiteGrabHistory(dbConn)


    def plan_next_excute_urls(self):
        items = {}
        items['siteStatus'] = 'WORKING'
        result = gbSite.query_grab_site_by_status(items)
        if result not None:
            hItems = {}
            hItems['siteDomain'] = result['siteDomain']
            hItems['grabStatus'] = result['NEW']
            result =  gbSiteHis.query_by_domain_and_status(hItems)
            if result not None and len(result) > 0:
                urls = []
                for res in result:
                    urls.append(res['url'])

                return urls

        
        items['siteStatus'] = 'WAIT'
        result = gbSite.query_grab_site_by_status(items)
        if result not None:
            urls = []
            urls.append(res['siteDomain'])

            return urls;


        return []

        







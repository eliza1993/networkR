import scrapy

from networkR.items import NetworkrItem
from networkR.dao.GrabSite import GrabSite
from networkR.dao.mysqlConnector import mysqlConnector
from networkR.dao.SiteGrabHistory import SiteGrabHistory

from networkR.util.UrlUtil import *

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


    def start_requests(self):
        if self.start_urls and len(self.start_urls) > 0:
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
        item['outPageArray'] = outPageArray

        return item



    def parse_page_links(self,domain,response):
        innerPageArray,outPageArray = [],[]

        totalLinks = []
        for aItem in response.xpath('//a'):
            link = aItem.xpath('@href').extract()
            if len(link) > 0:
                url = self.link_filter(domain,link[0])
                if not(url is None):
                    totalLinks.append(url)        
            
        
        for link in totalLinks:
            if domain in link:
                innerPageArray.append(handle_url(link))
            else:
                outPageArray.append(handle_url(link))

        return (innerPageArray,outPageArray)


    def link_filter(self,domain,link):
        if link is None:
            return link

        if 'javascript' in link:
            return None

        if 'http' in link:
            return link

        if 'www' in link:
            return link

        if '.com' in link:
            return link

        if '.cn' in link:
            return link
        if domain not in link:
            link = domain + '/' + link

        return link;


    def handle_start_url(self):
        items = {}
        items['siteDomain'] = ''
        for url in self.start_urls:
            items['siteDomain'] = url;
            result = self.gbSite.query_grab_site_by_domain(items)
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
                self.gbSite.insert_one(items)


    def init_gb_site(self):
        mysqlConn = mysqlConnector()
        dbConn = mysqlConn.openDb('192.168.31.160','root','','Spider')
        self.gbSite = GrabSite(dbConn)

    def init_site_grab_history(self):
        mysqlConn = mysqlConnector()
        dbConn = mysqlConn.openDb('192.168.31.160','root','','Spider')
        self.gbSiteHis = SiteGrabHistory(dbConn)


    def plan_next_excute_urls(self):
        items = {}
        items['siteStatus'] = 'WORKING'
        result = self.gbSite.query_grab_site_by_status(items)
        if not(result is None):
            hItems = {}
            hItems['siteDomain'] = result['siteDomain']
            hItems['grabStatus'] = result['NEW']
            result =  self.gbSiteHis.query_by_domain_and_status(hItems)
            if not(result is None) and len(result) > 0:
                urls = []
                for res in result:
                    urls.append(res['url'])

                return urls

            hItems['siteDomain'] = result['siteDomain']
            hItems['grabStatus'] = result['FINISH']
            self.gbSite.update(hItems)

        
        items['siteStatus'] = 'NEW'
        result = self.gbSite.query_grab_site_by_status(items)
        if not(result is None):
            urls = []
            urls.append(res['siteDomain'])

            return urls;


        return []

        







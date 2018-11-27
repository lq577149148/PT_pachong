# -*- coding: utf-8 -*-
import scrapy,re


class DangdangwSpider(scrapy.Spider):
    name = 'dangdangw'
    # allowed_domains = ['http://book.dangdang.com/']
    # start_urls = ['http://http://book.dangdang.com//']

    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }

    def start_requests(self):
        url = 'http://book.dangdang.com/'

        yield scrapy.Request(url=url,callback=self.parse)


    def parse(self, response):
        link = response.xpath("//ul[@id='component_403754__5298_5295__5295']/li/p[@class='name']/a/@href").extract()
        links = re.findall("component_map_id='(.*?)'",response.text)
        print(links,'==============')
        for x in links:
            urls = 'http://book.dangdang.com/Standard/Framework/Core/hosts/ajax_api.php?isajax=1&page_id=65152&component_map_id='+x
            yield scrapy.Request(url=urls,callback=self.parse1,headers=self.headers)
            print(x)
        for i in link:
            print(i)
            yield scrapy.Request(url=urls,callback=self.parse3,headers=self.headers)
    def parse1(self,response):
         link1 = response.xpath("//ul/li/p[@class='name']/a/@href").extract()
         print(link1)
         for x in link1:
             url1 = x
             yield scrapy.Request(url=url1,callback=self.parse2,headers=self.headers)

    def parse2(self,response):
        name = response.xpath("//div[@class='name_info']/h1/text()").extract()
        print(name)

    def parse3(self,response):
        name = response.xpath("//div[@class='name_info']/h1/text()").extract()
        print(name)
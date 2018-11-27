# -*- coding: utf-8 -*-
import scrapy


class SningwSpider(scrapy.Spider):
    name = 'sningw'
    # allowed_domains = ['https://search.suning.com/%E6%89%8B%E6%9C%BA/#second-filter']
    # start_urls = ['http://https://search.suning.com/%E6%89%8B%E6%9C%BA/#second-filter/']

    def start_requests(self):
        for i in range(4):
            for x in range(4):
                if i >= 1:
                    url = 'https://search.suning.com/emall/searchV1Product.do?keyword=%E6%89%8B%E6%9C%BA&pg=01&cc=010&adNumber=3&paging='+str(x)+'&cp='+str(i)
                    print(url)
                    yield scrapy.Request(url=url, callback=self.parse)
                else:
                    url = 'https://search.suning.com/emall/searchV1Product.do?keyword=%E6%89%8B%E6%9C%BA&pg=01&cc=010&paging='+str(x)+'&cp='+str(i)
                    print(url)
                    yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        print('==============================================')
        link = response.xpath("//div[@class='title-selling-point']/a/@href").extract()
        for i in link:
            urls = 'https:'+str(i)
            yield scrapy.Request(url=urls,callback=self.parse1)

    def parse1(self,response):
        name = response.xpath("//div[@class='proinfo-title']/h1/text()").extract()
        print(name)


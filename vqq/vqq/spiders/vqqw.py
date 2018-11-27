# -*- coding: utf-8 -*-
import scrapy,re
from ..items import VqqItem


class VqqwSpider(scrapy.Spider):
    name = 'vqqw'
    # allowed_domains = ['www.v.qq.com']
    # start_urls = ['http://www.v.qq.com/']

    def start_requests(self):
        url = 'https://v.qq.com/'
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        link = response.xpath("//a[@class='nav_link _link bold']/@href").extract()
        name = response.xpath("//a[@class='nav_link _link bold']/text()").extract()
        print(name)
        for i in link:
            urls = i
            yield scrapy.Request(url=urls,callback=self.parse1)
    def parse1(self ,response):
        links = response.xpath("//strong[@class='figure_title figure_title_two_row']/a/@href").extract()
        link1 = response.xpath("//strong[@class='figure_title']/a/@href").extract()
        for i in links:
            if len(i) <= 50:
                url1 = i
                yield scrapy.Request(url=url1,callback=self.parse2)
        for x in link1:
            if len(x) <= 50:
                url2 = x
                yield scrapy.Request(url=url2,callback=self.parse3)

    def parse2(self ,response):
        item = VqqItem()
        title = re.findall('<title>(.*?)</title>',response.text)
        item['title'] = title
        ping = response.xpath("//span[@class='video_score']/span/text()").extract()
        item['ping'] = ping
        name = response.xpath("//div[@class='mod_people_inner _starlist']/div/a/text()").extract()
        item['name'] = name
        for i in name:
            print(i)


        print(ping)
        print(title)
        yield item

    def parse3(self, response):
        item = VqqItem()
        title1 = re.findall('<title>(.*?)</title>', response.text)
        item['title1'] = title1
        ping1 = response.xpath("//span[@class='video_score']/span/text()").extract()
        item['ping1'] = ping1
        name1 = response.xpath("//div[@class='mod_people_inner _starlist']/div/a/text()").extract()
        item['name1'] = name1
        for i in name1:
            print(i)
        print(ping1)
        print(title1)
        yield item

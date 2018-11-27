# -*- coding: utf-8 -*-
import scrapy,re
import time
import random
import win_unicode_console
win_unicode_console.enable()

class YouxinwSpider(scrapy.Spider):
    name = 'youxinw'
    # allowed_domains = ['https://www.xin.com/beijing']
    # start_urls = ['http://https://www.xin.com/beijing/']

    def start_requests(self):
        url = "https://www.xin.com/beijing/dazhong/?q=%E5%A4%A7%E4%BC%97"
        yield scrapy.Request(url=url,callback=self.parse)


    def parse(self, response):
        # print(response.text)
        link = response.xpath("//a[@class='aimg']/div[@class='pad']/h2/span[@class='tit yx-l2']/@href").extract()
        for i in link:
            urls = "https:"+str(i)
            print(urls)
            time.sleep(random.randint(2,5))
            yield scrapy.Request(url=urls,callback=self.parse1)
    def parse1(self ,response):
        title = re.findall("<title>(.*?)</title>",response.text)
        print(title)


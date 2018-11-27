# -*- coding: utf-8 -*-
import scrapy,re
import win_unicode_console
win_unicode_console.enable()


class DouyutvSpider(scrapy.Spider):
    name = 'douyutv'
    # allowed_domains = ['www.douyu.com']
    # start_urls = ['http://www.douyu.com/']


    def start_requests(self):
        for i in range(1):
            url = 'https://www.douyu.com/gapi/rkc/directory/0_0/'+str(i)
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        link = re.findall('"rid":(.*?),',response.text)
        for i in link:
            urls = 'https://www.douyu.com/'+str(i)
            yield scrapy.Request(url=urls,callback=self.parse1)

    def parse1(self ,response):
        title = re.findall()
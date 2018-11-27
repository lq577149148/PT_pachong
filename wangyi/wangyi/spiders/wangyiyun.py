# -*- coding: utf-8 -*-
import scrapy,re
import win_unicode_console
win_unicode_console.enable()


class WangyiyunSpider(scrapy.Spider):
    name = 'wangyiyun'
    # allowed_domains = ['https://music.163.com/']
    # start_urls = ['http://https://music.163.com//']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://music.163.com/discover/toplist'
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        name = re.findall('<li><a href="(.*?)"',response.text)
        for i in name:
            urls = 'https://music.163.com'+i
            print(urls)
            yield scrapy.Request(url=urls,callback=self.parse1)
    def parse1(self,response):
        name = re.findall('content="(.*?)"',response.text)

        for z in name:
            print(z)
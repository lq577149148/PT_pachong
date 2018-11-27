# -*- coding: utf-8 -*-
import scrapy,time,re
import win_unicode_console
win_unicode_console.enable()


class GuomeiwSpider(scrapy.Spider):
    name = 'guomeiw'
    # allowed_domains = ['https://search.gome.com.cn/search?question=%E7%94%B5%E8%84%91']
    # start_urls = ['http://https://search.gome.com.cn/search?question=%E7%94%B5%E8%84%91/']
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',

    }

    def start_requests(self):
        url = 'https://search.gome.com.cn/search?question=%E7%94%B5%E8%84%91&searchType=goods&search_mode=normal'
        yield scrapy.Request(url=url,callback=self.parse,headers=self.headers)

    def parse(self, response):
        # print(response.text)
        link = re.findall('href="(.*?)"',response.text)
        a = str(link)
        print(a,'=======================')

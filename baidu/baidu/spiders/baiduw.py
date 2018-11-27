# -*- coding: utf-8 -*-
import scrapy,re
from newspaper import Article
import win_unicode_console
win_unicode_console.enable()


class BaiduwSpider(scrapy.Spider):
    name = 'baiduw'
    # allowed_domains = ['www.baidu.com']
    # start_urls = ['http://www.baidu.com/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'

    }

    def start_requests(self):
        a = input("请输入想要的资讯：：：")
        # for i in range(1,100):
        #     if i%10 == 0:
        #         print(i)
        url = 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word='+str(a)
        yield scrapy.Request(url=url,callback=self.parse,headers=self.headers)

    def parse(self, response):
        print('================')
        link = response.xpath("//div/div/h3/a/@href").extract()
        print(link)
        for i in link:
            urls = i
            print(i)
            yield scrapy.Request(url=urls,callback=self.parse1,headers=self.headers)

    def parse1(self, response):

        title = re.findall('<title>(.*?)</title>',response.text)
        news = Article(url=response.url, language='zh')
        news.download()
        news.parse()
        neirong = news.text
        print(neirong)
        print(title)


# -*- coding: utf-8 -*-
import scrapy,re
from ..items import WecahtItem
from newspaper import Article
import win_unicode_console
win_unicode_console.enable()

# import newspaper.article
class WechatSpider(scrapy.Spider):
    name = 'wechat'
    # allowed_domains = ['www.baidu.com']
    # start_urls = ['http://www.baidu.com/']

    def start_requests(self):
        a = input("请输入要搜索的公众号：：：")
        url = 'https://weixin.sogou.com/weixin?type=1&s_from=input&query='+str(a)
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        link = response.xpath("//div[@class='txt-box']/p[@class='tit']/a/@href").extract()
        for i in link:
            urls = i
            yield scrapy.Request(url=urls,callback=self.parse1,)

    def parse1(self,response):
        links = re.findall('"content_url":"(.*?)"',response.text)
        for z in links:
            a = z.replace('&amp;','&')
            urls = "https://mp.weixin.qq.com"+str(a)
            yield scrapy.Request(url=urls,callback=self.parse2)
    def parse2(self,response):
        item = WecahtItem()
        name = response.xpath("//div[@id='img-content']/h2[@id='activity-name']/text()").extract()
        neirong = Article(url=response.url,language='zh')
        neirong.download()
        neirong.parse()
        texts = neirong.text
        item['name'] = ''.join(name)
        item['texts'] = ''.join(texts)
        yield item

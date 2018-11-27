# -*- coding: utf-8 -*-
import scrapy
import win_unicode_console
win_unicode_console.enable()
import re


class SuSpider(scrapy.Spider):
    name = 'su'
    # allowed_domains = ['su.com']
    # start_urls = ['http://su.com/']

    def start_requests(self):
        for i in range(0,4):#循环接口网址（0,4）
            url='https://search.suning.com/emall/searchV1Product.do?keyword=%E5%8F%8C%E8%82%A9%E5%8C%85&ci=0&pg&=01&cp=0&il=0&st=0&iy=0&n=1sesab=ACAABAAB&id=IDENTIFYING&cc=010&paging='+str(i)+'&sub=1&jzq=196937'
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):

        xqys=response.xpath("//li/div/div/div[2]/div[2]/a/@href").extract()#详情页接口
        for xqy in xqys:
            url='https:'+xqy#拼接详情页接口
            yield scrapy.Request(url,callback=self.parse1)
    def parse1(self,response):
        pls=re.findall(r'href="//review.suning.com/cmmdty_review/general-(.*?)-1-total.htm',response.text)
        for pl in pls:
            url='https://review.suning.com/ajax/cluster_review_lists/style--'+str(pl)+'-total-1-default-10-----reviewList.htm?callback=reviewList'
            yield scrapy.Request(url=url,callback=self.parse2)
    def parse2(self,response):
        pl_con=re.findall(r'"content":"(.*?)",',response.text)
        print(pl_con)
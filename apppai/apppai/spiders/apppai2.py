# -*- coding: utf-8 -*-
import scrapy,re,json
import win_unicode_console
from ..items import ApppaiItem
win_unicode_console.enable()


class Apppai2Spider(scrapy.Spider):
    name = 'apppai2'
    # allowed_domains = ['http://mi.talkingdata.com/rank']
    # start_urls = ['http://http://mi.talkingdata.com/rank/']

    def start_requests(self):
        for i in range(3300):
            if i%30 == 0:
                url = 'http://mi.talkingdata.com/rank/active.json?date=2018-10-01&dateType=m&rankingStart='+str(i)+'&rankingSize=30'
                yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        name = re.findall('"appName":"(.*?)"',response.text)
        paiming = re.findall('"ranking":(.*?),',response.text)
        gongsi = re.findall('"company":"(.*?)"',response.text)
        appid = re.findall('"appId":(.*?),',response.text)
        a = dict(zip(paiming,name))
        # print(a)
        # print(response.text)

        for i in appid:
            urls = 'http://mi.talkingdata.com/app/profile/'+str(i)+'.json?startTime=2018-09-01'

        yield scrapy.Request(url=urls,callback=self.parse1,meta={'a':a})




    def parse1(self, response):

        item = ApppaiItem()

        # print(response.text)
        a = re.findall('"name":"(.*?)"',response.text)[1:8]
        b = re.findall('"share":"(.*?)"',response.text)[1:8]
        c = response.meta['a']
        item['a'] = c
        print(c,'=======================================')
        item['b'] = dict(zip(a, b))

        yield item



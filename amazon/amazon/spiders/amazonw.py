# -*- coding: utf-8 -*-
import scrapy,re
import requests
import json
import time
import redis
import win_unicode_console
win_unicode_console.enable()
import bs4



class AmazonwSpider(scrapy.Spider):
    name = 'amazonw'
    # allowed_domains = ['https://www.amazon.cn/']
    # start_urls = ['http://https://www.amazon.cn//']

    def start_requests(self):

        url = 'https://www.amazon.cn/s/ref=nb_sb_noss_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Daps&field-keywords=%E6%89%8B%E8%A1%A8'
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        print("========================================")
        link = re.findall('<a class="a-link-normal a-text-normal" target="_blank" href="(.*?)">',response.text)
        for i in link:
            str(i)
            print(i)
            urls = i
            yield scrapy.Request(url=urls,callback=self.parse1)

    def parse1(self,response):
        name = re.findall('<title>(.*?)</title>',response.text)
        xinxi = re.findall('<td class="a-span7 a-size-base">(.*?)</td>',response.text)
        links = re.findall('<a id="acrCustomerReviewLink" class="a-link-normal" href="(.*?)ref',response.text)
        price = re.findall('<span class="a-color-price">(.*?)</span>',response.text)
        print(xinxi,'====================')
        print(price)
        print(name)
        for z in links:
            print(z,'***********************************')
            # for x in range(3):
            #     urlss = 'https://www.amazon.cn'+z
            #     yield

    # def get_ip(self):
    #     coon = redis.from_url(REDIS_URL)
    #     url = "生成的API链接"
    #     body = requests.get(url)
    #     data = json.loads(body.text)
    #     code = data["code"]
    #     if code == "0":
    #         msgs = data["msg"]
    #         for msg in msgs:
    #             ip = msg["ip"]
    #             port = msg["port"]
    #             IP = ip + ":" + port
    #             coon.lpush("proxies", IP)
    #     elif code == "3001":
    #         time.sleep(5)
    #         self.get_ip()


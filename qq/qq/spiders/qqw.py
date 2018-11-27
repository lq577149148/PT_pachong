# -*- coding: utf-8 -*-
import scrapy,re


class QqwSpider(scrapy.Spider):
    name = 'qqw'
    # allowed_domains = ['https://y.qq.com/portal/search.html#page=1']
    # start_urls = ['http://https://y.qq.com/portal/search.html#page=1/']

    def start_requests(self):
        a = input("输入歌手:")
        url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?aggr=1&cr=1&n=20&w='+str(a)
        print(url)
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        # print(response.text)
        mid_id = re.findall('"media_mid":"(.*?)"',response.text)
        print(mid_id,'===================================')
        for i in mid_id:
            urls = 'https://y.qq.com/n/yqq/song/'+str(i)+'.html'
            print(urls)
            yield scrapy.Request(url=urls,callback=self.parse1)

    def parse1(self,response):
        pass


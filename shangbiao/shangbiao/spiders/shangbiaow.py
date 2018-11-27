# -*- coding: utf-8 -*-
import scrapy


class ShangbiaowSpider(scrapy.Spider):
    name = 'shangbiaow'
    # allowed_domains = ['http://wsjs.saic.gov.cn/']
    # start_urls = ['http://http://wsjs.saic.gov.cn//']


    def start_requests(self):
        url = 'http://wsjs.saic.gov.cn/txnRead01.do?y7bRbP=KaD.kqkN_8vN_8vN_pSi_k2C7QsyXjHE9.PYeMKFfjuN'


    def parse(self, response):
        pass

# -*- coding: utf-8 -*-
import scrapy,re


class LvmamawSpider(scrapy.Spider):
    name = 'lvmamaw'
    # allowed_domains = ['http://flight.lvmama.com/booking/']
    # start_urls = ['http://http://flight.lvmama.com/booking//']


    def start_requests(self):
        url = 'http://flight.lvmama.com/tosearch/getCities'
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        city = re.findall('"(.*?)"',response.text)
        print(len(city))
        city1 = ['SHA','PEK','CAN']
        for x in city1:
            for i in city:
                a = i[-3:]
                urls = 'http://flight.lvmama.com/booking/'+str(x)+'-'+str(a)+'.html?date1=2018-11-20&date2=2018-11-22'
                print(urls)
                yield scrapy.Request(url=urls,callback=self.parse1)

    def parse1(self, response):
        hangban = response.xpath("//div[@class='tl-detail clearfix']/div[@class='tl-col tl-info']/div[@class='tl-bottom']/span/text()").extract()
        print(hangban)


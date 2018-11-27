# -*- coding: utf-8 -*-
import scrapy,re,time


class MeitaunwSpider(scrapy.Spider):
    name = 'meitaunw'
    # allowed_domains = ['https://bj.meituan.com/s/%E5%B1%B1%E4%B8%9C/']
    # start_urls = ['http://https://bj.meituan.com/s/%E5%B1%B1%E4%B8%9C//']
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
    # }

    cookies = {' __mta': '149133961.1541994065419.1542011577105.1542011584107.18', ' lsu': '', ' u': '384314673', ' lng': '116.478787', ' _lxsdk_cuid': '16705cea3cdc8-0b83f79401c62c-514d2f1f-144000-16705cea3cfc8', ' _lxsdk_s': '16706ca50f0-cba-71a-a1a%7C%7C292', ' lt': 'WSoQUK1U3PD1mbJlpcj_sa-WYxMAAAAAbAcAAK_B3utG_IegE0dxIuIM288hiTH-WR0rt8-TEbUiNoF-LFHvefu2wzlKAZl-8EG7-A', ' _lxsdk': '16705cea3cdc8-0b83f79401c62c-514d2f1f-144000-16705cea3cfc8', ' n': 'OfS427304446', ' mtcdn': 'K', ' token2': 'WSoQUK1U3PD1mbJlpcj_sa-WYxMAAAAAbAcAAK_B3utG_IegE0dxIuIM288hiTH-WR0rt8-TEbUiNoF-LFHvefu2wzlKAZl-8EG7-A', ' _lx_utm': 'utm_source%3DBaidu%26utm_medium%3Dorganic', '__mta': '149133961.1541994065419.1542007498864.1542010848889.6', ' unc': 'OfS427304446', ' ci': '1', ' lat': '39.932222', ' uuid': 'e39f85f66b7c45c3a1e1.1542007182.2.0.0', ' userTicket': 'EYmUJlGWjntzfZnOOXcWbHprkZkAaeFYPzMbkAoV', ' rvct': '1'}

    def start_requests(self):
        a = input("请输入搜索的地区:")
        url = 'https://apimobile.meituan.com/group/v4/poi/pcsearch/1?uuid=e39f85f66b7c45c3a1e1.1542007182.1.0.0&userid=-1&limit=32&offset=32&cateId=-1&q='+str(a)
        yield scrapy.Request(url=url,callback=self.parse,cookies=self.cookies)

    def parse(self, response):
        # print(response.text)
        name = re.findall('"id":(.*?),',response.text)
        # print(name)
        for i in name:
            urls = 'http://www.meituan.com/meishi/'+str(i)
            print(urls)

            yield scrapy.Request(url=urls,callback=self.parse1,cookies=self.cookies)

    def parse1(self ,response):
        title = response.xpath("//div[@class='seller-info-head']/h1[@class='seller-name']/text()").extract()
        print(title)

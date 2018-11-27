# -*- coding: utf-8 -*-
import scrapy,re,json
import win_unicode_console
win_unicode_console.enable()


class YhdwSpider(scrapy.Spider):
    name = 'yhdw'
    # allowed_domains = ['http://www.yhd.com/']
    # start_urls = ['http://http://www.yhd.com//']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    headers1 = {
        'Referer': 'http://item.yhd.com/4614166.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
        'callback': 'commentDetailCallback'
    }
    cookies = {' cid': 'NWhTMjEwNnVCODcyN2xYNjU4OGlBMzMwMXpBMDkwMmNNMjMyM2JLODM2NGpEMTUy', ' shshshfpb': '1c2007b83a6844e17b4e5b46784528ec4a25e1eda9ee6b7085be8d1052', ' __jda': '81617359.1541982339768200858114.1541982340.1541982340.1541982340.1', ' __jdv': '259140492|baidu|-|organic|not set|1541982339768', ' __jdb': '81617359.52.1541982339768200858114|1.1541982340', ' cart_cookie_uuid': '2e06d656-34e3-4434-899c-3ff8d5e42749', ' yihaodian_uid': '278727083', ' msessionid': 'YFJXG2X496KR8WFHUM14K1BHX2M838VM4MB6', ' uname': '18501190439%40phone', ' shshshfp': '614b651e9445d365be70d45ff3c05223', ' yhd_location': '2_2817_51973_0', ' shshshfpa': '164b2ede-385b-eac3-e664-31b40c89e710-1541984515', ' __jdc': '81617359', ' JSESSIONID': '9DAAA801B50B649DFF3E3C2BBB580E7F.s1', ' shshshsID': '9db17f9103e57bb115e9440a30a56408_2_1541987727553', 'Cookie: provinceId': '2', ' cart_num': '0', ' cityId': '2817'}


    def start_requests(self):
        url = 'http://search.yhd.com/c0-0/k%25E5%2592%2596%25E5%2595%25A1/'
        yield scrapy.Request(url=url,callback=self.parse,headers=self.headers)

    def parse(self, response):
        # print('=========================')
        link = response.xpath("//div/p[@class='proName clearfix']/a/@href").extract()
        # price = response.xparh("//p[@class='proPrice']/em[@id='price0_1233204']/text()").extract()
        # print(price)
        for i in link:
            urls = "http:"+str(i)
            print(urls)
            yield scrapy.Request(url=urls,callback=self.parse1,headers=self.headers)

    def parse1(self ,response):
        title = re.findall('<title>(.*?)</title>',response.text)
        id = re.findall('<span>商品编号</span>(.*?)</p>',response.text)
        print(id)
        print(title)
        for x in id:
            urlss = 'http://item.yhd.com/squ/comment/getCommentDetail.do?productId='+str(x)+'&callback=commentDetailCallback'
            print(urlss)
            yield scrapy.Request(url=urlss,callback=self.parse2,headers=self.headers1,cookies=self.cookies)

    def parse2(self ,response):
        # a = {}
        a = response.text
        # print(a)
        # c = a['value']
        # print(c)
        print('============================================================')
        # a = re.findall('{(.*?)}',response.text)
        # v = json.loads(response.text)['value']
        # htmls = html['value']
        # print(a)
        c = a[34:-3]
        print(c)
        # v = str(c)
        # print(a)
        # neirong = c.xpath("//dl/dd[@class='clearfix']/span[@class='text comment_content_text']/text()")
        # print(neirong)



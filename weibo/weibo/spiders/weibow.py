# -*- coding: utf-8 -*-
import scrapy,re
import json
from ..items import WeiboItem
from lxml import etree

import win_unicode_console
win_unicode_console.enable()

class WeibowSpider(scrapy.Spider):
    name = 'weibow'
    # allowed_domains = ['https://s.weibo.com/weibo/%25E6%2597%25A0%25E5%258F%258C?topnav=1']
    # start_urls = ['http://https://s.weibo.com/weibo/%25E6%2597%25A0%25E5%258F%258C?topnav=1/']
    cookies = {' WBStorage': 'e8781eb7dee3fd7f|undefined', ' SUHB': '0KABcTzTpRlfJx', ' wvr': '6', ' cross_origin_proto': 'SSL', ' _s_tentry': 'passport.weibo.com', ' ULV': '1540944679081:8:2:1:8055912243399.308.1540944679070:1538871513883', ' SCF': 'AqP1aVKkZncIXoLZNrEXxRfGCwoyV490UXNr9mrorRn1LAOS7QgabPFJPFGsgxYNZHXA1qjOlIZW6WzNlgmoHpM.', ' login_sid_t': 'abe3081c5822684d99eea56c9adbb03c', 'SINAGLOBAL': '6172144502425.479.1532653095927', ' ALF': '1541554159', ' UOR': ',,www.baidu.com', ' SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WWW0sSVSQ95UUk8kxPvHVVs5JpX5K2hUgL.Fo-4SKMRe0e4e052dJLoIp-LxK.L1-eLBonLxK.L1-eLBonc1hnt', ' Apache': '8055912243399.308.1540944679070', ' un': '18501190439', ' SSOLoginState': '1540949359', ' WBtopGlobal_register_version': 'd7c69d5faf4232e8', ' SUB': '_2A2523XU_DeRhGeNH7lUZ8y3FyDyIHXVVq-H3rDV8PUNbmtAKLXHjkW9NSokVDQVSX51geKckPlhHh4Zi-Umf8M4r'}
    cookies1 = {' Apache': '837992107367.2892.1541032248480', ' TC-V5-G0': '8518b479055542524f4cf5907e498469', ' TC-Ugrow-G0': '370f21725a3b0b57d0baaf8dd6f16a18', ' ULV': '1541032248524:15:1:8:837992107367.2892.1541032248480:1540988856537', ' SUB': '_2A2523jlmDeRhGeNH7lUZ8y3FyDyIHXVVqi2urDV8PUNbmtAKLRjjkW9NSokVDQnWmlPBB0GHZgq6ullqxHJMPCpb', ' _s_tentry': '-', 'SINAGLOBAL': '6172144502425.479.1532653095927', ' wb_view_log_5957833930': '1536*8641.25', ' SSOLoginState': '1541032246', ' wvr': '6', ' TC-Page-G0': '841d8e04c4761f733a87c822f72195f3', ' SUHB': '0ftZqJF3Kd1zts', ' UOR': ',,www.baidu.com', ' ALF': '1572568245', ' SCF': 'AqP1aVKkZncIXoLZNrEXxRfGCwoyV490UXNr9mrorRn1A3yFLI0ku1q0BwOPaERnvp8orROquzFW1cdglYWS_10.', ' SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WWW0sSVSQ95UUk8kxPvHVVs5JpX5KzhUgL.Fo-4SKMRe0e4e052dJLoIp-LxK.L1-eLBonLxK.L1-eLBonc1hnt'}


    #两条cookies 第一条是除点赞接口的cookies，
    #第二条，爬取点赞接口时，请求数据会重定向，所以在写一条点赞接口的cookies，


    headers = {
        'Referer': 'https://s.weibo.com/weibo/%25E6%2597%25A0%25E5%258F%258C?topnav=1&wvr=6',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }


    #添加headers
    def start_requests(self):
        for i in range(1):
            url = 'https://s.weibo.com/weibo/%25E6%2597%25A0%25E5%258F%258C?page='+str(i)
            yield scrapy.Request(url=url,callback=self.parse,headers=self.headers,cookies=self.cookies)

    #使用框架的起始函数。用来循环搜索页爬取的页数，用来拼接

    def parse(self, response):
        link = re.findall('mid="(.*?)"',response.text,re.S)#正则匹配mid用来拼接评论，转发，点赞的接口id
        a = set(link)#去掉重复的id
        for i in a:
            #循环啊列表拼接三条接口，返回函数进行抓取。
            urls = 'https://weibo.com/aj/v6/comment/big?ajwvr=6&id='+str(i)+'&from=singleWeiBo'#一级评论
            yield scrapy.Request(url=urls, callback=self.parse1, headers=self.headers, cookies=self.cookies, meta={'meta': urls})#定义meta传一级评论url到parse1
            urls2 = 'https://weibo.com/aj/v6/mblog/info/big?ajwvr=6&id='+str(i)+'&page=2'#转发
            yield scrapy.Request(url=urls2, callback=self.parse3, headers=self.headers, cookies=self.cookies)
            urls3 = 'https://weibo.com/aj/v6/like/likelist?ajwvr=6&mid='+str(i)+'&issingle=1&type=0'#点赞
            yield scrapy.Request(url=urls3,callback=self.parse4,headers=self.headers,cookies=self.cookies1)


    def parse1(self,response):#一级评论函数
        item = WeiboItem()
        resp = json.loads(response.text)#利用json转码
        pinglun = resp['data']
        ping = pinglun['html']#转码后拿出html键里面的值，这里的值是一个.html格式的，所以刚用xpath匹配
        html = etree.HTML(ping)
        p1_name = html.xpath("//div[@class='WB_text']/a[1]/text()")#xpath匹配名称
        p1_neirong = html.xpath("//div[@class='list_con']/div[@class='WB_text']/text()")
        item['a']=dict(zip(p1_name,p1_neirong))
        yield item
        dianzanshu = html.xpath("//a[@class='S_txt1']/span/em[2]/text()")
        link1 = html.xpath("//div/@comment_id")#一级评论里可以找到二级评论需要拼接的id，用xpath获取到。
        mins = response.meta['meta']#yield传下来一级评论的url来进行二级评论的拼接。
        # https://weibo.com/aj/v6/comment/big?ajwvr=6&more_comment=big&root_comment_id=4290003108338239&is_child_comment=ture&id=4289923332780566&from=singleWeiBo
        for x in link1:#循环拼接二级评论的url，返回的二级评论
            urls1 = mins+'&root_comment_id='+str(x)+'&is_child_comment=ture&from=singleWeiBo'
            yield scrapy.Request(url=urls1,callback=self.parse2,headers=self.headers,cookies=self.cookies)


    def parse2(self,response):#二级评论抓取函数
        item = WeiboItem()
        erji = json.loads(response.text)
        pingl = erji['data']
        pingll = pingl['html']
        html1 = etree.HTML(pingll)
        p2_name = html1.xpath('//div[@class="WB_text"]/a/text()')
        p2_neirong = html1.xpath("//div[@class='list_con']/div[@class='WB_text']/text()")
        item['w'] = dict(zip(p2_name, p2_neirong))#两个列表进行拼接一一对应存入pymongo，字典形式
        yield item


    def parse3(self,response):#转发抓取函数，抓取原理与一级评论相同
        item = WeiboItem()
        zhuan = json.loads(response.text)
        zhuanf = zhuan['data']
        zhaunfa = zhuanf['html']
        html2 = etree.HTML(zhaunfa)
        z_name = html2.xpath('//div[@class="WB_text"]/a/text()')
        z_neirong = html2.xpath('//div[@class="WB_text"]/span/text()')
        item['v'] = dict(zip(z_name, z_neirong))#两个列表进行拼接一一对应存入pymongo，字典形式
        yield item


    def parse4(self,response):#点赞抓取函数，抓取原理同上
        item = WeiboItem()
        dianz = json.loads(response.text)
        dianza = dianz['data']
        dianzan = dianza['html']
        html3 = etree.HTML(dianzan)
        d_name = html3.xpath('//div[@class="WB_text"]/a/text()')
        d_neirong = html3.xpath('//div[@class="WB_text"]/span/text()')
        item['z'] = dict(zip(d_name, d_neirong))#两个列表进行拼接一一对应存入pymongo，字典形式
        yield item
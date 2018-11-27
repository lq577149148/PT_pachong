# -*- coding: utf-8 -*-
import scrapy,re,json,time
from lxml import etree


class JdwSpider(scrapy.Spider):
    name = 'jdw'
    # allowed_domains = ['https://search.jd.com/']
    # start_urls = ['http://https://search.jd.com//']

    #获取的cookies和headers信息，这里不用加，只是装逼
    cookies = {' PCSYCityID': '1', ' shshshfp': 'ef5018e1e041fdb879d4037734abfcb6', ' _gcl_au': '1.1.903569151.1541043798', ' wlfstk_smdl': 'ud521hybyc05wa1nmfdjrsvrgbfzqc0l', ' shshshsID': '13d2b1558dea39339e5cd1a13020bb1c_3_1541069483246', ' ceshi3.com': '000', ' unpl': 'V2_ZzNtbUpTExImARRTLB8MUWILFglKXkYUfVpAAClJDAdgAEdbclRCFXwURlRnGFwUZwMZX0RcQxBFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2VHgcVQNgCxJcQWdzEkU4dl15HF8BYzMTbUNnAUEpDEZRchkRBWQGG1tFX0MUdjhHZHg%3d', ' rkv': 'V0200', ' _tp': 'JLFCq4vlHGdDOM19WQ06D8wNCzTT2cpJq%2B62m3m4UaU%3D', ' 3AB9D23F7A4B3C9B': '7YDZ63HQHVSKSZS5LAJ54OHEYVGPY6YOO3EAVI3V6YTJU42YHBSBN5D5CZU4AKCUXZZBYWDARHESEF265STXWQBMMU', ' __jdc': '122270672', ' TrackID': '101FwpZnpq3zyG3nt1fo51xDdCSa3Y2hKJUDXAGHg8AU583BIz7hntqkFaTTxCtSbMGeCpmifPT7mSA9--Yxqo-xNfUhJUqb9onvq2VW1nU4', ' __jdb': '122270672.5.1248769102|5.1541068830', '__jdu': '1248769102', ' xtest': '3601.cf6b6759', ' ipLoc-djd': '1-72-2799-0', ' shshshfpb': '2e59c7261f4a0436bab8bfc8d42d6e7e95ba0b46bc222914a9533b0015', ' _pst': 'jd_71666f46be34b', ' unick': 'jd_71666f46be34b', ' pin': 'jd_71666f46be34b', ' __jdv': '122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_95a6b8c6f7ae495e98409c7ecaa362d7|1541043434402', ' shshshfpa': '4ea103e4-51d8-e086-b7aa-928dfc59535a-1537258497', ' qrsc': '3', ' __jda': '122270672.1248769102.1537258495.1541056901.1541068830.5', ' pinId': 'Rwqbdxl7javKB4ASueUNwbV9-x-f3wj7', ' thor': '18F8F44A03110915003456F24698202DB622EC81EE81E5451DFA12DBFF37E303A4963240B8391DA7F496E8148ABA39105697667C8E28FF208C6594C9941FD107ECD6DFE15336770183AB24E8AF1AFFEED7A0A9A86975C9C543A8497B276F66395C5470BF8A555C988E87BEE9E8CD9CD124329DA7A9BB3CE1353070FE66F1B65D42622B20A49955EF9B58C90177C19D9A530B1FEEFF49CA2385A5B2CED41E66B6'}
    headers = {
        'referer': 'https://item.jd.com/27155510320.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    cookies1 = {' _gcl_au': '1.1.110012713.1541074143', ' __jda': '122270672.1248769102.1537258495.1541068830.1541076028.6', ' unpl': 'V2_ZzNtbUpTExImARRTLB8MUWILFglKXkYUfVpAAClJDAdgAEdbclRCFXwURlRnGFwUZwMZX0RcQxBFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2VHgcVQNgCxJcQWdzEkU4dl15HF8BYzMTbUNnAUEpDEZRchkRBWQGG1tFX0MUdjhHZHg%3d', ' 3AB9D23F7A4B3C9B': '7YDZ63HQHVSKSZS5LAJ54OHEYVGPY6YOO3EAVI3V6YTJU42YHBSBN5D5CZU4AKCUXZZBYWDARHESEF265STXWQBMMU', ' shshshfpb': '2e59c7261f4a0436bab8bfc8d42d6e7e95ba0b46bc222914a9533b0015', ' pin': 'jd_71666f46be34b', ' __jdb': '122270672.3.1248769102|6.1541076028', ' _tp': 'JLFCq4vlHGdDOM19WQ06D8wNCzTT2cpJq%2B62m3m4UaU%3D', ' ipLoc-djd': '1-72-2799-0', ' PCSYCityID': '1', ' shshshsID': 'ecbb2125ac26b6d6956cd9e8751b9722_2_1541076942125', ' JSESSIONID': '77065106CEC3975791A4791761D1AA4B.s1', ' pinId': 'Rwqbdxl7javKB4ASueUNwbV9-x-f3wj7', ' __jdv': '122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_95a6b8c6f7ae495e98409c7ecaa362d7|1541043434402', ' __jdc': '122270672', ' unick': 'jd_71666f46be34b', ' ceshi3.com': '000', ' thor': '158C5A2E393D2A0FA7D4B839593522AC690682F993E3F80032AAE1E43B4330A81596F3DC1419107D0DA462CA03B7006197D092922ED9661475510FFF1BAF8D955FB58D517911C01E50EBBF5DFBB89DF4B76283E4DD75A659ED0239193184E3FC4F19DE35A2A61986B021050B4B8F747B755083C36C28D8E2904FC86F11B6362F6C67C442CF4472EAC3E0DC857076E6564B6FCE2E001030C66C9FC3BB2ED55DAA', ' cn': '1', ' TrackID': '101FwpZnpq3zyG3nt1fo51xDdCSa3Y2hKJUDXAGHg8AU583BIz7hntqkFaTTxCtSbMGeCpmifPT7mSA9--Yxqo-xNfUhJUqb9onvq2VW1nU4', ' _pst': 'jd_71666f46be34b', '__jdu': '1248769102', ' mt_xid': 'V2_52007VwMRV1ReVVIfSBpsVzdXQVZcC1pGTRxMWRliB0YHQVFRWk1VHFtVNVETV1xYWggXeRpdBW4fElJBWVJLH0ESXgRsAxdiX2hSahxMEF4BYQUVUm1YV1wY', ' user-key': 'fe0cafed-5b83-4eda-a6b8-b3bbbcf442bf', ' shshshfp': 'ef5018e1e041fdb879d4037734abfcb6', ' shshshfpa': '4ea103e4-51d8-e086-b7aa-928dfc59535a-1537258497'}
    headers1 = {
            'referer': 'https://search.jd.com/Search?keyword=%E5%A4%A7%E5%9C%B0%E7%93%9C&enc=utf-8'
    }

    #起始函数。页面分析，京东的商品信息，只能爬前三十条的详细页面，后三十条的详细页面的信息是通过XHR动态加载的，需要找接口，接口会重定向，
    #加referer即可，分析 接口url。。。主要log_id是一个时间戳，time.time（）获取到后，做四舍五入处理拼接上去，即可获取到后三十条的商品信息。
    def start_requests(self):
        url = 'https://search.jd.com/Search?keyword=%E5%A4%A7%E5%9C%B0%E7%93%9C&enc=utf-8'#页面url，前30条url
        a = time.time()
        b = '%.5f'%a
        urls = 'https://search.jd.com/s_new.php?keyword=%E5%A4%A7%E5%9C%B0%E7%93%9C&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%A4%A7%E5%9C%B0%E7%93%9C&stock=1&page=2&s=30&scrolling=y&log_id='+str(b)
        #后30条接口url
        yield scrapy.Request(url=urls,callback=self.parse4,headers=self.headers1)#yield到后30条的爬取函数
        time.sleep(5)
        # yield scrapy.Request(url=url,callback=self.parse,headers=self.headers,cookies=self.cookies)#yield到前30条的爬取函数


    # def parse(self, response):
    #     link = response.xpath("//div[@class='p-name p-name-type-2']/a/@href").extract()#xpath获取详细页的url
    #     for i in link:
    #         print(i)
    #         if len(i) <= 35:#有长id，过滤这些id
    #             urls = 'https:' + str(i)#拼接详细页id
    #             # print(urls)
    #             yield scrapy.Request(url=urls, callback=self.parse1, headers=self.headers, cookies=self.cookies)
    #
    #
    # def parse1(self,response):#获取详细页的信息
    #     name = response.xpath("//div[@class='itemInfo-wrap']/div[@class='sku-name']/text()").extract()
    #     price = response.xpath("//div[@class='dd']/span[@class='p-price']/span[@class='price J-p-31813557250']/text()").extract()
    #     jianjie = response.xpath("//div[@class='p-parameter']/ul[@class='parameter2 p-parameter-list']/li/text()").extract()
    #     lian = response.xpath("//div[@class='left-btns']/a/@data-id").extract()#从详细页获取详细页id，用来拼接评论页的url
    #     for z in lian:
    #         urlss = 'https://sclub.jd.com/comment/productPageComments.action?productId='+str(z)+'&score=0&sortType=5&page=0&pageSize=10'
    #         yield scrapy.Request(url=urlss,callback=self.parse2,headers=self.headers,cookies=self.cookies1)
    #
    # def parse2(self,response):#获取评论页的信息
    #     id = re.findall('"id":"(.*?)"', response.text)#使用正则匹配
    #     comments = re.findall('"content":"(.*?)"',response.text)
    #     c = dict(zip(id,comments))#两个列表一一对应成字典
    #     print(c)
        '''           
        
        
        
        ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑网页前三十条数据↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
        
        
        ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓网页后三十条数据↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
        
        
        
        '''
    def parse4(self,response):#都同上
        links = response.xpath("//div[@class='p-name p-name-type-2']/a/@href").extract()
        for i in links:
            print(i,'===========我是后30条商品==========')
            if len(i) <= 35:
                urls = 'https:' + str(i)
                # print(urls)
                yield scrapy.Request(url=urls, callback=self.parse5, headers=self.headers, cookies=self.cookies)

    def parse5(self,response):
        name = response.xpath("//div[@class='itemInfo-wrap']/div[@class='sku-name']/text()").extract()
        price = response.xpath(
            "//div[@class='dd']/span[@class='p-price']/span[@class='price J-p-31813557250']/text()").extract()
        jianjie = response.xpath(
            "//div[@class='p-parameter']/ul[@class='parameter2 p-parameter-list']/li/text()").extract()
        lian = response.xpath("//div[@class='left-btns']/a/@data-id").extract()
        for z in lian:
            urlss = 'https://sclub.jd.com/comment/productPageComments.action?productId='+str(z)+'&score=0&sortType=5&page=0&pageSize=10'
            yield scrapy.Request(url=urlss, callback=self.parse6, headers=self.headers, cookies=self.cookies1)

    def parse6(self,response):
        id = re.findall('"id":"(.*?)"', response.text)
        comments = re.findall('"content":"(.*?)"', response.text)
        c = dict(zip(id, comments))
        print(c)






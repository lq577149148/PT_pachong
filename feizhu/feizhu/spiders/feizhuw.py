# -*- coding: utf-8 -*-
import scrapy,re
import time
import random


class FeizhuwSpider(scrapy.Spider):
    name = 'feizhuw'
    # allowed_domains = ['https://hotel.fliggy.com/']
    # start_urls = ['http://https://hotel.fliggy.com//']
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    cookies = {' hng': 'CN%7Czh-CN%7CCNY%7C156', ' JSESSIONID': '1ADA742B865D4819D0020447E55406AF', 'cna': 'lJ7NE4VxPDoCAd6AtgmvN1FX', ' dnk': '%5Cu6211%5Cu4E00%5Cu4E0D%5Cu5C0F%5Cu5FC3luqun', ' _tb_token_': 'Tk3GMhEo6XJLGVeulKll', ' uc1': 'cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie21=U%2BGCWk%2F7p4mBoUyS4E9C&cookie15=UtASsssmOIJ0bQ%3D%3D&existShop=false&pas=0&cookie14=UoTYNOeAsOPr1w%3D%3D&tag=8&lng=zh_CN', ' UM_distinctid': '1673931e388728-06f2e72db5db2-514d2f1f-144000-1673931e3892f2', ' t': '2a5f199640642160e7ee4dcb2dfd295e', ' csg': '182bda0b', ' login': 'true', ' _l_g_': 'Ug%3D%3D', ' isg': 'BAEBa2O0PqYacFKSw6xT1KE9EE0RMGoHWrkTUGNQ9omdSigcqH5c8NWIKP6pwg1Y', ' tracknick': '%5Cu6211%5Cu4E00%5Cu4E0D%5Cu5C0F%5Cu5FC3luqun', ' lid': '%E6%88%91%E4%B8%80%E4%B8%8D%E5%B0%8F%E5%BF%83luqun', ' cookie1': 'AimaAngzx04FHuodaF9dPIGiBl1%2BV6ssvycr28b%2FV5g%3D', ' _nk_': '%5Cu6211%5Cu4E00%5Cu4E0D%5Cu5C0F%5Cu5FC3luqun', ' cookie2': '1fe700b3e85023ed50e4074815622408', ' chanelStatExpire': '"2018-11-25 10:13:46"', ' unb': '2819587827', ' sg': 'n78', ' cookie17': 'UUBZGJdYRoTyrw%3D%3D', ' CNZZDATA1253581663': '431915929-1542848091-https%253A%252F%252Flogin.taobao.com%252F%7C1542848091', ' chanelStat': '"Mw=="'}
    cookies1 = {' cookie2': '1fe700b3e85023ed50e4074815622408', ' _tb_token_': 'Tk3GMhEo6XJLGVeulKll', ' _l_g_': 'Ug%3D%3D', ' t': '2a5f199640642160e7ee4dcb2dfd295e', ' UM_distinctid': '1673931e388728-06f2e72db5db2-514d2f1f-144000-1673931e3892f2', ' _nk_': '%5Cu6211%5Cu4E00%5Cu4E0D%5Cu5C0F%5Cu5FC3luqun', ' csg': '182bda0b', ' cookie1': 'AimaAngzx04FHuodaF9dPIGiBl1%2BV6ssvycr28b%2FV5g%3D', ' tracknick': '%5Cu6211%5Cu4E00%5Cu4E0D%5Cu5C0F%5Cu5FC3luqun', ' VISITED_HOTEL_TOKEN': '1fef48c3-5bfc-4d64-8032-c5bb5feb347c', ' chanelStat': '"Mw=="', ' CNZZDATA1253581663': '431915929-1542848091-https%253A%252F%252Flogin.taobao.com%252F%7C1542857148', ' uc1': 'cookie14=UoTYNOeAty5O1w%3D%3D&lng=zh_CN&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&existShop=false&cookie21=VT5L2FSpccLuJBreK%2BBd&tag=8&cookie15=UIHiLt3xD8xYTw%3D%3D&pas=0', ' unb': '2819587827', 'cna': 'lJ7NE4VxPDoCAd6AtgmvN1FX', ' hng': 'CN%7Czh-CN%7CCNY%7C156', ' isg': 'BPf3noZdYDix5uS0KX49mmvvhutLotQ5YItF9kmkE0Yt-Bc6UYxbbrVZ3hgDEKOW', ' login': 'true', ' chanelStatExpire': '"2018-11-25 10:13:46"', ' cookie17': 'UUBZGJdYRoTyrw%3D%3D', ' sg': 'n78', ' JSESSIONID': '67E8CA3E37459DF9F6721F33C1A791A8', ' dnk': '%5Cu6211%5Cu4E00%5Cu4E0D%5Cu5C0F%5Cu5FC3luqun', ' lid': '%E6%88%91%E4%B8%80%E4%B8%8D%E5%B0%8F%E5%BF%83luqun'}

    headers1 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
        'referer': 'https://sec.taobao.com/query.htm',
    }
    cookies2 = {' _tb_token_': 'Tk3GMhEo6XJLGVeulKll', ' sg': 'n78', ' _nk_': '%5Cu6211%5Cu4E00%5Cu4E0D%5Cu5C0F%5Cu5FC3luqun', ' lid': '%E6%88%91%E4%B8%80%E4%B8%8D%E5%B0%8F%E5%BF%83luqun', ' hng': 'CN%7Czh-CN%7CCNY%7C156', ' UM_distinctid': '1673931e388728-06f2e72db5db2-514d2f1f-144000-1673931e3892f2', ' isg': 'BBgYtAsW9w2nh9uJElMqL8Aa6UagH2OsG35aa1IJZNMG7bjX-hFMGy5NIWX4fTRj', ' csg': '182bda0b', ' cookie1': 'AimaAngzx04FHuodaF9dPIGiBl1%2BV6ssvycr28b%2FV5g%3D', ' t': '2a5f199640642160e7ee4dcb2dfd295e', ' login': 'true', ' unb': '2819587827', ' cookie17': 'UUBZGJdYRoTyrw%3D%3D', ' cookie2': '1fe700b3e85023ed50e4074815622408', ' _l_g_': 'Ug%3D%3D', ' tracknick': '%5Cu6211%5Cu4E00%5Cu4E0D%5Cu5C0F%5Cu5FC3luqun', 'cna': 'lJ7NE4VxPDoCAd6AtgmvN1FX', ' dnk': '%5Cu6211%5Cu4E00%5Cu4E0D%5Cu5C0F%5Cu5FC3luqun', ' uc1': 'cookie14=UoTYNOeAty5O1w%3D%3D&lng=zh_CN&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&existShop=false&cookie21=VT5L2FSpccLuJBreK%2BBd&tag=8&cookie15=UIHiLt3xD8xYTw%3D%3D&pas=0'}
    headers3 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    cookies3 = {' isg': 'BOTkVwjZY6FRqJdtvl8ec1ReteLcYxfAD7qWT_4Fbq9yqYRzJozVdxiLbUEUcUA_', ' sg': 'n78', ' lid': '%E6%88%91%E4%B8%80%E4%B8%8D%E5%B0%8F%E5%BF%83luqun', ' cookie1': 'AimaAngzx04FHuodaF9dPIGiBl1%2BV6ssvycr28b%2FV5g%3D', ' _nk_': '%5Cu6211%5Cu4E00%5Cu4E0D%5Cu5C0F%5Cu5FC3luqun', ' unb': '2819587827', 'cna': 'lJ7NE4VxPDoCAd6AtgmvN1FX', ' t': '2a5f199640642160e7ee4dcb2dfd295e', ' _l_g_': 'Ug%3D%3D', ' cookie2': '1fe700b3e85023ed50e4074815622408', ' cookie17': 'UUBZGJdYRoTyrw%3D%3D', ' _mw_us_time_': '1542858666548', ' dnk': '%5Cu6211%5Cu4E00%5Cu4E0D%5Cu5C0F%5Cu5FC3luqun', ' uc1': 'cookie14=UoTYNOeAty5O1w%3D%3D&lng=zh_CN&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&existShop=false&cookie21=VT5L2FSpccLuJBreK%2BBd&tag=8&cookie15=UIHiLt3xD8xYTw%3D%3D&pas=0', ' login': 'true', ' hng': 'CN%7Czh-CN%7CCNY%7C156', ' UM_distinctid': '1673931e388728-06f2e72db5db2-514d2f1f-144000-1673931e3892f2', ' _tb_token_': 'Tk3GMhEo6XJLGVeulKll', ' tracknick': '%5Cu6211%5Cu4E00%5Cu4E0D%5Cu5C0F%5Cu5FC3luqun', ' csg': '182bda0b'}


    def start_requests(self):
        # url2 = 'https://s.fliggy.com/visa/list.htm?spm=181.1109657.a1z68.32.3aac3ee1Ik1Erd&market=1&mq=%E9%9F%A9%E5%9B%BD'
        # yield scrapy.Request(url=url2,callback=self.parse_2,headers=self.headers3,cookies=self.cookies2)
        # for i in range(100):
        #     if i%20 == 0:
        url = 'https://hotel.fliggy.com/ajax/hotelList.htm?pageSize=20&currentPage=2&totalItem=16324&startRow=0&endRow=19&city=110100&tid=null&market=0&previousChannel=&u=null&detailLinkCity=110100&cityName=%E5%8C%97%E4%BA%AC&checkIn=2018-11-25&checkOut=2018-11-26&browserUserAgent=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20WOW64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F68.0.3440.75%20Safari%2F537.36&userClientIp=221.221.150.233&userSessionId=2819587827&offset=20&keywords=null&priceRange=R0&dangcis=null&brands=null&services=null&order=DEFAULT&dir=DESC&client=11.17.201.108&tagids=null&searchPoiName=undefined&pByRadiusLng=-1&pByRadiusLat=-1&radius=-1&pByRectMinLat=-1&pByRectMinLng=-1&pByRectMaxLat=-1&pByRectMaxLng=-1&lowPrice=-1'
        yield scrapy.Request(url=url,callback=self.parse,headers=self.headers,cookies=self.cookies)

    def parse(self, response):
        title = re.findall('"inRightMapHotelTitle":"(.*?)"',response.text)
        didian = re.findall('"businessAreas":(.*?),',response.text)
        yuding = re.findall('"latestBookingTips":"(.*?)",',response.text)
        pingfen = re.findall('"rateScore":"(.*?)",',response.text)
        duoping = re.findall('"rateNum":"(.*?)",',response.text)
        jiage = re.findall('"priceDesp":"(.*?)",',response.text)
        shid = re.findall('"shid":(.*?),',response.text)
        print(title)
        print(didian)
        print(yuding)
        print(pingfen)
        print(duoping)
        print(jiage)
        print(shid)
        for i in shid:
            urls = 'https://hotel.fliggy.com/hotel_detail2.htm?spm=181.7087309.0.0.5b3fec74acYoBm&searchBy=&shid='+str(i)+'&city=110100'
            time.sleep(random.randint(1,5))
            yield scrapy.Request(url=urls,callback=self.parse_1,headers=self.headers1,cookies=self.cookies1,dont_filter=True)

    def parse_1(self ,response):
        name = re.findall('<title>(.*?)</title>',response.text)
        chuli = response.xpath("//tr[@class='first']/td[@class='item-elapsed J_FloatTip']//text()").extract()
        chengong = response.xpath('//*[@id="J_RoomList"]/div[1]/div/div[2]/table/tbody/tr/td/text()').extract()
        fangxing = response.xpath('//*[@id="J_RoomList"]/div[1]/div/div[2]/table/tbody/tr/td[4]/p/a/text()').extract()
        jiage = response.xpath('//*[@id="J_RoomList"]/div[1]/div/div[2]/table/tbody/tr/td[6]/div/div/span/text()').extract()
        jiudianjieshao = response.xpath("//div[@class='hotel-facility-desc']/div[@id='hotel-desc']/div[@class='bd']/text()").extract()
        pinglun = response.xpath("//div[@class='tb-r-body']/div[@class='tb-r-cnt']/text()").extract()
        pingname = response.xpath("//div[@class='tb-r-buyer']/div[@class='tb-r-nick']/a/text()").extract()
        ping = dict(zip(pingname,pinglun))
        print("酒店名称",name)
        # print("处理时长",chuli)
        # print("成功几率",chengong)
        # print("酒店房型",fangxing)
        print("房间价格",jiage)
        print("酒店介绍",jiudianjieshao)
        print("评论",ping)

    # def parse_2(self, response):
    #     link = response.xpath("//td[@class='item-info']/div[@class='item-info-content']/a/@href").extract()
    #     for i in link:
    #         print(i)
    #         url = 'http://'+str(i)
    #         print(url)
    #         print(random.randint(3,5))
    #         yield scrapy.Request(url=url,callback=self.parse_3,headers=self.headers3,cookies=self.cookies3)
    #
    # def parse_3(self, response):
    #     name = response.xpath("//div[@class='item-title']/h1[@class='title-txt']/span[1]/text()").extract()
    #     print(name)

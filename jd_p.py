import requests
import re,time
from lxml import etree
# for i in range(1,2,2):
#     headers = {
#         'referer': 'https://search.jd.com/Search?keyword=ipad&enc=utf-8&wq=ipa&ev=exbrand_Apple%5E&page=1',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
#     }
#     url = 'https://search.jd.com/Search?keyword=ipad&enc=utf-8&wq=ipa&ev=exbrand_Apple%5E&page='+str(i)
#     response = requests.get(url,headers=headers)
#     response.encoding = response.apparent_encoding
#     html = etree.HTML(response.text)
#     prict = html.xpath("//div[@class='gl-i-wrap']/div[@class='p-price']/strong/i/text()")#标题
#     print(response.text)
#     html = etree.HTML(response.text)
#     data_stu = re.findall('<li data-sku="(.*?)" class="gl-item">',response.text)
#     list_id = ''
#     for id in  data_stu:
#         list_id = list_id+","+id
#         new_url = 'https://item.jd.com/'+str(id)+'.html'
#         print(new_url)
#         resp = requests.get(new_url, headers=headers)
#         resp.encoding=resp.apparent_encoding
#         html1 = etree.HTML(resp.text)

        # title = html1.xpath("//div[@class='itemInfo-wrap']/div[@class='sku-name']/text()")
        # if len(title) == 2:
        #     title = title[1].strip()
        # else:
        #     title = title[0].strip()
        # print(title)
#后三十条接口referer
headers = {
    'referer': 'https://search.jd.com/Search?keyword=ipad&enc=utf-8&wq=ipa&ev=exbrand_Apple%5E'
}
a =time.time()
b = '%.5f'%a
url = 'https://search.jd.com/s_new.php?keyword=ipad&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&wq=ipa&ev=exbrand_Apple%5E&page=2&s=27&scrolling=y&log_id='+str(b)
response = requests.get(url=url,headers=headers)
html = etree.HTML(response.text)
link = html.xpath("//div[@class='p-name p-name-type-2']/a/@href")#xpath匹配详情页链接
print(link)
for i in link:
    print(i)
# data_stu2 = re.findall('<li data-sku="(.*?)" class="gl-item">', response.text)
# for id2 in data_stu2:
#     new_url2 = 'https://item.jd.com/' + str(id2) + '.html'
#     print(new_url2)

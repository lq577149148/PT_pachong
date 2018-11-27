import requests

# 蘑菇代理的隧道订单
appKey = "dXNMR0I5S1hNRHN5ZUN5TDpaSWpRUktoWkd1aFZRRGNP"

# 蘑菇隧道代理服务器地址
ip_port = 'transfer.mogumiao.com:9001'

# 准备去爬的 URL 链接
url = 'https://hotel.fliggy.com/hotel_list3.htm?cityName=%B1%B1%BE%A9&city=&keywords=&checkIn=2018-11-29&checkOut=2018-11-30&ttid=sem.000000736'

proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
print(proxy)
headers = {"Proxy-Authorization": 'Basic '+ appKey}
r = requests.get("https://ip.cn", headers=headers, proxies=proxy,verify=False,allow_redirects=False)
print(r.status_code)
print(r.content)
if r.status_code == 302 or r.status_code == 301 :
    loc = r.headers['Location']
    url_f = "https://ip.cn" + loc
    print(loc)
    r = requests.get(url_f, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
    print(r.status_code)
    print(r.text)
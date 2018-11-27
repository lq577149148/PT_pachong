def get_ip_port():
    url = 'XXXXXX'
    response = requests.get(url)
    proxies = {}
    ip_port = response.json()['msg'][0]['ip']+":"+response.json()['msg'][0]['port']
    return ip_port

def process_response(self,request,response,spider):
    print(response.status)
    if response.status >= 400:
        print(2222222222222222222222)
        ip = get_ip_port()
        print(ip)
        request.meta['proxy'] = 'http://' + ip
        return request
    else:
        if len(response.text) >10000:
            print(3333333333333333)
            return response
        else:
            print(44444444444444444444)
            ip = get_ip_port()
            print(ip)
            request.meta['proxy'] = 'http://' + ip
            return request

def process_exception(self,request, exception, spider):
    print(1231111111111111111111111111111111111111111111111111111)
    ip = get_ip_port()
    print(ip)
    request.meta['proxy'] = 'http://'+ip
    return request

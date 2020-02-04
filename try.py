import requests
from fake_useragent import UserAgent
proxy = '127.0.0.1:10809'
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}
ua=UserAgent()
header={'User-Agent':ua.random}
response = requests.get('https://httpbin.org/get', proxies=proxies,headers=header)
print(response.text)

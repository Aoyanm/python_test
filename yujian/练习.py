import json
import requests
joker = """
　　　　　　■　　　■■■■　　　■　　　■■　　■■■■■■　　■■■■■　　
　　　　　　■　　■■　　■■　　■　　　■　　　■　　　　　　　■　　　■■　
　　　　　　■　　■　　　　■　　■　　■■　　　■　　　　　　　■　　　　■　
　　　　　　■　　■　　　　■　　■　■■　　　　■　　　　　　　■　　　　■　
　　　　　　■　　■　　　　■　　■■■　　　　　■　　　　　　　■　　　■■　
　　　　　　■　　■　　　　■　　■■■■　　　　■■■■■■　　■■■■■　　
　　　　　　■　　■　　　　■　　■　　■　　　　■　　　　　　　■　　■　　　
　■　　　　■　　■　　　　■　　■　　■■　　　■　　　　　　　■　　■■　　
　■　　　　■　　■　　　　■　　■　　　■　　　■　　　　　　　■　　　■　　
　■■　　■■　　■■　　■■　　■　　　■■　　■　　　　　　　■　　　■■　
　　■■■■　　　　■■■■　　　■　　　　■　　■■■■■■　　■　　　　■　
"""
print(joker)
# iurl = str(input('url:'))
iurl = 'a0yanm.com'
from bs4 import  BeautifulSoup
# with open('data.json','r') as b:
#     a = json.load()
#     print(b)

# for f in open('data.json','r'):
#     print(f['url'])
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}
file = open('data.json','r')
data = json.load(file)
url =requests.get(url='http://127.0.0.1/about/_notes/dwsync.xml',headers=headers)

# if url.status_code == 404:
#     print("不存在")
# elif url.status_code == 200:
#     print("存在")

for f in data:
    cmsurl = f['url']
    cmsname = f['name']
    url = 'http://' + iurl + cmsurl
    cmsur = requests.get(url=url,headers=headers)
    if cmsur.status_code == 200:
        print(url)
        print(cmsname)

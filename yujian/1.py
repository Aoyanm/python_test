import requests
import re
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import sys
import time
requests.packages.urllib3.disable_warnings()

inurl = sys.argv
inurl = inurl[1]
tim = time.strftime("%m%d", time.localtime())

ua = UserAgent()
headers = {"User-Agent": ua.random}
fo = open('test.txt',"r")#读取字典

#通过输入来改善http链接语句
def url(name):
    newurl = re.search('http', name)

    if newurl is None:
        urlname = 'http://' + name + '/'
    elif name[0:5] == 'https':
        urlname = name
    else:
        urlname = name

    return urlname

def lu_list(name):
    mulu_dict = []

    for mulu_list in fo:
        mulu = name + mulu_list
        mulu = mulu.strip()
        mulu_dict.append(mulu)

    return mulu_dict

def Suurl_list(mulu_dict):
    Suurl = []
    for Su in mulu_dict:
        Surviveurl = requests.get(url=Su,headers=headers,allow_redirects=False,verify=False)
        sta = Surviveurl.status_code
        if sta == 200:
            Suurl.append(Su)

    return Suurl

def title(inurl,Suurl):
    txtnme = (inurl + '_' + tim + '.txt')
    txtnme = str(txtnme)

    for china in Suurl:
        f = open(txtnme, 'a+')
        curl = requests.get(url=china,headers=headers,allow_redirects=False,verify=False)
        curl = BeautifulSoup(curl.text,'html.parser')
        r1 = curl.find(name='title')
        if r1 is None:
            r1 = '标题为空'
        r1 = str(r1)
        china = str(china)
        f.write(r1 + '\n' + china + '\n'+ '\n')
        # print(r1 + '\n' + china + '\n')

title(inurl,Suurl_list(lu_list(url(inurl))))




# def yujian(url):
#     for mulu_list in fo:
#         paurl = url + mulu_list
#         str(paurl)
#         r = requests.get(url=paurl,headers=headers,allow_redirects=False,verify=False)
#         status = r.status_code
#         if status == 200:
#             url200.append(paurl)






















# if inurl is None: #如有http直接判断是否为http或者https
#     url = 'http://' + inurl + '/'
#     inurl = str(url)
# elif inurl[0:5] == 'http:':
#     yujian(inurl)
#     print(url200)
# elif inurl[0:5] == 'https':
#     yujian(inurl)
#     print(inurl)
# else:
#     yujian(inurl)
#     print(url200)
# def yujian(url):
#     fo = open('bc.txt',"r")
#     for f in fo:
#         ua = UserAgent()
#         headers = {"User-Agent": ua.random}
#         paurl = url + f
#         r = requests.get(url=paurl,headers=headers,allow_redirects=False,verify=False)
#         status = r.status_code
#         if status == 200:
#             url200.append(paurl)





import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent()
headers = {"User-Agent":ua.random}
#print (headers)

html = requests.get('https://github.com/login',headers=headers)
htmlyuan = BeautifulSoup(html.text,"html.parser")
token = htmlyuan.find(name='input',attrs={'name':'authenticity_token'}).get('value')
#print (token)

h_cookies = html.cookies.get_dict()
'''

commit: Sign in
utf8: ✓
authenticity_token: XUHz+dqHDiUhDOzG+QQkiIRGXkHA0WLJl/UUCpeKXMIAvU5OCY2Ra93hFHRdZ51AkSCO/t3byUDwvWba8jCaeQ==
login: 123213
password: 123213
'''


payload = {
    'commit':'Sign in',
    'utf8':'✓',
    'authenticity_token':token,
    'login':'563360925@qq.com',
    'password':'qwer563360925.'
}

cookies = requests.post('https://github.com/session',data=payload,cookies=h_cookies)
cookiesdict = cookies.cookies.get_dict()
#print (cookiesdict)
#print (h_cookies)
cookies_dict = {}
cookies_dict.update(cookiesdict)
cookies_dict.update(h_cookies)
email = requests.get('https://github.com/settings/emails',cookies=cookies_dict)
#htmlmail = BeautifulSoup(email.text,'html.parser')
print (email.text)

#li = htmlmail.find(name='li',attrs={'class':'Box-row clearfix css-truncate settings-email'})
#print (li)
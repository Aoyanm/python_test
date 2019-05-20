import requests
import re
import threading
import json

print('banner')
banner ="""
 _   _            _     ____                  
| | | | __ _  ___| | __/ ___|  ___ __ _ _ __  
| |_| |/ _` |/ __| |/ /\___ \ / __/ _` | '_ \ 
|  _  | (_| | (__|   <  ___) | (_| (_| | | | |
|_| |_|\__,_|\___|_|\_\|____/ \___\__,_|_| |_|

"""
print('[1]CMS识别与CMS特殊路径收集')
print('[2]敏感目录扫描')
print(banner)
xz = input('请选择:')


def ini():
    global e
    import configparser
    conf = configparser.ConfigParser()
    cmserror = []
    conf.read('hackscan.ini')
    error = conf.get('cmscanerror', 'error')
    error1 = conf.get('cmscanerror', 'error1')
    error2 = conf.get('cmscanerror', 'error2')
    error3 = conf.get('cmscanerror', 'error3')
    error4 = conf.get('cmscanerror', 'error4')
    error5 = conf.get('cmscanerror', 'error5')
    error6 = conf.get('cmscanerror', 'error6')
    error7 = conf.get('cmscanerror', 'error7')
    error8 = conf.get('cmscanerror', 'error8')
    error9 = conf.get('cmscanerror', 'error9')
    error10 = conf.get('cmscanerror', 'error10')
    error11 = conf.get('cmscanerror', 'error11')
    error12 = conf.get('cmscanerror', 'error12')
    cmserror.append(error1)
    cmserror.append(error2)
    cmserror.append(error3)
    cmserror.append(error4)
    cmserror.append(error5)
    cmserror.append(error6)
    cmserror.append(error7)
    cmserror.append(error8)
    cmserror.append(error9)
    cmserror.append(error10)
    cmserror.append(error11)
    cmserror.append(error12)
    for e in cmserror:
        pass


ini()


def cmsscan():
    user = input('输入要扫描的url：')
    print('[&]识别CMS，并扫描出CMS存活的路径')
    yuanheaders = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}
    yuan = user.rstrip().rstrip('/')
    yuans = requests.get(url=yuan, headers=yuanheaders, allow_redirects=False)
    yuanlen = len(yuans.text)

    print('[@]扫描中....')
    with open('data.json', 'r') as b:
        a = json.load(b)
        lisw = eval(str(a))
        for x in lisw:
            cms = x['url']
            cmsname = x['name']

            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}
            urls = user.rstrip().rstrip('/') + cms
            cmssb = requests.get(url=urls, headers=headers, allow_redirects=False)
            cmslen = len(cmssb.text)
            if cmssb.status_code == 200 and yuanlen != cmslen:
                print('[*]识别到的CMSurl：{}'.format(cmssb.url))
                print('[*]CMS为:{}'.format(cmsname))
            else:
                pass


def mgscan():
    user = input('输入要扫描的url：')
    with open('漏洞.txt', 'r') as a:
        for x in a.readlines():
            url = re.findall('(.*?)\|\|', x.strip())
            names = re.findall('\|\|(.*)', x.strip())
            urls = "".join(url)
            payload = user.rstrip().rstrip('/') + urls
            namess = "".join(names)
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}
            mgs = requests.get(url=payload, headers=headers, allow_redirects=False)
            if mgs.status_code == 200:
                if e in str(mgs.text):
                    pass
                else:
                    print('[*]扫描出的敏感目录:{}'.format(mgs.url))
                    print(namess)


def main():
    while True:
        if xz == '1':
            c = threading.Thread(target=cmsscan, args=())
            c.start()
            break
        elif xz == '2':
            mgscan()
            m = threading.Thread(target=mgscan, args=())
            m.start()
        else:
            print('[-]输入不能为空！')
            continue


main()
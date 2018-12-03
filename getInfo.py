#!/usr/bin/python
# -*- coding: utf-8 -*-
from queue import Queue
import threading
import requests
import sys

ThinkPHP = set()
q = Queue()
'''
从目标文件中读取指定条数的链接
'''
def load_file(fileName,start,nums):
    #target = set()
    with open(fileName,'r') as f:
        a = f.readlines()
        for i in range(start,nums):
            #target.add(i.strip('\n'))
            q.put(a[i].strip('\n'))
    #return target
'''
从目标链接中选择PHP
'''
def get_php(target):
    try:
        res = requests.get(target,timeout=1)
        origin = len(res.text)
    except:
        return
    if 'X-Powered-By' in res.headers:
        if 'PHP' in res.headers['X-Powered-By']:
            print('[PHP]PHP Find... '+target)
            if 'ThinkPHP' in res.headers['X-Powered-By']:
                print('[PHP]ThinkPHP Find... '+target)
                return 1
    else:
            try:
                res = requests.get(target+'/index.php',timeout=1,allow_redirects=False)
                now = len(res.text)
            except:
                return
            if res.status_code == 200 and (now+100)>=origin:
                print('[PHP]PHP Find... '+target)
'''
开始扫描
'''
def scan_thread():
    while not q.empty():
        target = q.get()
        if get_php(target):
            ThinkPHP.add(target)
        #if get_php(target):
            #info_scan(target)


'''
get infosec

def info_scan(target):
    try:
        res = requests.get(target+'/robots.txt',timeout=1)
    except:
        return
    if res.status_code == 200 and 'User-agent' in res.text:
        print('[INFO]robots find...,'+target+'robots.txt')
'''




if __name__ == '__main__':
    target = load_file('butian.txt',450,500)
    for i in range(20):
        t1 = threading.Thread(target=scan_thread)
        t1.start()

# -*- coding: utf-8 -*-
#!/usr/bin/env python
from queue import Queue
import threading
import requests
import sys

q = Queue()
'''
从目标文件中读取链接
'''
def load_file(fileName):
    with open(fileName,'r') as f:
        for i in f.readlines():
            q.put(i.strip('\n'))

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
            if 'ThinkPHP' in res.headers['X-Powered-By']:
                print('[PHP]ThinkPHP Find... '+target)
                return 1
'''
开始扫描
'''
def scan_thread():
    while not q.empty():
        target = q.get()
        get_php(target)


if __name__ == '__main__':
    target = load_file('php.txt')
    for i in range(50):
        t1 = threading.Thread(target=scan_thread)
        t1.start()

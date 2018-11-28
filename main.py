#!/usr/bin/env python
# -*- coding: utf-8 -*-
#主程序
import sys
import threading
from load import *
from queue import Queue

q = Queue()

def start_scan(poc_class):
    while not q.empty():
        target = q.get()
        #pong.scan(target)
        poc_class.scan(target)


if __name__ == '__main__':
    try:
        file = sys.argv[1]
        pocname = sys.argv[2]
    except:
        print('[Usage]'+sys.argv[0]+' <target_file> <pocname>')
        exit()
    target = loadFile(file)
    for i in target:
        q.put(i)
    poc_class = loadPoc(pocname)
    pong = poc_class()
    for i in range(10):
        t = threading.Thread(target=start_scan,args=(pong,))
        t.start()

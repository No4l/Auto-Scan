#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.dont_write_bytecode = True#不生成pyc文件
'''
从文件中读目标地址
target 目标网址
'''
def loadFile(fileName):
    target = set()
    with open(fileName,'r') as f:
        for i in f.readlines():
            target.add(i.strip('\n'))
    return target


'''
读取poc
p1 poc类
'''
def loadPoc(pocname):
    p1 = __import__('Poc.'+pocname,fromlist=True)
    p1 = getattr(p1,pocname)
    return p1

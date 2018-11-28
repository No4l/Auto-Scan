#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.dont_write_bytecode = True#不生成pyc文件
'''
从文件中读目标地址
'''
def load(fileName):
    target = set()
    with open(fileName,'r') as f:
        for i in f.readlines():
            target.add(i.strip('\n'))
    return target

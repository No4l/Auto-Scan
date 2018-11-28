#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")#先跳到上级目录下
sys.dont_write_bytecode = True#不生成pyc文件
from poc import Poc

class Get_sql(Poc):
    def scan(self,target):
        print(1111)

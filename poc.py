#!/usr/bin/env python
#coding:utf-8
#主程序
from abc import ABCMeta,abstractmethod,ABC
import sys
sys.dont_write_bytecode = True#不生成pyc文件

'''
抽象
python2 __metaclass__ = ABCMeta
python3 类继承ABC
'''
class Poc(ABC):
    #__metaclass__ = ABCMeta
    #metaclass = ABCMeta

    #抽象方法，继承的类需要实现
    @abstractmethod
    def scan(self,url): pass

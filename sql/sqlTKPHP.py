# -*- coding: utf-8 -*-
#!/usr/bin/env python
import requests
#from urllib.parse import urlparse
from bs4 import BeautifulSoup

url = 'http://www.uec.org.cn'
text = requests.get(url).text
href = []
html = BeautifulSoup(text,'lxml')
for i in html.find_all('a'):
    if 'id' in i.get('href'):
        

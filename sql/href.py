#coding:utf-8
#get href
from bs4 import BeautifulSoup
import requests
import sys
'''
wd 关键词
page 页数
返回 html源代码
'''
def getHtml(wd,page):
	html = ''
	header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
	}
	for i in range(1,page+1):
		url = "https://www.baidu.com/s?wd={0}&pn={1}".format(wd,i*10)
		html += requests.get(url,headers=header).text
	return html

'''
html html源代码
返回href
'''
def html2href(html):
	href = set()
	html = BeautifulSoup(html,'lxml')
	for i in html.find_all('a'):
		try:
			a = requests.get(i.get('href'),timeout=0.5).url
			#根据情况更改
			if "php" in a and "baidu" not in a:
				href.add(a)
				print(a)
		except:
			continue
	return href

'''
输出提示信息
'''
def Usage():
	print("[-]Example:"+sys.argv[0]+" <keyword> <page>")


def main():
	try:
		keyword = sys.argv[1]
		page = int(sys.argv[2])
	except:
		Usage()
		exit()
	html2href(getHtml(keyword,page))

if __name__ == '__main__':
	main()

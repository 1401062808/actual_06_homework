# coding:utf-8
import requests
from pyquery import PyQuery as pq
import os,sys
reload(sys)
sys.setdefaultencoding('utf-8')
# url = 'http://movie.douban.com/top250'
# url = 'http://t66y.com/index.php'

i = 1

for j in range(10)[1:10]:
	print j
	url = 'http://www.zhihu.com/people/auxten/answers?page=%s' % j
	res = requests.get(url)
	# for p in pq(res.content).find('.question_link'):
	# 	print i,p.text.encode('utf-8')
	# 	i += 1
	# print res.content
	for p in pq(res.content).find('.zm-item'):
		print '问题   ',i,pq(p).find('.question_link').text()
		print '-'*10
		print '点赞数  ',pq(p).find('.zm-item-vote').text()
		print '-'*10 + '\n'
		print '回答    ',pq(p).find('.content.hidden').text()
		
		i += 1


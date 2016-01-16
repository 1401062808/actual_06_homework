#coding:utf-8
from pyquery import PyQuery as pq
import requests

ql_list = []
zs_list = []
# page_counter = 1
for p in range(1,6):
    url = 'http://www.zhihu.com/topic/19776749/top-answers?page=%s' %(p)
    res = requests.get(url)
    question_link = pq(res.content).find('.question_link')
    zh_summary = pq(res.content).find('.zh-summary')
    for ql in question_link:
        ql_list.extend(['\nhttp://www.zhihu.com'+ pq(ql).attr('href')])
    for zs in zh_summary:
        zs_list.append(pq(zs).text())

#在不同页码出现IndexError: list index out of range的错误，原因？
for i in range(100):
    print '--------',i+1,'--------',
    print ql_list[i]
    print zs_list[i]

    # for i in range(page_counter,page_counter+19):
    #     if i < 101:
    #     print '--------', i ,'--------',
    #     print '\nhttp://www.zhihu.com'+ pq(question_link[i]).attr('href')
    #     print zh_summary[i]
    #     print pq(zh_summary[i]).text()
    #     page_counter += 20
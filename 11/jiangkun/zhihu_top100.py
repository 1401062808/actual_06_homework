# coding: utf-8
import requests
from pyquery import PyQuery as pq

question_num = 1
page_num = 1
to_stop = False
scrap_questions_num = 100

while True:
    url = "http://www.zhihu.com/topic/19776749/top-answers?page=%d" % (page_num)
    res = requests.get(url)
    # print res.encoding

    for p in pq(res.content).find('.feed-main'):
        # print type(p)
        print question_num, '. ' ,pq(p).find('.question_link').text()
        relative_link = pq(p).find('.question_link').attr('href')
        absolute_link = 'http://www.zhihu.com' + relative_link
        
        print '  链接 ', absolute_link
        print '  vote: ', pq(p).find('.zm-item-vote-count').text()
        print '  回答摘要'
        print ' ', pq(p).find('.zh-summary').text()[:-4]

        print '-' * 60
        print

        if question_num == scrap_questions_num:
            to_stop = True
            break
        question_num += 1

    page_num += 1
    if to_stop ==True:
        break
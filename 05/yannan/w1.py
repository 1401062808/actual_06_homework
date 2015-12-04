# -*- encoding: utf-8 -*-
__author__ = 'yannan'

'''
# 作业1

* 一个list[(1,4),(5,1),(2,3)],根据每个元组中的较大值进行排序
    - 期待结果：[(2,3),(1,4),(5,1)]
    - 要求：用sorted和lambda完成
    - 级别1：用lambda中用max
    - 级别2：lambda中不用max
    - 提示：True乘以4 ==4 Fale乘以2 == 0
'''

list_src=[(1,4),(5,1),(2,3)]

#print sorted(list_src)

#print max(list_src[1])

#print iter(list_src)

#lambda x:[sorted(list_src,key=i) for x in list_src if i=max(x)]
print sorted(list_src,key=lambda i:max(i))
print sorted(list_src,key=lambda i:min(i),reverse=True)


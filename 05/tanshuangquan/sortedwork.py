#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
一个list[(1,4),(5,1),(2,3)],根据每个元组中的较大值进行排序
期待结果：[(2,3),(1,4),(5,1)]
要求：用sorted和lambda完成
级别1：用lambda中用max
级别2：lambda中不用max
'''

print " 级别1：用lambda中用max"
print ">>>sorted(L, key = lambda x : max(x))"
L = [(1,4),(5,1),(2,3)]
print sorted(L, key = lambda x : max(x))

print " 级别2：lambda中不用max"
print ">>>sorted(L, key = lambda x : x[0] if (x[0] > x[1]) else x[1])"
L = [(1,4),(5,1),(2,3)]
print sorted(L, key = lambda x : x[0] if (x[0] > x[1]) else x[1])

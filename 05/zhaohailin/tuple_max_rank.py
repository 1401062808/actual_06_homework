#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-25 20:23:12
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# import os
mylist = [(1,4),(5,1),(2,3)]
print sorted(mylist,key=lambda x:max(x))
print sorted(mylist,key=lambda (x,y): x * (x > y) + y * (x <= y))

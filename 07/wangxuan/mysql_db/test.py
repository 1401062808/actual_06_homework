#!/usr/bin/env python
#-*-coding:utf8-*-
import db
#with open('../userdata','r') as f:
#	for line in f:
#		username = line.split()[0]
#		password = line.split()[1]
#		sqli = "INSERT INTO user VALUES('%s','%s')"%(username,password)
#		db.mysql(sqli)g
with open('../bookdata','r') as f:
	for line in f:
		bookname = line.split()[0]
		nums = line.split()[1]
		sqli = "INSERT INTO bookinfo VALUES('%s','%s','')"%(bookname,nums)
		db.mysql(sqli)

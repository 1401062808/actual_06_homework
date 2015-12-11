#!/usr/bin/env python
import MySQLdb as mysql

def get_data(sql_str):
	db = mysql.connect(host='127.0.0.1',user='root',passwd='lyao36843',db='liaoyao')
	db.autocommit(True)
	cur = db.cursor()
	cur.execute(sql_str)
	data = cur.fetchall()
	if len(data) == 0:
		return 'no result'
	else:
		return data

#sql = "select * from user where name='zhangsan'"
#print get_data(sql)

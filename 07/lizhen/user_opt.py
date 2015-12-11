#!/bin/env python
#!coding: utf-8
import MySQLdb as ml

conn = ml.connect(user='root',host='',port=3306,db='users',charset='utf8')
conn.autocommit(1)
cur = conn.cursor()
def show():
  sql = "select id,name,pass from user"
  cur.execute(sql)
  user_list = cur.fetchall()
  return user_list


def add(username,password):
  sql = "insert into user(name,pass) values(%s,%s)"
  cur.execute(sql,[username,password]) 
  return True

def userdel(userid):
  sql = "delete from user where id=%s"
  cur.execute(sql,[userid])
  return True

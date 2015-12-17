# -*- encoding: utf-8 -*-
__author__ = 'yannan'

import MySQLdb as mysql

def mysql_select(sql_comm):
    db = mysql.connect(user='reboot',passwd='reboot123',db='yanzilla')
    db.autocommit(True)
    cur = db.cursor()
    cur.execute(sql_comm)
    return cur.fetchall()

if __name__=='__main__':
    sql_comm = 'select * from userinfo'
    print mysql_select(sql_comm)

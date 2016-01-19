#!/usr/bin/env python
from flask import Flask,render_template,request
import MySQLdb as mysql
import json

app = Flask(__name__)

#connect to mysql
#con = mysql.connect(host='127.0.0.1',user='root',passwd='',db='liaoyao')
#con.autocommit(True)
#cur = con.cursor()

class DB():
    def __init__(self,host,user,passwd,db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.conn = None
        self._connect()
    
    def _connect(self):
        self.conn = mysql.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
        self.conn.autocommit(True)
    
    def execute(self,sql):
        msg='ok'
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
        except Exception,e:
            print e
            print 'reconnect db123'
            self._connect()
            cur = self.conn.cursor()
            try:
                cur.execute(sql)
            except:
                msg='error in sql'

            self.conn.close()
            cur.close()
        return {"cur":cur,"msg":msg}
    def add(self):
        pass
db = DB('127.0.0.1','root','','liaoyao')

@app.route('/',methods=['GET','POST'])
def index():
	print request.method
	if request.method == 'GET':
		return render_template('index.html')
	elif request.method == 'POST':
		sql = 'select * from server10'
		cur = db.execute(sql)
		return json.dumps(cur['cur'].fetchall())

@app.route('/addhost')
def addhost():
	name = request.args.get('name')
	mem = request.args.get('mem')
	end_date = request.args.get('end_date')
	sql = 'insert into server10 (name,memory,end_date) values ("%s",%s,"%s")' % (name,mem,end_date)
	#print sql
	#res = 'ok'
	#try:
	#	cur.execute(sql)
	#except:
	#	res = 'error in sql'
	#return res
	cur = db.execute(sql)
	return cur['msg']

@app.route('/delhost',methods=['POST'])
def delhost():
	id = request.form.get('id')
	sql = 'delete from server10 where id=%s' % id
	#cur.execute(sql)
	#res = 'ok'
	#try:
	#	cur.execute(sql)
	#except:
	#	res = 'error in sql'
	#return res
	res = 'ok'
	db.execute(sql)
	return res


if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=9092)

#!/usr/bin/env python
import MySQLdb as mysql
from flask import Flask,request,render_template
import json

app = Flask(__name__)

#connect to mysql
con = mysql.connect(user='root',passwd='',db='liaoyao')
con.autocommit(True)
cur = con.cursor()


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/list')
def list():
	sql = 'select * from server'
	cur.execute(sql)
	return json.dumps(cur.fetchall())

@app.route('/add')
def add():
	name = request.args.get('name')
	mem = request.args.get('mem')
	sql = 'insert into server (server,memory) values ("%s",%s)' % (name,mem)
	cur.execute(sql)
	return 'ok'

@app.route('/del')
def delete():
	server_id = request.args.get('id')
	sql = 'delete from server where id=' + server_id
	cur.execute(sql)
	return 'ok'
	
if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True,port=9092)

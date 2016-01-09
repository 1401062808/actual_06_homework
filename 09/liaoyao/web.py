#!/usr/bin/env python
from flask import Flask,render_template,request
import MySQLdb as mysql
import json

app = Flask(__name__)

#connect to mysql
con = mysql.connect(host='127.0.0.1',user='root',passwd='',db='liaoyao')
con.autocommit(True)
cur = con.cursor()

@app.route('/',methods=['GET','POST'])
def index():
	print request.method
	if request.method == 'GET':
		return render_template('index.html')
	elif request.method == 'POST':
		sql = 'select * from server10'
		res = cur.execute(sql)
		return json.dumps(cur.fetchall())


if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=9092)

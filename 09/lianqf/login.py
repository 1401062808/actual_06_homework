import MySQLdb as mysql
from flask import Flask,request,render_template,session,redirect,url_for
import json


app = Flask(__name__)
app.secret_key='slddosvdfdsfefewfdfdfsfefsaqegd'

db  = mysql.connect(host='192.168.31.222',user='python',passwd='123456',db='python')
db.autocommit(True)
cur = db.cursor()



@app.route('/')
def index():
	if 'username' not in session:
		return redirect(url_for('login'))
	else:
		return render_template('index.html')

@app.route('/userlist')
def userlist():
	sql = 'select * from usertable'
	cur.execute(sql)
	return json.dumps(cur.fetchall())

@app.route('/serverlist')
def serverlist():
	sql = 'select * from server'
	cur.execute(sql)
	return json.dumps(cur.fetchall())


@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/logout')
def logout():
	session.pop('username')
	return redirect(url_for('index'))

@app.route('/loginaction')
def loginaction():
	name = request.args.get('name')
	pwd = request.args.get("pwd")
	sql = "select user,password from usertable "
	cur.execute(sql)
	for data in cur.fetchall():
	    if name==data[0] and pwd == data[1]:
		session['username'] = 'admin'
		break
	return redirect(url_for('index'))

@app.route('/addserver')
def addserver():
	host = request.args.get('host') 
	memory = request.args.get('memory') 
	disk = request.args.get('disk') 
	cpu = request.args.get('cpu') 
	vendor = request.args.get('vendor') 
	sql = 'insert into server (host,memory,disk,cpu,vendor) values ("%s","%s","%s","%s","%s")' %(host,memory,disk,cpu,vendor)
	cur.execute(sql)
	return 'ok'

@app.route('/delserver')
def delserver():
	serverid = request.args.get('id') 
	sql = 'delete from server where serverid=' + serverid
	cur.execute(sql)
	return 'ok'

@app.route('/updateserver')
def updateserver():
	serverid = request.args.get('id') 
	host = request.args.get('host') 
	memory = request.args.get('memory') 
	disk = request.args.get('disk') 
	cpu = request.args.get('cpu') 
	vendor = request.args.get('vendor') 
	sql = 'update server set host = "%s",memory = "%s",disk = "%s",cpu = "%s",vendor = "%s" where serverid = %s' %(host,memory,disk,cpu,vendor,serverid)
	cur.execute(sql)
	return 'ok'



@app.route('/adduser')
def add():
	user = request.args.get('user') 
	pwd = request.args.get('pwd') 
	sql = "insert into usertable (user,password) values('%s','%s')" %(user,pwd)
	print sql
	cur.execute(sql)
	return 'ok'
	#return sql

@app.route('/deluser')
def deluser():
	userid = request.args.get('id') 
	sql = 'delete from usertable where id=' + userid
	cur.execute(sql)
	return 'ok'




if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=9011)
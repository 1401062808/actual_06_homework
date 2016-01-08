from flask import Flask,render_template,request,redirect,session,url_for
import MySQLdb as mysql
import json
con = mysql.connect(user = 'root', host = 'localhost', passwd = 'ciscoccnp', db = 'songxiang' )
con.autocommit(True)
cur = con.cursor()


app = Flask(__name__)
app.secret_key = 'sdf'

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/loginaction')
def loginaction():
	name = request.args.get('username')
	pwd = request.args.get('pwd')
	if name == 'admin' and pwd =='admin':
		session['username'] = 'admin'
		return redirect(url_for('index'))
	else:
		return redirect(url_for('login'))

@app.route('/logout')
def logout():
	session.pop('username')
	return redirect(url_for('index'))

@app.route('/',methods=['GET','POST'])
def index():
	if 'username' not in session:
		return redirect(url_for('login'))
	else:
		if request.method == 'GET':
			return render_template('index.html')
		elif request.method == 'POST':
			sql = 'select * from server10'
			res = cur.execute(sql)
			return json.dumps(cur.fetchall())

@app.route('/addhost')
def addhost():
	name = request.args.get('name')
	mem = request.args.get('mem')
	end_date = request.args.get('end_date')
	sql = 'insert into server10 (name,memery,end_date) values ("%s","%s","%s")' % (name,mem,end_date)
	print sql
	res = 'ok'
	try:
		cur.execute(sql)
	except:
		res = 'error in sql '
	return res

@app.route('/update')
def update():
	data_id = request.args.get('id')
	name = request.args.get('name')
	mem = request.args.get('mem')
	end_date = request.args.get('end_date')
	sql = 'update server10 set server10.name=%s,server10.memery=%s,server10.end_date=%s where server10.id=%s' % (name,mem,end_date,data_id)
	print sql
	res = 'ok'
	try:
		cur.execute(sql)
	except:
		res = 'error in sql '
	return res

@app.route('/delete')
def delete():
	data_id = request.args.get('id')
	sql = 'delete from server10 where id=%s' % data_id
	res = 'ok'
	try:
		cur.execute(sql)
	except:
		res = 'error in sql '
	return res
if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 1234,debug = True)

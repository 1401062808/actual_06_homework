from flask import Flask, render_template,url_for,redirect,request
import db

sql = 'select * from server'
db.cur.execute(sql)
User_pass = db.cur.fetchall()

def password_temp():
	d = {}
	for i in User_pass:
		d[i[1]] = i[2]
	return d


app = Flask(__name__)



@app.route('/')
def root():
	return redirect('/login')

@app.route('/index')

def index():
	return render_template('index.html',data = User_pass)

@app.route('/add')
def add_user():
	name = request.args.get('user')
	passwd = request.args.get('passwd')
	dic = password_temp()
	
	if name not in dic and passwd != '':
		sql_add = 'insert into server values ("%s",%s)' % (name, passwd)
		db.cur.execute(sql_add)
	return redirect('/index')

@app.route('/login')

def login():
	return render_template('login.html')

@app.route('/access')
def verify():
	name = request.args.get('username')
	passwd = request.args.get('password')
	dic = password_temp()

	if name in dic and dic[name] == passwd:
		return redirect('/index')
	else:
		return redirect('/login')

if __name__ == '__main__':
	app.run(host = '0.0.0.0',port = 1234,
		debug = True)
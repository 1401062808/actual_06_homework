#!/usr/bin/env python
from flask import Flask,render_template,request,redirect,url_for
import user
app = Flask(__name__)

@app.route('/')
def index():
	sql = "select * from user"
	result = user.get_data(sql)
	return render_template('index.html',data=result)

@app.route('/add')
def add():
	name = request.args.get('username')
	pwd = request.args.get('pwd')
	if not name or not pwd:
		return 'username or passwd is not null'
	else:
		sql = "select * from user where name='%s'" % (name.strip())
		name_result = user.get_data(sql)
		if name_result == 'no result':
			insert_sql = "insert into user (name,passwd) values ('%s','%s')" % (name.strip(),pwd.strip())
			user.get_data(insert_sql)
			return redirect(url_for('index'))
		else:
			return 'user is exist!'

@app.route('/del')
def delete():
	name = request.args.get('user')
	delete_sql = "delete from user where name='%s'"	% name
	user.get_data(delete_sql)
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=9999)

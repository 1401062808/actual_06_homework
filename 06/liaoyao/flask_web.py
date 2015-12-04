#!/usr/bin/env python
# -*- coding: utf-8 -*-  
from flask import Flask,request,render_template,redirect,url_for
app = Flask(__name__)

user_dict = {}
f = open('user.txt')
for line in f.readlines():
	tmp_list = line.strip().split()
	user_dict[tmp_list[0]] = tmp_list[1]
f.close()

@app.route('/')
def index():
	useradd = """<form action="/add">
			name:<input type="text" name="name">
			passwd:<input type="password" name="pwd">
			<input type="submit" >
		     </form>"""
	table_str = '<table border="1"><tr><td>user</td><td>pass</td><td>op</td></tr>'
	for user in user_dict:
		table_str += '<tr><td>%s</td><td>%s</td><td><a href="/delete?name=%s">delete</a></td></tr>' % (user,user_dict[user],user)
	end_str = '</table>'
	result = useradd + '\n' + table_str + end_str
	return result

@app.route('/add')
def add():
	user = request.args.get('name')
	passwd = request.args.get('pwd')
	if user in user_dict:
		return 'Error'
	else:
		if not user or not passwd:
			return 'Error'
		else:
			user_dict[user] = passwd
	return redirect(url_for('index'))

@app.route('/delete')
def delete():
	user = request.args.get('name')
	user_dict.pop(user)
	return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)

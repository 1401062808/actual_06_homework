# -*- coding:utf-8 -*-
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')

def index():
	global d
	f = open('data.txt','r')
	datas = f.readlines()
	f.close()
	for i in datas:
		temp = i.strip().split()
		d[temp[0]] = temp[1]
	web_head = '''
						<!DOCTYPE html>
			<html>
				<head>
					<title>form</title>
				</head>
				<body>
					<form action="/add" method="get" accept-charset="utf-8">
						user:
						<input type="text" name="user" value="" placeholder="">
						passwd:
						<input type="password" name="passwd" value="" placeholder="">
						<input type="submit" name="submit" value="">
					</form>
					<table action="/dele" border = '1'>
						<thead>
							<tr>
								<th>name</th>
								<th>passwd</th>
								<th>delete</th>
							</tr>
						</thead>
						<tbody>
			'''
	web_end = '''
								</tbody>
					</table>

				</body>
			</html>

			'''
	web_mid = ''
	for i in d:
		lines = ''
		lines = '''<tr><td>%s</td><td>%s</td><td><a   href="/dele?name=%s">删除</a></td></tr>''' % (i,d[i],i)
		web_mid = web_mid+lines


	return web_head + web_mid + web_end
@app.route('/add')
def add():
	global d
	name = request.args.get('user')
	passwd = request.args.get('passwd')
	if name in d:
		return "该用户已存在"
	else:
		f=open('data.txt','a+')
		user_passwd = '%s %s' % (name,passwd)
		f.writelines(user_passwd)
		f.close()
		return  index()
@app.route('/dele')
def delet():
	global d
	name = request.args.get('name')
	del d[name]
	re_write = ''
	re_writes = []
	for i in d:
		re_write = '%s %s\n' % (i,d[i])
		re_writes.append(re_write)
	f=open('data.txt','w+')
	f.writelines(re_writes)
	f.close()
	return index()
if __name__ == '__main__':
	d = {}
	# process()
	app.run(host='0.0.0.0',port = 1234,debug = True)
	
	# print d
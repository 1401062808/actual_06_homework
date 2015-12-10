# -*- coding:utf-8 -*-
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')

def index(n = 0):
	global d
	with open('data.txt','r') as f:
		datas = f.readlines()
	for i in datas:
		temp = i.strip().split()
		d[temp[0]] = temp[1]
	web_head = '''
						<!DOCTYPE html>
			<html>
				<head>
					<title>form</title>
					<link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.css">
					<style>
					#table{
						margin-top: 20px;

					}
					#form{
						margin-top: 20px;

					}
					</style>
				</head>
				<body>
					<div id="form" class="container">
					<form action="/add" method="get" accept-charset="utf-8" class="form-inline">
						<div>
						<label for="exampleInputName2">Name</label>
						<input type="text" name="user" value="" placeholder="">
						<label for="exampleInputName2">Password</label>
						<input type="password" name="passwd" value="" placeholder="">
						<button type="submit" name="submit" class="btn btn-primary" >添加用户</button>
						</div>
					</form>
					</div>
					<div id="table" class="container-fluid">
					<table class="table table-striped table-hover table-bordered" action="/dele" >
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
					</div>

				</body>
			</html>

			'''
	web_mid = ''
	for i in d:
		lines = ''
		lines = '''<tr><td>%s</td><td>%s</td><td><a href="/dele?name=%s">删除</a></td></tr>''' % (i,d[i],i)
		web_mid = web_mid+lines

	if n == 0:
		return web_head + web_mid + web_end
	elif n == 1:
		return web_head + web_mid + '''</tbody></table></div><script type="text/javascript">alert("该用户不存在")</script></body></html>'''
	elif n == 2:
		return web_head + web_mid + '''</tbody></table></div><script type="text/javascript">alert("错误的用户名或密码")</script></body></html>'''
@app.route('/add')
def add():
	global d
	name = request.args.get('user')
	passwd = request.args.get('passwd')
	if name in d:
		return index(1)
	elif name == "" or passwd == "" :
		return index(2)
	else:
		with open('data.txt','a+') as f:
			user_passwd = '%s %s\n' % (name,passwd)
			f.writelines(user_passwd)
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
	with open('data.txt','w+') as f:
		f.writelines(re_writes)
	return index()
if __name__ == '__main__':
	d = {}
	# process()
	app.run(host='0.0.0.0',port = 1234,debug = True)
	
	# print d
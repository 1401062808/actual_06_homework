#coding:utf-8
from flask import Flask, request, render_template
app = Flask(__name__)
user_dict = {}

@app.route('/')
def index():
	index_form = '''
	<form name="useradd" action="/useradd">
		username:<input name="username" type="text">
		password:<input name="password" type="password">
		<input type="submit" vaule="add">
	</form>
	'''
	index_table = '''<table border="1"><tr><th>user</th><th>passwd</th><th>delete</th></tr>'''

	with open('user.txt') as f:
		for l in f.xreadlines():
			username, password = l.strip().split(' ')
			user_dict[username] = password
	f.close()

	for i in user_dict:
		index_table += '<tr><td>%s</td><td>%s</td><td><a href="/userdel?username=%s">del</a></td></tr>' %(i, user_dict[i], i)
	index_table += '</table>'
	index_html = index_form + index_table

	return index_html

@app.route('/useradd')
def useradd():
	global user_dict
	userName = request.args.get('username')
	passWord = request.args.get('password')
	if len(userName) == 0 or len(passWord) == 0:
		return 'empty username or password'
	if userName not in user_dict:
		user_info = '%s %s\n' %(userName, passWord)
		with open('user.txt', 'a+') as f:
			f.write(user_info)
		f.close()
		return index()
	else:
		return 'username has already in user.txt'

@app.route('/userdel')
def userdel():
	global user_dict
	userName = request.args.get('username')
	if userName in user_dict:
		user_dict.pop(userName)
	with open('user.txt', 'w') as f:
		for i in user_dict:
			f.write('%s %s\n' %(i, user_dict[i]))
	f.close()
	return index()

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=9090, debug=True)


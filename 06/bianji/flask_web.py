#!/usr/bin/env python
#encoding:utf-8
__author__ = 'bianji'
from flask import Flask,render_template,request,redirect,url_for
import json

app = Flask(__name__)

filename = 'user.txt'
user_dict = {}
with open(filename,'rb') as file:
    for line in file:
        content = line.strip('\n').split(' ')
        user_dict[content[0]] = content[1]
    print user_dict

@app.route('/',methods=['GET','POST'])
def index():
    table = '''<table border=1><tr><td>username</td><td>password</td><td>operate</td></tr>'''
    for key,value in user_dict.iteritems():
        print key,value
        table += '<tr><td>%s</td><td>%s</td><td><a href="/del?username=%s">操作</a></td></tr>' % (key,value,key)
    table += '</table>'
    content = '''
        <html>
            <title>Python 666</title>
            <body>
            <form action="/add">
        username:<input type="text" name="username">password:<input name="password" type="password">
        <input type="submit" value="提交">
            </form>
                %s
            </body>
        </html>
    ''' % table
    return content

@app.route('/add')
def add():
    username = request.args.get('username')
    password = request.args.get('password')
    if username is None or username.strip() == '' or username in user_dict:
        return '用户名输入不合法或已经存在'
    if password is None or password.strip() == '':
        return '密码输入不合法'
    user_dict[username.encode('utf-8')] = password.encode('utf-8')
    print user_dict
    with open(filename,'wb') as file:
        for key,value in user_dict.iteritems():
            file.write('%s %s\n' % (key,value))
    return redirect(url_for('index'))

@app.route('/del')
def delete():
    username = request.args.get('username')
    print username
    if username in user_dict:
        user_dict.pop(username)
    with open(filename,'wb') as file:
        for key,value in user_dict.iteritems():
            file.write('%s %s\n' % (key,value))
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
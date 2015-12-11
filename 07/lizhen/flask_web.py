#!/bin/env python
#coding: utf-8
from flask import Flask,request,render_template,redirect,url_for
#import user_gener
import user_opt

app = Flask(__name__)

@app.route('/')
def index():
  users = user_opt.show() 
  return render_template('index.html',users=users)
@app.route('/add')
def useradd():
  username = request.args.get('username')
  password = request.args.get('password')
  if len(username.strip())== 0:
    return redirect("/")
  user_opt.add(username,password)
  return redirect(url_for('.index'))
@app.route('/del')
def userdel():
  username = request.args.get('userid')
  print username 
  user_del = user_opt.userdel(username)
  return redirect("/")
@app.errorhandler(404)
def page_not_found(error):
    print "error:",error
    home_url = "您要访问的页面不存在,<a href='/')>点我返回首页</a>"
    return home_url

if __name__ == "__main__":
  # defult host=localhost port=5000
  app.run(host='0.0.0.0',port=9998,debug=True)

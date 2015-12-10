#!/bin/env python
#coding: utf-8
from flask import Flask,request,render_template,redirect
#import user_gener
import htmlgener

app = Flask(__name__)

@app.route('/')
def show():
  tr_str = ''
  users = htmlgener.show()
  for user in users:
    tr_str += """
      <tr><form action="/del">
        <td><input name='username'  value = %s  type='hidden'>%s</input> <td>
        <td>%s <td>
        <td>
            <input type="submit" value="DEL"> </input>
        <td></form>
      </tr>
   
    """ %(user,user,users[user])
  html = htmlgener.htmlgener(tr_str)
  return html
@app.route('/add')
def useradd():
  username = request.args.get('username')
  password = request.args.get('password')
  if len(username.strip())== 0:
    return redirect("/")
  htmlgener.add(username,password)
  return redirect('/')
@app.route('/del')
def userdel():
  username = request.args.get('username')
  print username 
  user_del = htmlgener.userdel(username)
  return redirect("/")
@app.errorhandler(404)
def page_not_found(error):
    print "error:",error
    home_url = "您要访问的页面不存在,<a href=\"/\">点我返回首页</a>"
    return home_url

if __name__ == "__main__":
  # defult host=localhost port=5000
  app.run(host='0.0.0.0',port=9998,debug=True)

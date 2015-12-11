# -*- encoding: utf-8 -*-
__author__ = 'yannan'
from flask import Flask,request,render_template,redirect,url_for
import conn_db
app = Flask(__name__)
@app.route('/')
def index():
    sql_comm = 'select * from userinfo'
    return render_template("index.html",data=conn_db.mysql_select(sql_comm))
@app.route('/add')
def add():
    user = request.args.get('user')
    pwd = request.args.get('pwd')
    sql_comm = 'select username from userinfo where username ="%s"' %(user)
    user_exist = conn_db.mysql_select(sql_comm)
    if not user or not pwd:
        return '<p>need user and pwd</p>'+redirect(url_for('index'))
    elif user_exist:
        return '<p>user exist</p>'+redirect(url_for('index'))
    else:
        sql_comm = 'insert into userinfo(username,password) values("%s","%s")' %(user,pwd)
        conn_db.mysql_select(sql_comm)
    return redirect(url_for('index'))
@app.route('/delete')
def delete():
    user = request.args.get('user')
    sql_comm='delete from userinfo where username="%s"' %(user)
    conn_db.mysql_select(sql_comm)
    return redirect(url_for('index'))
if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0",port=9527)
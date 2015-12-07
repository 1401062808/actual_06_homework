#!/usr/bin/env python
#encoding:utf-8
__author__ = 'bianji'
from flask import Flask,request,redirect,\
    url_for,render_template,g,flash,abort
import MySQLdb as mysql



app = Flask(__name__)
@app.before_request
def before_request():
    g.db = mysql.connect(host='10.37.253.60',user='bianji',passwd='bianji123',\
                     db='homework',charset='utf8')
    g.cursor = g.db.cursor()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/',methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        try:
            g.cursor.execute("INSERT INTO user(username,password) VALUES ('%s','%s')" % (name,password))
        except Exception as e:
            abort(500)
        return redirect(url_for('index'))
    g.cursor.execute("SELECT * FROM `user`")
    data = g.cursor.fetchall()
    print data
    return render_template('homework.html',userdata = data)


@app.route('/del',methods=['POST'])
def delete():
    if request.method == 'POST':
        username = request.form.get('username')
        g.cursor.execute("DELETE FROM `user` WHERE username='%s'" % username)
        return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
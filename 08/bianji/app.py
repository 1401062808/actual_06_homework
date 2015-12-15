#!/usr/bin/env python
#encoding:utf-8
__author__ = 'bianji'
from flask import Flask,render_template,jsonify,request,g
import MySQLdb as mysql
from flask.ext.login import login_required
app = Flask(__name__)

@app.before_request
def before_request():
    g.db = mysql.connect(host='10.37.253.60',user='bianji',passwd='bianji123',\
                     db='homework',charset='utf8')
    g.cursor = g.db.cursor()


@app.after_request
def afert_request(response):
    g.db.close()
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/userlist')
def userlist():
    g.cursor.execute("SELECT COUNT(*) FROM `user`")
    g.cursor.execute("SELECT * FROM `user`")
    data = g.cursor.fetchall()
    print len(data)
    return jsonify(code=200,message=data)


@app.route('/add',methods=['POST'])
def adduser():
    username = request.form['username']
    password = request.form['password']
    try:
        g.cursor.execute("INSERT INTO user(username,password) VALUES ('%s','%s')" % (username,password))
    except Exception as e:
        return jsonify(code=500,message=str(e))
    else:
        return jsonify(code=200,message='success')


@app.route('/del',methods=['POST'])
def deluser():
    username = request.form['username']
    print username
    try:
        g.cursor.execute("DELETE FROM `user` WHERE username='%s'" % username)
    except Exception as e:
        return jsonify(code=500,message=str(e))
    else:
        return jsonify(code=200,message='success')

if __name__ == '__main__':
    app.run(debug=True)
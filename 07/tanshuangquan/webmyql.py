# coding=utf-8
from flask import Flask,request,render_template
import MySQLdb as mysql
app=Flask(__name__)

con = mysql.connect(user='vip',passwd='211',db='vipuser',host='localhost',charset='utf8')
con.autocommit(True)
cur=con.cursor()

udic={}
sql='select name,pwd from user;'
cur.execute(sql)
for i in cur.fetchall():
    udic[i[0]] = i[1]

print udic

@app.route('/',methods=["GET"])
def index():
    return '<a href="/login"> Welcome to new World</a>'


@app.route('/login',methods=["GET"])
def login():
    return render_template("user.html",users=udic)

@app.route('/add',methods=["GET"])
def adduser():
    name=request.args.get('name')
    password=request.args.get('pwd')
    if name in udic or name=="" or password=="":
        return '<a href="/login"> Welcome to new World</a>'
    else:
        udic[name]=password
        print udic
        name=name.encode('utf-8')
        password= password.encode('utf-8')
        sql= 'insert user values ("%s","%s")' % (name,password)
        cur.execute(sql)
    #return 'ok'
    return render_template("user.html",users=udic)

@app.route('/del',methods=["GET"])
def deluser():
    user=request.args.get('user')
    del udic[user]
    user=user.encode('utf-8')
    sql='delete from user where name="%s"' % (user)
    cur.execute(sql)
    return render_template("user.html",users=udic)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9002,debug=True)

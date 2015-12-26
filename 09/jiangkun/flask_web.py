# coding:utf-8
from flask import Flask,request,render_template,session,redirect,url_for
# import datetime

app = Flask(__name__)
# session必须配置一个加密密钥
app.secret_key='adfdsafjk;l!#$dadfdsafasdfsaf'


import MySQLdb as mysql
import json
import datetime

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            # return obj.strftime('%Y-%m-%dT%H:%M:%SZ')
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


con= mysql.connect(user="root",passwd="redhat",db="jiangkun")
con.autocommit(True)
cur = con.cursor()

@app.route('/')
def index():
    if 'username' not in session:
        print url_for('login')
        return redirect(url_for('login'))
    else:
        return render_template('index.html')


@app.route('/loginaction')
def loginaction():
    name = request.args.get('name')
    pwd = request.args.get('pwd')

    sql='select passwd from user where name="%s"' % name
    cur.execute(sql)
    res_tuple = cur.fetchall()
    pwd_db = res_tuple[0][0]

    print "*"*20
    print res_tuple
    if name == name and pwd == pwd_db:
        session['username'] = name
    
    print url_for('index')
    return redirect(url_for('index'))
    # else:
    #     pass
    #     return 'error'


@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('index'))


@app.route('/list')
def list():
    sql='select * from server'
    cur.execute(sql)
    res_tuple = cur.fetchall()

    # res_json = json.dumps(res_tuple)
    # TypeError: datetime.datetime(2017, 1, 1, 0, 0) is not JSON serializable
    res_json = json.dumps(res_tuple, cls = DatetimeEncoder)
    return res_json


@app.route('/add')
def add():
    name = request.args.get('name')
    mem = request.args.get('mem')
    expiredDate = request.args.get('expiredDate')

    sql = 'insert into server (host, memory, expiration_time) values ("%s",%s, "%s")'%(name, mem, expiredDate)
    cur.execute(sql)
    return 'ok'


@app.route('/del')
def delelt():
    server_id = request.args.get('id')
    sql='delete from server where id='+server_id
    cur.execute(sql)
    return 'ok'


@app.route('/login')
def login():
    return render_template('login.html')


if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=9092)
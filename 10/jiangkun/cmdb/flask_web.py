# coding: utf-8
from flask import Flask, render_template, request
import MySQLdb as mysql
import json

con = mysql.connect(host='127.0.0.1', user='root',
                    passwd='redhat', db='jiangkun')
con.autocommit(True)
cur = con.cursor()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # print request.method
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        sql = 'select * from server10'
        cur.execute(sql)
        res = cur.fetchall()
        # print res
        # print json.dumps(res)
        return json.dumps(res)


@app.route('/searchbyid')
def search_host():
    host_id = request.args.get('id')

    sql = 'select * from server10 where id=%s' % (host_id)

    try:
        cur.execute(sql)
        res = cur.fetchall()
    except:
        res = 'error'

    return json.dumps(res)


@app.route('/addhost')
def add_host():
    name = request.args.get('name')
    mem = request.args.get('mem')
    end_date = request.args.get('end_date')
    sql = 'insert into server10 (name, memory, end_date) values ("%s", %s, "%s")' % (
        name, mem, end_date)

    res = 'ok'
    # print sql
    try:
        cur.execute(sql)
    except:
        # except (attrubutibe Error,mysqldb.opeartionError)
        # 捕获mysql.operationerror
        res = 'error in sql'
        # 打印日志

    return res


@app.route('/delhost')
def del_host():
    del_id = request.args.get('id')
    sql = 'delete from server10 where id=%s' % (del_id)
    res = 'ok'
    try:
        cur.execute(sql)
    except:
        res = 'error in sql'

    return res


@app.route('/modhost')
def mod_host():
    mod_id = request.args.get('id')
    mod_name = request.args.get('name')
    mod_mem = request.args.get('mem')
    mod_end_date = request.args.get('end_date')

    sql = 'update server10 set name="%s", memory=%s, end_date="%s" where id=%s' % (
        mod_name, mod_mem, mod_end_date, mod_id)
    # print sql
    res = 'ok'
    try:
        cur.execute(sql)
    except:
        res = 'error in sql'

    # print res
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=9092)

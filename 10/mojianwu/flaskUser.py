#coding:utf-8
from flask import Flask, render_template, request
import MySQLdb
import json

app = Flask(__name__)

class DB():
    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.conn = None
        self.db_connect()

    def db_connect(self):
        self.conn = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db)
        self.conn.autocommit(True)

    def db_execute(self, sql):
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
        except:
            print 'db reconnect...'
            self.db_connect()
            cur = self.conn.cursor()
            cur.execute(sql)
        return cur 

db = DB('localhost', 'root', 'root', 'mo')

@app.route('/', methods=['GET', 'POST'])
def index():
    print request.method
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        sql = 'select * from t_hosts order by id desc'
        cur = db.db_execute(sql)
        return json.dumps(cur.fetchall())

@app.route('/addHost')
def addHost():
    host = request.args.get('host')
    mem  = request.args.get('mem')
    date = request.args.get('date')
    sql = 'insert into t_hosts(host, memory, endDate) values("%s", %s, "%s")' %(host, mem, date)
    data = 'ok'
    try:
        db.db_execute(sql)
    except:
        data = 'mysql execute error'
        raise data
    finally:
        return data

@app.route('/delHost', methods=['POST'])
def delHost():
    id = request.args.get('id')
    sql = 'delete from t_hosts where id="%s"' %id
    data = 'ok'
    try:
        db.db_execute(sql)
    except:
        data = 'mysql execute error'
        raise data
    finally:
        return data

@app.route('/modHost', methods=['POST'])
def modhost():
    id = request.args.get('id')
    host = request.args.get('host')
    mem  = request.args.get('mem')
    date = request.args.get('date')
    print 'test:', id, host, mem, date
    sql = 'update t_hosts set host="%s", memory=%s, endDate="%s" where id=%s' %(host, mem, date, id)
    print sql
    data = 'ok'
    try:
        db.db_execute(sql)
    except:
        data = 'mysql execute error'
        raise data
    finally:
        return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)
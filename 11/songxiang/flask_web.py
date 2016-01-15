from flask import Flask,render_template,request
import MySQLdb as mysql
import json
# con = mysql.connect(user = 'root', host = 'localhost', passwd = 'ciscoccnp', db = 'songxiang' )
# con.autocommit(True)
# cur = con.cursor()


app = Flask(__name__)

class DB():
	def __init__(self,host,user,passwd,db):
		self.host = host
		self.user = user
		self.passwd = passwd
		self.db = db
		self.conn = None
		self._connect()
	def _connect(self):
		self.conn = mysql.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
		self.conn.autocommit(True)
	def execute(self,sql):
		msg='ok'
		try:
			cur = self.conn.cursor()
			cur.execute(sql)
		except Exception,e:
			print e
			print 'reconnect db'
			self._connect()
			cur = self.conn.cursor()
			try:
				cur.execute(sql)
			except:
				msg='error in sql'

			self.conn.close()
			cur.close()

		return {"cur":cur,"msg":msg}
db = DB('localhost','root','ciscoccnp','songxiang')

@app.route('/',methods=['GET','POST'])
def index():
	print request.method
	if request.method == 'GET':
		return render_template('index.html')
	elif request.method == 'POST':
		sql = 'select * from server10'
		# res = cur.execute(sql)
		cur = db.execute(sql)
		print sql
		print json.dumps(cur['cur'].fetchall())
		return json.dumps(cur['cur'].fetchall())

@app.route('/addhost')
def addhost():
	name = request.args.get('name')
	mem = request.args.get('mem')
	end_date = request.args.get('end_date')
	sql = 'insert into server10 (name,memery,end_date) values ("%s","%s","%s")' % (name,mem,end_date)
	print sql
	# res = 'ok'
	# try:
	# 	cur.execute(sql)
	# except:
	# 	res = 'error in sql '
	# print res
	db.execute(sql)
	return cur['msg']

@app.route('/updatehost',methods=['POST'])
def updatehost():
	id = request.form.get('id')
	name = request.form.get('name')
	date = request.form.get('date')
	sql = 'update server10 set name="%s",memery=%s,end_date="%s" where id=%s'%(name,men,date,id)
	print sql
	db.execute(sql)
	return cur['msg']

@app.route('/delhost',methods=['POST'])
def delhost():
	data_id = request.form.get('id')
	sql = 'delete from server10 where id=%s' % (data_id)
	res = 'ok'
	db.execute(sql)

	return res

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 1234,debug = True)

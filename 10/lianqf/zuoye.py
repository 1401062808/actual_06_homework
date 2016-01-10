from flask import Flask,render_template,request
import MySQLdb as mysql
import json

db =  mysql.connect (host='180.153.191.128',user='reboot',passwd='reboot123',db='lianqf')
# db =  mysql.connect (host='192.168.31.146',user='python',passwd='123456',db='python')
db.autocommit(True)
cur = db.cursor()

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	print request.method
	if request.method=='GET':
		return render_template('index.html')
	elif request.method=='POST':
		sql = 'select * from server10'
		res = cur.execute(sql)
		return json.dumps(cur.fetchall())

@app.route('/addhost')
def addhost():
	name = request.args.get('name')
	mem = request.args.get('mem')
	end_date = request.args.get('end_date')
	sql = "insert into server10(name,memery,end_date) values('%s',%s,'%s')" %(name,mem,end_date)
	print sql
	res ='ok'
	try:
		cur.execute(sql)
	except:
		res = 'error in sql'
	return res

@app.route('/delhost')
def delhost():
	delid = request.args.get('id')
	sql = "delete from server10 where id =" + delid
	res = 'ok'
	try:
		cur.execute(sql)
	except:
		res = 'error in sql'
	return res

@app.route('/edithost')
def edithost():
	editid = request.args.get('id')
	name = request.args.get('name')
	mem = request.args.get('mem')
	end_date = request.args.get('end_date')
	sql = 'update server10 set name="%s" ,memery = %s,end_date="%s" where id=%s' %(name,mem,end_date,editid)
	try:
		cur.execute(sql)
	except:
		res = 'error in sql'
	return res
	
if __name__=='__main__':
	app.run(debug=True,host='0.0.0.0',port=9001)
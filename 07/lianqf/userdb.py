import MySQLdb as mysql
from flask import Flask,request,render_template

app = Flask(__name__)
def get_data():
	db  = mysql.connect(host='192.168.31.222',user='root',passwd='ABCabc123',db='lianqf')
	db.autocommit(True)
	cur = db.cursor()

	sql = 'select * from usertable'
	print cur.execute(sql)

	dict_user = {}
	for data in cur.fetchall():
	    dict_user[data[1]] = data[2]
	return dict_user

def del_data(username):
	
	db  = mysql.connect(host='192.168.31.222',user='root',passwd='ABCabc123',db='lianqf')
	db.autocommit(True)
	cur = db.cursor()

	sql = "delete from usertable where user = '%s'" %username
	print sql

	print cur.execute(sql)

def add_data(user,password):


	db  = mysql.connect(host='192.168.31.222',user='root',passwd='ABCabc123',db='lianqf')
	db.autocommit(True)
	cur = db.cursor()

	sql = "insert into usertable (user,password) values('%s','%s') " %(user,password)
	print sql

	print cur.execute(sql)

@app.route('/')
def index():
	dict_sqluser = get_data()
	return render_template('index.html',userpass=dict_sqluser)

@app.route('/add',methods=['GET','POST'])
def Uadd():
	user = request.args.get('user') 
	password = request.args.get('password') 
	if user=='' or password=='' :
		message = "user or password is null!"
	else:
		print '%s %s' %(user,password)
		add_data(user,password)
		message = "%s is add!" %user
	dict_sqluser = get_data()
	return render_template('index.html',userpass=dict_sqluser,msg=message)

@app.route('/del',methods=['GET','POST'])
def Udel():
	user = request.args.get('user')	 
	del_data(user)
	dict_sqluser = get_data()
	message = "%s is delete!" %user
	return render_template('index.html',userpass=dict_sqluser,msg=message)



if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=9011)
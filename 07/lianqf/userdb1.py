import MySQLdb as mysql
from flask import Flask,request,render_template

app = Flask(__name__)

def update_data(sql):
	
	db  = mysql.connect(host='192.168.31.222',user='root',passwd='ABCabc123',db='lianqf')
	db.autocommit(True)
	cur = db.cursor()

	print cur.execute(sql)
	dict_user = {}
	for data in cur.fetchall():
	    dict_user[data[1]] = data[2]
	return dict_user


@app.route('/')
def index():
	str_sql = 'select * from usertable'
	dict_sqluser = update_data(str_sql)
	return render_template('index.html',userpass=dict_sqluser)

@app.route('/add',methods=['GET','POST'])
def Uadd():
	user = request.args.get('user') 
	password = request.args.get('password') 
	str_sql = 'select * from usertable'
	dict_sqluser = update_data(str_sql)
	if user=='' or password=='' :
		message = "user or password is null!"
	else:
		if user not in dict_sqluser:
			str_sql = "insert into usertable (user,password) values('%s','%s') " %(user,password)
			update_data(str_sql)
			message = "%s is add!" %user
		else:
			message = "%s is exist!" %user
	str_sql = 'select * from usertable'
	dict_sqluser = update_data(str_sql)
	return render_template('index.html',userpass=dict_sqluser,msg=message)

@app.route('/del',methods=['GET','POST'])
def Udel():
	user = request.args.get('user')	 
	str_sql = "delete from usertable where user = '%s'" %user
	dict_sqluser = update_data(str_sql)
	message = "%s is delete!" %user
	str_sql = 'select * from usertable'
	dict_sqluser = update_data(str_sql)
	return render_template('index.html',userpass=dict_sqluser,msg=message)



if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=9011)
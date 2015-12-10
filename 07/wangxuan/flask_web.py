import mysql_db.db as mydb
from flask import Flask,render_template,request,redirect
app = Flask(__name__)

@app.route('/user/')
def user ():
	return render_template('user.html')
@app.route('/')
@app.route('/index')
def index():
	user = {'nickname':'Miguel'}
	return render_template("index.html",user=user)


@app.route('/login')
def login():
	return render_template("login.html")

@app.route('/loginin')
def loginin():
	user = request.args.get('username')
	passwd = request.args.get('password')
#	dict_user = {}
#	with open("userdata","r") as f:
#		for line in f:
#			dict_user[line.split()[0]] = line.split()[1]
#	if user in dict_user and dict_user[user] == passwd:
#		return 'yes you are in!'
#	if user not in dict_user:
#		return 'You have not been signed!'
#	if user in dict_user and dict_user[user] != passwd:
#		return 'wrong password'
	res = mydb.mysql("select * from user where username='%s'"%(user))
	if len(res) == 0:
		str_alert = 'you are not in'
		return render_template("login0.html")
	else:
		if passwd == str(res[0][1]):
			return redirect('/showbooks')	
		else:
			str_alert = 'wrong password!'
			return render_template("login1.html")	

@app.route('/sigin')
def sigin():
	return render_template("signin.html")	

@app.route('/siginin',methods=['GET','POST'])
def siginin():
	user = request.args.get('username')
	passwd = request.args.get('password')
	#check the user if in the userdata.
	with open("userdata","r") as f:
		for line in f:
			if line.split()[0] == user:
				return 'You have been signed in !'
	with open("userdata","a+") as f:
		f.writelines(user + ' ' + passwd + '\n')
	return 'added!'
@app.route('/showuser')
def showuser():
	list_user = []
	dict_user = {}
	with open("userdata","r") as f:
		for line in f:
			user = line.split()[0]
			passwd = line.split()[1]
			dict_user['user'] = user
			dict_user['passwd'] = passwd
			list_user.append(dict_user.copy())
#	list_user = [{'user':'wang','passwd':'123'},{'user':'liu','passwd':'123'},{'user':'sun','passwd':'456'}]
	return render_template("showuser.html",list_user = list_user)

@app.route('/showbooks')
def showbooks():
	'''
	list_books = [{'bookname':'<bookname>','nums':'1','remark':''}]
	'''
	res = mydb.mysql('select * from bookinfo;')
	list_books = []
	dict_books = {}
	for i in res:
		dict_books['bookname'] = i[0]
		dict_books['nums'] = i[1]
		dict_books['remark'] = i[2]
		list_books.append(dict_books.copy())
	return render_template("showbooks.html",list_books = list_books)	
@app.route('/delete')
def delete():
	'''
	The user in data can not be the same!
	'''
	dict_del = request.args.items()
	dict_user = {}
	with open("userdata","a+") as f:
		for line in f:
			dict_user[line.split()[0]] = line.split()[1]
	list_user = zip(*dict_del)[0]	
	for i in list_user:
		del dict_user[i]
	with open("userdata","w") as f:
		for i in dict_user.items():
			tmp = ' '.join(i)+'\n'
			f.writelines(tmp)
	return redirect('/showuser')
@app.route('/deletebooks')
def deletebooks():
	dict_del = request.args.items()
	list_books = []
	list_delbooks = zip(*dict_del)[0]
	with open("bookdata","r") as f:
		for line in f:
			list_books.append(list(line.split()))
	print list_books
	for i in list_delbooks:
		for j in list_books:
			if i == j[0]:
				tmp = int(j[2]) - 1
				j[2] = str(tmp)
	print list_books
	with open("bookdata","w") as f:
		for line in list_books:
			tmp = ' '.join(line) + '\n'
			f.writelines(tmp)
	return redirect('/showbooks')	
if __name__ == '__main__':
	app.run()

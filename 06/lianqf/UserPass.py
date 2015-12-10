from flask import Flask,request,render_template
app = Flask(__name__)

dict_user = {}
with open('data.txt') as f :
	for temp in f.readlines():
		key,dict_user[key] = temp.strip().split(' ')
print (dict_user)


def file_update(dict_userpass):
	with open('data.txt','w') as f:
		for key in dict_userpass:
			f.write(key + ' ' + dict_userpass[key] + '\n')


@app.route('/')
def index():
	return render_template('index.html',userpass=dict_user)



@app.route('/add')
def Uadd():
	user = request.args.get('user')
	password = request.args.get('password')
	print (user + ' ' + password)
	if user in dict_user:
		res = 'already exist'
	else:
		if user == '' and password == '' :
			res = 'user and password can not be empty'
		else:
			dict_user[user] = password
			file_update(dict_user)
			res = 'is add'

	return render_template('index.html', user_dic=dict_user, msg='user: %s password: %s  %s' % (user, password,res) )

@app.route('/del',methods=['GET','POST'])
def Udel():
	user = request.args.get('user')	
	print (user)
	dict_user.pop(user)
	file_update(dict_user)
	res = 'is delete'
	return render_template('index.html', user_dic=dict_user, msg='user: %s  %s' % (user,res))

			
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=9013,debug=True)
from flask import Flask,render_template,request,redirect
#coding:utf8
app=Flask(__name__)

res=''
user_dic={}
#读
with open('user.txt') as f:
	for i in f.readlines():
		user_dic[i.split()[0]] = i.split()[1]

@app.route('/home')
def index():
	return render_template('index.html',user_dic=user_dic)
	
@app.route('/home/action')
def action():
	user = request.args.get('user')
	pwd = request.args.get('pwd')
	if user in user_dic:
		res = 'already exist'
	else:
		if user =='' or pwd == '':
			res = 'can not be empty'
			
		else:
			user_dic[user] = pwd
			res = 'is successfull add'
#添加写入	
	with open('user.txt','w') as ff:
		for j in user_dic:
			ff.write(j+'\t'+user_dic[j]+'\n')
#	return render_template('index.html', user_dic=user_dic, msg='user: %s paswd: %s  %s' % (user, pwd,res) )
	return render_template('index.html', user_dic=user_dic, msg='user: %s paswd: %s  %s' % (user, pwd,res) )

@app.route('/home/del',methods=['GET','POST'])
def udel():
	user = request.args.get('user')
	if user in user_dic:
	        user_dic.pop(user)

	res = 'already delete'
#删除写入
	with open('user.txt','w') as ff:
		for j in user_dic:
			ff.write(j+'\t'+user_dic[j]+'\n')
	return redirect('/home')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=9000,debug=True)

from flask import Flask,request,render_template,redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/acd')
def acd():
	user = request.args.get('user')
	pwd = request.args.get('pwd')
	action = open('user.txt')
	check_user = action.readlines()
	action.close()
	user_dit = {}
	for key in check_user:
		data = key.split(' ')
		user_dit[data[0]] = data[1]
	if user == '' or pwd == '':
		return 'Please submit after input!'
	elif user in user_dit:
		return 'Username exist,please choose other one!'
	else:
		write_to_file =[' '.join([user, pwd + '\n'])]
		user_info_file = open('user.txt','a+')
		user_info_file.writelines(write_to_file)
		user_info_file.close()	
		table_str = '<table border="1"><tr><td>user</td><td>password</td><td>option</td></tr>'
		src_file = open('user.txt')
		lines = src_file.readlines()
		for line in lines:
			tmp = line.replace('\n','').split(' ')
			table_str += '<tr><td>%s</td><td>%s</td><td><a href="%s">delete</a></td></tr>'%(tmp[0],tmp[1],lines.index(line))
		table_str += '</table>'
		read_file = open('templates/index.html')
		read_file_list = read_file.readlines()
		read_file.close()
		if 'border' in read_file_list[-1]:
			read_file_list[-1] = table_str
		else:
			read_file_list.append(table_str)
		des_file = open('templates/index.html','w+')
		des_file.writelines(read_file_list)
		des_file.close()
	return redirect('/')

@app.errorhandler(404)
def page_not_found(error):
	return 'guess'
	
if  __name__ == '__main__':
	app.run(host='0.0.0.0',port=1234,debug=True)

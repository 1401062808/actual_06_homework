# -*- encoding: utf-8 -*-
__author__ = 'yannan'
from flask import Flask,request,render_template
app = Flask(__name__)

dict1={}
f = open('user.txt')

for i in f.readlines():
    dict1[i.replace('\n','').split(' ')[0]]=i.replace('\n','').split(' ')[1]
f.close()

@app.route('/')
def index():
    return render_template("work.html")
@app.route('/login')
def whois():
    global name,passwd,operate
    name = request.args.get('user')
    psswd = request.args.get('pwd')
    operate = request.args.get('operate')
    table_srt = '<table border="1"><tr><td>usr</td><td>pwd</td></tr>'
    for i in dict1:
        table_srt += '<tr><td>%s</td><td>%s</td><td>%s</td></tr>' %(i,dict1[i],operate)
    table_srt += '</table>'
    try:
        if name in dict1 or name == ''or psswd == '':
            table_srt = 'no'
        elif name not in dict1 and name != '' and psswd != '':
            dict1[name] = psswd
    except:
        table_srt='no'
    try:
        if operate:
            operte = dict1.pop(name)
    except:
        table_srt='not define'
    return table_srt
@app.errorhandler(404)
def page_not_found(error):
    return 'Err..'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9527,debug=True)
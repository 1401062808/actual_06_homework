# coding=utf-8
from flask import Flask,request,render_template
app=Flask(__name__)

userfile=open('user.txt')
udic={}

for i in userfile.readlines():
    ilist=i.split(" ")
    udic[ilist[0]]=ilist[1].strip('\n')
userfile.close

@app.route('/',methods=["GET"])
def index():
    return '<a href="/login"> Welcome to new World</a>'


@app.route('/login',methods=["GET"])
def login():
    return render_template("user.html",users=udic)

@app.route('/add',methods=["GET"])
def adduser():
    name=request.args.get('name')
    password=request.args.get('pwd')
    print name,password
    if name in udic or name=="" or password=="":
        return '<a href="/login"> Welcome to new World</a>'
    else:
        ufile=open('user.txt','a')
        ufile.write(name+' '+password+'\n')
        ufile.close
        udic[name]=password 
    return render_template("user.html",users=udic)

@app.route('/del',methods=["GET"])
def deluser():
    user=request.args.get('user')
    del udic[user]
    print "222",udic
    udfile=open('user.txt','w')
    for i in udic:
        print "i",i
        udfile.write(i+' '+udic[i]+'\n')
    udfile.close
    return render_template("user.html",users=udic)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9002,debug=True)

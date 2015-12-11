import MySQLdb as mysql 

db = mysql.connect(user = 'root' , passwd = '', db = 'songxiang1')
db.autocommit(True)
cur = db.cursor()
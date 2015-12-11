# coding:utf-8
__author__ = "seerjk"
# import
import MySQLdb as mysql

db_user = 'reboot'
db_pwd = 'reboot123'
db_name = 'jiangkun'
db_host = '127.0.0.1'
db_port = 3306

def execute(sql_str):
    # connect
    db = mysql.connect(user=db_user, passwd=db_pwd, db=db_name, host=db_host, port=db_port)
    db.autocommit(True)
    cur = db.cursor()

    # sql_str='insert into server values("python", 16)'
    print "result:" + str(cur.execute(sql_str))
    # cur.execute(sql_str)
    # return cur.fetchall()
    result_tuple = cur.fetchall()
    db.close()
    return result_tuple


def select_by_condition(sql_str):
    '''
    select by input sql_str
    internal function

    input: sql_str
    return: result_tuple, number of rows
    '''
    # connect
    db = mysql.connect(user=db_user, passwd=db_pwd, db=db_name, host=db_host, port=db_port)
    # db.autocommit(True)
    cur = db.cursor()

    result_tuple = ()
    influenced_rows = -1

    try:
        influenced_rows = cur.execute(sql_str)
        result_tuple = cur.fetchall()
    except mysql.Error, e:
        # to do: write log
        print "Error %d: %s" % (e.args[0], e.args[1])
    finally:
        db.close()
    return result_tuple, influenced_rows


def select_all():
    '''
    return the whole user table in result_tuple
    '''
    sql_str = "select * from user"
    result_tuple, rows = select_by_condition(sql_str)
    return result_tuple


def select_passwd_by_name(name):
    '''
    input name
    return passwd

    if name not in user table: return -1 int
    elif name exist: return passwd str
    '''
    sql_str = "select * from user where name='%s'" % name
    result_tuple, rows = select_by_condition(sql_str)
    if rows == 1:
        return result_tuple[0][2]
    else:
        return -1


def select_name_by_id(id):
    '''
    input id
    return name

    if id not in user table: return -1 int
    elif id exist: return name str
    '''
    id = int(id)
    sql_str = "select name from user where id=%d" % id
    result_tuple, rows = select_by_condition(sql_str)
    print "*******"
    print rows
    if rows == 1:
        return result_tuple[0][0]
    else:
        return -1


def is_name_exist(name):
    '''
    input name

    if name not exist: return False
    if name exist: return True
    '''
    sql_str = "select * from user where name='%s'" % name
    result_tuple, rows = select_by_condition(sql_str)
    if rows == 1:
        return True
    else:
        return False


def is_name_exist(name):
    '''
    input name

    if name not exist: return False
    if name exist: return True
    '''
    sql_str = "select * from user where name='%s'" % name
    result_tuple, rows = select_by_condition(sql_str)
    if rows == 1:
        return True
    else:
        return False


def change_user(sql_str):
    '''
    insert, update, delete
    internal function

    input: sql_str
    if ok and 1 row affected: return 1
    if ok and 0 row affected: return 0
    if error: return -1
    '''
    # connect
    db = mysql.connect(user=db_user, passwd=db_pwd, db=db_name, host=db_host, port=db_port)
    cur = db.cursor()

    influenced_rows = -1

    try:
        influenced_rows = cur.execute(sql_str)
        db.commit()
    except mysql.Error, e:
        # to do: write log
        print "Error %d: %s" % (e.args[0], e.args[1])
        # Rollback in case there is any error
        db.rollback()
    finally:
        db.close()
    return influenced_rows


def change_user_passwd(name, old_passwd, new_passwd):
    '''
    change user's passwd

    input name, old_passwd, new_passwd
    if old_passwd != passwd in db: return -1
    if ok: return 1
    '''
    pass


def user_sign_up(name, passwd):
    '''
    sign up

    input name, passwd
    if error: return -1
    '''
    status_tmp = select_passwd_by_name(name)
    if status_tmp == -1:
        # name not in user table -- insert
        sql_str = "insert into user (name, passwd) values ('%s', '%s')" % (name, passwd)
        result_code = change_user(sql_str)
    else:
        # name in user table -- update
        return -1

    if result_code == -1:
        return -1
    else:
        # 1
        return 1


def user_add(name, passwd):
    '''
    user add: sign up or change passwd

    input name, passwd
    if error: return -1
    if insert a new recode: return 1
    if update (change passwd): return 0
    '''
    user_exist = is_name_exist(name)
    if user_exist == False:
        # name not in user table -- insert
        sql_str = "insert into user (name, passwd) values ('%s', '%s')" % (name, passwd)
        result_code = change_user(sql_str)
        oper_code = 1
    else:
        # name in user table -- update
        # return 0
        sql_str = "update user set passwd='%s' where name='%s'" % (passwd, name)
        result_code = change_user(sql_str)
        oper_code = 0

    if result_code == -1:
        return -1
    else:
        return oper_code


def user_delete_by_name(name):
    '''
    delete row
    input: name

    if name exist: do delete and return 1
    if not exist: return -1
    '''
    # user_exist = is_name_exist(name)
    # if user_exist == False:
    #     return -1
    # else:
    #     # exist, do delete
    #     sql_str = "delete from user where name='%s'" % name
    #     result_code = change_user(sql_str)

    # if name not exist, do delete is ok and 0 rows affected
    sql_str = "delete from user where name='%s'" % name
    result_code = change_user(sql_str)
    return result_code


def user_delete_by_id(id):
    '''
    delete row
    input: name

    if name exist: do delete and return 1
    if not exist: return 0
    '''
    # if name not exist, do delete is ok and 0 rows affected
    id = int(id)
    sql_str = "delete from user where id='%d'" % id
    result_code = change_user(sql_str)
    return result_code


def main():
    # sql_str='insert into server values("python", 16)'
    # sql_str="select * from user where name='i'"
    # res_tuple = execute(sql_str)

    # print select_passwd_by_name('admin')
    print "***** testing add"
    print user_add("juju", "12345")
    print user_add("ruru", "134")

    res_tuple = select_all()

    for c in res_tuple:
        print "%s %s %s" % c

    print "***** testing delete"
    print user_delete_by_name("juju")
    print user_delete_by_id(12)

    res_tuple = select_all()

    for c in res_tuple:
        print "%s %s %s" % c

    print select_name_by_id(12)



if __name__ == "__main__":
    main()

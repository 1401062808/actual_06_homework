# coding:utf-8
__author__ = "seerjk"

from flask import Flask, request, render_template, redirect, url_for
import db
import json

app = Flask(__name__)

@app.route('/')
def index():
    res_tuple = db.select_all()
    error_info = request.args.get('error_info')
    # print error_info
    return render_template('index.html', data=res_tuple, error=error_info)


@app.route('/add')
def add():
    name = request.args.get('name')
    passwd = request.args.get('passwd')
    error_info = "%s has added succussfully." % name
    # 1: ok  ;  0: error
    status_code = 1

    # if name == "" or passwd == "": 前端可以做，后端也要做
    # 前后端都要做数据校验
    if name == "" or passwd == "":
        error_info = "name or password is empty."
        status_code = 0
    else:
        result_code = db.user_add(name, passwd)
        if result_code == -1:
            error_info = "db error!"
            status_code = 0
        elif result_code == 0:
            error_info = "changed %s's password." % name
            status_code = 1
        else:
            # 1
            error_info= "%s has been added." % name
            status_code = 1

    res_status_tuple = ("res_status", error_info, status_code)

    # url_for ?error_info=str
    # red_url = url_for('index', error_info=error_info)
    # return redirect(red_url)

    res_tuple = db.select_all()
    res_list = list(res_tuple)
    res_list.insert(0, res_status_tuple)
    res_json = json.dumps(res_list)
    # print "*" * 20
    # print res_json
    # print "*" * 20
    return res_json

@app.route('/delete')
def delete():
    id_num = request.args.get('id_num')
    deleted_name = db.select_name_by_id(id_num)

    # 1: ok  ;  0: error
    status_code = 1
    error_info = "%s has been deleted!" % deleted_name

    result_code = db.user_delete_by_id(id_num)

    if result_code == 0:
        error_info = "id not exist"
        status_code = 0

    res_status_tuple = ("res_status", error_info, status_code)
    # return redirect("/?error_info=%s" % (error_info))
    # red_url = url_for('index', error_info=error_info)
    # return redirect(red_url)

    res_tuple = db.select_all()
    res_list = list(res_tuple)
    res_list.insert(0, res_status_tuple)
    res_json = json.dumps(res_list)
    # print "*" * 20
    # print res_json
    # print "*" * 20
    return res_json


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=9090)

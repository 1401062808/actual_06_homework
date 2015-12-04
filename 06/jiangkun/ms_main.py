# coding:utf-8
from flask import Flask, request, render_template
from user import html_table, add_user, delete_user, oper_result
app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    name = request.args.get('name')
    passwd = request.args.get('passwd')
    add = request.args.get('add')
    oper = request.args.get('oper')

    # print "+++++++++++++++++++++++++++"
    print "name: %s, passwd: %s" % (name, passwd)
    # print "+++++++++++++++++++++++++++"


    operation_result_str = ""
    # status_code = 0

    if add == "submit" and oper == None:
        oper = 'add'
        status_code = add_user(name=name, passwd=passwd)
        operation_result_str = oper_result(oper=oper, status_code=status_code)

    elif add == None and oper == 'del':
        oper = 'del'
        status_code = delete_user(name=name)
        operation_result_str = oper_result(oper=oper, status_code=status_code)

    # print operation_result_str
    # print status_code
    
    result = '''
        <form action="/" method="get">
            name:
            <input type="text" name="name">
            password:
            <input type="password" name="passwd">
            <input type="submit" name="add" value="submit">
        </form>
    '''
    if operation_result_str != 1:
        operation_result_str = '<h2>%s</h2>' % operation_result_str
        result += operation_result_str

    user_html_table = html_table()
    result += user_html_table

    return result



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9003, debug=True)
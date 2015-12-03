# coding:utf-8

file_name = 'user.txt'

def read_user_file():
    '''
    read file 'user.txt'
    internal function

    if error: return -1
    if ok: return user_dict
    '''
    try:
        with open(file_name) as f:
            lines = f.readlines()
    except Exception, e:
        return -1

    user_dict = {}

    for line in lines:
        line = line.strip().split(' ')
        user_dict[line[0]] = line[1]

    return user_dict


def write_to_user_file(user_dict):
    '''
    write user_dict into 'user.txt' file
    internal function
    
    if ok: return 1
    if error: return -1
    '''
    # print user_dict
    try:
        with open(file_name, 'w') as f:
            user_list = []
            result_str = ""
            for name, passwd in user_dict.items():
                # error:  empty
                # user_list.append("%s %s\n") % (name, passwd)
                user_item = "%s %s\n" % (name, passwd)
                user_list.append(user_item)
                # result_str += "%s %s\n" % (name, passwd)

            f.writelines(user_list)
            # f.write(result_str)

    except Exception, e:
        return -1

    return 1


def add_user(name, passwd):
    '''
    add user and password into 'user.txt' file
    
    if file write error: return -1
    if name or password == None: return -2
    if name was already in 'user.txt': return -3
    if success: return 1
    '''
    # print "passwd (%s)" % passwd
    # if name == None or passwd == None:
    # 无法判断出name 或者 passwd为空的情况
    # /?name=&passwd=  穿回去的 是 空字符串 "" 而不是 None

    if len(name) == 0 or len(passwd) == 0:
        return -2

    user_dict = read_user_file()

    if name in user_dict:
        return -3
    
    user_dict[name] = passwd

    status = write_to_user_file(user_dict)

    if status == -1:
        return -1
    else:
        return 1


def delete_user(name):
    '''
    delete user by name
    name in user.txt file is unique

    if file write error: return -1
    if name == None: return -2
    if name is not in 'user.txt': return -3
    if success: return 1
    '''
    # if name == None:
    if len(name) == 0:
        return -2

    user_dict = read_user_file()

    if name in user_dict:
        user_dict.pop(name)
    else:
        # name not in user_dict
        return -3

    status = write_to_user_file(user_dict)

    if status == -1:
        return -1
    else:
        return 1


def html_table():
    '''
    return a html table

    if user.txt file error: return -1
    if ok: return result_str
    '''
    user_dict = read_user_file()
    if user_dict == -1:
        # "user.txt file error."
        return -1

    result_str = '''
        <table border="1">
        <thead>
            <tr>
                <th>user</th>
                <th>passord</th>
                <th>operate</th>
            </tr>
        </thead>
        <tbody>
    '''

    for name, pwd in user_dict.items():
        result_str += '''
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td><a href="/?name=%s&oper=del">delete</a></td>
        </tr>
        ''' % (name, pwd, name)

    result_str += '''
                </tbody>
        </table>
    '''
    
    return result_str


def oper_result(status_code, oper):
    '''
    return operation result_dict

    if success: return 1
    '''
    result_dict = {
        "add":{
            -1: "file write error",
            -2: "name or password is empty",
            -3: "name was already in user.txt",
            1: 1
        },
        "del":{
            -1: "file write error",
            -2: "name is empty",
            -3: "name is not in user.txt",
            1: 1
        }
    }

    return result_dict[oper][status_code]


if __name__ == "__main__":
    # test write_to_user_file
    tmp_user_dict = read_user_file()
    tmp_user_dict["juju"] = "1234"
    # print tmp_user_dict
    write_to_user_file(tmp_user_dict)
    print read_user_file()
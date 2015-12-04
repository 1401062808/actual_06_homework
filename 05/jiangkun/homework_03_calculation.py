# coding:utf-8
# 实现加减乘除功能的函数
# - 级别1 不支持优先级
# - 级别2 支持优先级，但是没有括号
# - def operate(str):
# - operate('1+2+3-5') == 1

def analysis_expression(exp_str):
    '''
    translate a string of expression to a list 

    if error in expression: return -1
    else: return exp_list (numbers, operators)
    '''
    # exp_str = ''
    if len(exp_str) == 0:
        return -1
    
    # delete blank in exp_str
    tmp_list = exp_str.split(' ')
    exp_str = ''.join(tmp_list)

    exp_list = []
    operators_list = ['+', '-', '*', '/']
    tmp_num_str = ""

    for i in xrange(len(exp_str)):
        # print i
        if not (exp_str[i] in operators_list or exp_str[i] == '.' or exp_str[i].isdigit()):
            # 表达式中有非数字和操作符 .
            return -1

        if i == 0 and exp_str[0] == '-':
            # -5+1
            tmp_num_str += '-'
        elif exp_str[i] == '-' and exp_str[i-1] in operators_list:
            # 1+-5
            tmp_num_str = '-'
        elif exp_str[i] in ['+', '*', '/'] and exp_str[i-1] in operators_list:
            # 1++5*+5 
            return -1
        else:
            if exp_str[i].isdigit() or exp_str[i] == '.':
                tmp_num_str += exp_str[i]
            elif exp_str[i] in operators_list:
                # 当前是操作符
                tmp_num = float(tmp_num_str)
                exp_list.append(tmp_num)
                exp_list.append(exp_str[i])
                tmp_num_str = ""
            
            if i == len(exp_str) - 1:
                # 遍历到最后一个
                if exp_str[i].isdigit():
                    # 最后一个是数字
                    tmp_num = float(tmp_num_str)
                    exp_list.append(tmp_num)
                    tmp_num_str = ""
                else:
                    # 最后一个不是数字结尾 1++5+
                    return -1

    return exp_list


def calculation1(exp_str):
    '''
    calculate a string of expression
    
    input a string of numbers and operator
    return result

    Support: + - * /
    Not Support priority
    '''
    exp_list = analysis_expression(exp_str)
    if exp_list == -1:
        return

    # operator switch
    operator_dict = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }

    # 方法1:
    # result = exp_list[0]

    # 除去第一个，exp_list 后面每两个可作为一次运算
    # for i in range(len(exp_list))[1::2]:
    #     case exp_list[i]
    #     pass

    # 方法2：stack，遇到operators 则出栈 exp_list.pop()
    result = exp_list.pop(0)
    while exp_list != []:
        operator = exp_list.pop(0)
        # if tmp in operator_dict:
        tmp_num = exp_list.pop(0)
        if operator == '/' and tmp_num == 0:
            # 除数为0的情况
            return
        result = operator_dict[operator](result, tmp_num)
    
    return result


def calculation2(exp_str):
    '''
    calculate a string of expression
    
    input a string of numbers and operator
    return result

    Support + - * /
    Support priority

    with stack
    '''
    exp_list = analysis_expression(exp_str)
    if exp_list == -1:
        return

    # operator switch
    operator_dict = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }

    # 方法：stack，遇到operators 则出栈 exp_list.pop()
    # + - 入栈 stack_list.append()
    # * / 出栈 stack_list.pop()
    # L.insert(index, object) -- insert object before index
    # L.pop([index]) -> item -- remove and return item at index (default last).
    operator_level1 = ['+', '-']
    operator_level2 = ['*', '/']

    # 先进行 * / 运算，最后保证stack_list中只剩余 + - 运算
    stack_list = []
    stack_list.append(exp_list.pop(0))
    while exp_list != []:
        operator = exp_list.pop(0)
        # if operator in operator_dict:
        tmp_num = exp_list.pop(0)
        if operator == '/' and tmp_num == 0:
            # 除数为0的情况
            return

        if operator in operator_level1:
            stack_list.append(operator)
            stack_list.append(tmp_num)
        elif operator in operator_level2:
            pop_num = stack_list.pop()
            result = operator_dict[operator](pop_num, tmp_num)
            stack_list.append(result)
    
    # * / 运算结束，保证stack_list中都是 + - 运算
    result = stack_list.pop(0)
    while stack_list != []:
        operator = stack_list.pop(0)
        # if tmp in operator_dict:
        tmp_num = stack_list.pop(0)
        result = operator_dict[operator](result, tmp_num)
    
    return result


if __name__ == '__main__':
    # main process
    print "Main:"
    # print analysis_expression('1 2 a  a  b  ')
    # print analysis_expression('1+2+-5.6')
    # print analysis_expression('-1  +2+-5.6')
    # print analysis_expression('1+5*+*5')
    print analysis_expression('1+2+5.6--5.0')
    print calculation1('1+2+5.6--5.0')
    print calculation1('-5.0')
    print calculation1('1+2*3')
    print calculation2('1+2*3')
    print calculation2('1*5+2*3*3+5/-6/7')
    print calculation1('')
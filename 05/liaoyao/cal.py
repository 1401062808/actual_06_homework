#!/usr/bin/env python

def op_str(input_str):
	op_list = []
	num_str = ''
	for i in input_str:
		if i == '+' or i == '-' or i == '*' or i == '/':
			op_list.append(i)
			num_str = num_str + ' '
		else:
			num_str = num_str + i
	tmp_list = [op_list,num_str]
	return tmp_list

def op(actions):
	op_action = actions[0]
	tmp_str = actions[1]
	num_list = tmp_str.split()
	for i in op_action:
		if i == '+':
			tmp_sum = int(num_list[0]) + int(num_list[1])
			num_list[:2] = [tmp_sum]
		elif i == '-':
			tmp_sum = int(num_list[0]) - int(num_list[1])
                        num_list[:2] = [tmp_sum]
		elif i == '*':
			tmp_sum = int(num_list[0]) * int(num_list[1])
                        num_list[:2] = [tmp_sum]
		elif i == '/':
			if num_list[1] == '0':
				print 'Error'
			else:
				tmp_sum = (int(num_list[0]) + 0.0) / int(num_list[1])
                        	num_list[:2] = [tmp_sum]
	return num_list

expression = raw_input('Please input the expression: ')
if (expression.strip()).startswith('-'):
	str = (expression.strip()).replace('-','',1)
	tmp_list = op_str(str)
	tmp_list[1] = '-' + tmp_list[1]
	#print tmp_list
	result = op(tmp_list)
	print result[0]
else:
	tmp_list = op_str(expression.strip())
	result = op(tmp_list)
	print result[0]

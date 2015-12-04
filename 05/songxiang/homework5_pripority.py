#  -*- coding:utf-8 -*-
def caculate(number1,symbol,number2):
	if symbol == '+':
		return float(number1) + float(number2)
	elif symbol == '-':
		return float(number1) - float(number2)
	elif symbol == '*':
		return float(number1) * float(number2)
	elif symbol == '/' and number2 != 0:
		return float(number1) / float(number2)
def opearte(string):
	number_list = []
	symbols = ['-','+','*','/']
	numbers = ['0','1','2','3','4','5','6','7','8','9','.']
	number_str = ''
	for i in string:
		if i in symbols and number_str != '':
			number_list.append(number_str)
			number_list.append(i)
			number_str = ''
		elif i in numbers:
			number_str = number_str + i
		else:
			return 'error, 有非法字符 '
	number_list.append(number_str)
	number_list = pre_muli(number_list)
	number_list = pre_plus(number_list)
	return number_list
def pre_muli(number_list):
	count = 0
	if len(number_list) == 1:
		return number_list
	for i in number_list:
		if i == '*' or i =='/':
			number_new=[]
			print count
			tem = caculate(number_list[count-1],number_list[count],number_list[count+1])
			number_new.append(tem)
			number_list[count-1:count+2] = number_new
			number_list = pre_muli(number_list)
			return number_list
		count = count + 1
	return number_list
def pre_plus(number_list):
	count = 0
	if len(number_list) == 1:
		return number_list
	for i in number_list:
		if i == '+' or i == '-':
			number_new =[]
			tem = caculate(number_list[count-1],number_list[count],number_list[count+1])
			number_new.append(tem)
			number_list[count-1:count+2] = number_new
			pre_plus(number_list)
			return number_list
		count = count + 1
	return number_list
if __name__ == '__main__':
	a = '2.4+1'
	result = opearte(a)
	print result









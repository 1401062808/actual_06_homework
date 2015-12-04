# coding=utf-8


calc_dict = {
'+':{'level':1,'fn':lambda x,y:x+y},
'-':{'level':1,'fn':lambda x,y:x-y},
'*':{'level':2,'fn':lambda x,y:x*y},
'/':{'level':2,'fn':lambda x,y:x/y},
}

# 给定操作符和数字算结果
def calc(operate,a,b):
	return calc_dict[operate]['fn'](int(a),int(b))
# 逆波兰表达式解析

# '9+3*3+10/2'
# 变为
# ['9', '3', '3', '*', '+', '10', '2', '/', '+']
# 具体算法：两个栈，数字栈和操作符栈
# 如果是数组，直接入栈=》数字栈
# 如果是操作符，如果此操作符的优先级，比操作符栈顶得元素优先级小，把操作符栈全部入栈到数字栈，并且最新的这个操作符入栈=》操作符
# 如果有优先级比栈顶的优先级高，就入栈=>操作符栈
# 遍历完成，把操作符栈全部入栈到数字栈，搞定

def getPoland(input_str):
	temp = ''
	arr = []
	calc_arr = []
	for s in input_str:
		if s not in calc_dict:
			temp +=s
		else:
			arr.append(temp)
			if len(calc_arr)==0:
				calc_arr.append(s)
			elif calc_dict[s]['level']<calc_dict[calc_arr[-1]]['level']:
				arr.extend(calc_arr[::-1])
				calc_arr = [s]
			else:
				calc_arr.append(s)
			temp = ''
	arr.append(temp)
	arr.extend(calc_arr[::-1])
	return arr

def operate(input_str):

	arr = getPoland(input_str)
	# 计算逆波兰表达式
	# 遍历arr，如果是数字，就入栈，遇见操作符，就从栈内取两个数字，把结果入栈，遍历完，栈内还剩一个数字，bingo
	res = []
	for n in arr:
		if n in calc_dict:
			cal1 = res.pop()
			cal2 = res.pop()
			# print n
			r = calc_dict[n]['fn'](cal2,cal1)
			# print r
			res.append(r)
		else:
			res.append(int(n))
	print res[0]

operate('9+3*3+10/2')

print eval('9+3*3+10/2')
# print int('1+2')
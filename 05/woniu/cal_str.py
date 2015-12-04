calc_dict = {
'+':lambda x,y:x+y,
'-':lambda x,y:x-y,
'*':lambda x,y:x*y,
'/':lambda x,y:x/y
}


def split_str(str):
	s_index = 0
	i = 0
	tmp_list = []
	for x in str:
		if x in calc_dict:
			tmp_list.append(str[s_index:i])
			s_index = i
		i += 1
	tmp_list.append(str[s_index:])
	return tmp_list


def calc(a,b):
	return calc_dict[b[0]](int(a),int(b[1:]))


def operate(input_str):
	l = split_str(input_str)
	init_value = l[0]
	for x in range(1,len(l)):
		init_value = calc(init_value,l[x])
	return init_value

print operate('10+2*3-6')

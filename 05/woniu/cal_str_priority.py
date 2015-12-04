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

calc_str = '10+2*3-6'
l = split_str(calc_str)

am_list = []
while True:
	num = l.pop(0)
	if num[0]=='*' or num[0]=='/':
		prev = am_list.pop()
		am_list.append(prev[0]+str(calc(prev[1:],num)))
	else:
		am_list.append(num)
	if len(l)==0:
		break

init_value = am_list[0]

for x in range(1,len(am_list)):
	init_value = calc(init_value,am_list[x])
print init_value



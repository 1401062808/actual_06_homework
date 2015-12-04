cal_dict = {
	'+':lambda x,y: x+y,
	'-':lambda x,y: x-y,
	'*':lambda x,y: x*y,
	'/':lambda x,y: x/y,
}

def cal_fn(opearte,x,y):
	x = float(x)
	y = float(y)
	return cal_dict[opearte](x,y)

def swith(express_input):
	swith_list = []
	num = ''
	for key in express_input:
		if key not in cal_dict:
			num += key
		else:
			swith_list.extend([int(num),key])
			num = ''
	swith_list.append(int(num))
	return swith_list
data = '1+2+3'
new_list = swith(data)
result = new_list[0]

for key in range(1,len(new_list),2):
	temp = new_list[key]
	result = cal_fn(temp,result,new_list[key+1])
print result
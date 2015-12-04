def swith(express_input,operations=['+', '-', '*', '/']):
    swith_list = []
    num = ''
    for key in express_input:
        if key not in operations:
            num += key
            continue
        if key in operations:
            swith_list.extend([int(num),key])
            num = ''
            continue
    swith_list.append(int(num))
    return swith_list

data =raw_input('please input Expression:')
new_list = swith(data)
result = new_list[0]
for key in range(1,len(new_list)):
        if new_list[key] == '+':
            result = result + new_list[key + 1]
        elif new_list[key] == '-':
            result = result - new_list[key + 1]
        elif new_list[key] == '*':
            result = result * new_list[key + 1]
        elif new_list[key] == '/':
            result = result / new_list[key + 1]

print result

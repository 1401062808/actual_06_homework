num_list = [(2,3),(1,4),(5,1)]

print sorted(num_list,key=lambda x:max(x))
print sorted(num_list,key=lambda x: x[0] > x[1] and x[0] or x[1])
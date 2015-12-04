number_list = [(2,3),(1,4),(5,1),(1,6)]
print [sorted(number_list,key = lambda x : max(x))]
print [sorted(number_list,key = lambda x : (x[0]>x[1])*x[0]+(x[0]<x[1])*x[1] )]

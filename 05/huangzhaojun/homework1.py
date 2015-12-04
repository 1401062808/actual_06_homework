a = [(1, 4), (5, 1), (2, 3)]

print sorted(a,key = lambda x:max(x)) #use max()

print sorted(a,key = lambda x:x[1] < x[0] and x[0] or x[1]) #without use max()


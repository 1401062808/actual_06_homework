arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]

newlist = []
for i in arr1:
    if i in arr2 and i not in newlist:
        newlist.append(i)
print newlist
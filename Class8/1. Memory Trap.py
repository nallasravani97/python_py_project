l1 = [1,2,3,4,5,6]
print(l1,id(l1))

l1 = l1 + [7,8,9]
print(l1,id(l1))

l1.extend([10,11,12])
print(l1,id(l1))

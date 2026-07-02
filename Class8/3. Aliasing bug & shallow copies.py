list_a = ["A","B","C"]
list_b = list_a
list_b.append("D")
print(list_a,id(list_a))
print(list_b,id(list_b))

list_c = list_a.copy()
list_c.append("E")
print(list_c)
print(list_a)
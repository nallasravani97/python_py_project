data=[5,4,6,7,9,4,0,2,3,5,9]

new_data = sorted(data)
print("original list", data)
print("new sorted list", new_data)
data.sort(reverse=True)
print("original list after sort():", data)
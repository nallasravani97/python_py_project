#1. The Zip Mapper
years=[1990,1992,2024,2025]
sales=[12000,20000,25000,100000]
total_sales= (dict(zip(years,sales)))
print(total_sales)

#2. the merge Operator (|)
default_config = {"theme":"light", "notification":True}
user_config = {"theme":"dark"}
print(default_config|user_config)

#3. Common keys(&)
dict_a = {"a":1,"b":2}
dict_b = {"b":3,"c":4}
common_keys = dict_a.keys()&dict_b.keys()
print(common_keys)
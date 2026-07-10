student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}
result = student.pop("non_existing_key", "not found")
print("result of pop():", result)

removed_items = student.popitem()
print("removed_items using popitem():", removed_items)
print("updated dict:", student)
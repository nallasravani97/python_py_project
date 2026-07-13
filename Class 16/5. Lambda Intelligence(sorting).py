students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_by_score =sorted(students, key=lambda x: x[1])
print(f"sorted by score: {sorted_by_score}")

sorted_by_name_length=sorted(students, key=lambda x: len(x[0]))
print(f"sorted by name_length: {sorted_by_name_length}")
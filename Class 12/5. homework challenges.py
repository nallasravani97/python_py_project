chars = ['m', 'a', 'a', 'm']

frequency = {}
for char in chars:
    frequency[char] = frequency.get(char, 0) + 1

for char, count in frequency.items():
    print(f"{char}: {count}")

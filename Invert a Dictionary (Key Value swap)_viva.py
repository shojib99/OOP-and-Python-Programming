data = {'a': 1, 'b': 2, 'c': 3}

inverted = {}

for k, v in data.items():
    inverted[v] = k

print(inverted)

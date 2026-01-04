numbers = [1, 2, 3, 2, 4, 5, 1, 6]

duplicates = []
seen = set()

for num in numbers:
    if num in seen:
        duplicates.append(num)
    else:
        seen.add(num)

print("Duplicate elements:", list(set(duplicates)))

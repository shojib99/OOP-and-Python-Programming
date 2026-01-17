nums = [1, 2, 3, 4, 2, 5, 1, 6, 7]

seen = set()
duplicates = set()

for n in nums:
    if n in seen:
        duplicates.add(n)
    else:
        seen.add(n)

print("Duplicate elements:", duplicates)

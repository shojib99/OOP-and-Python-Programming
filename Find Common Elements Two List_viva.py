list1 = [1, 2, 3, 4, 5, 7, 9]
list2 = [4, 5, 6, 7]

common = []

for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print("Common elements:", common)

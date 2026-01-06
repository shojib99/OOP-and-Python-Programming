numbers = [10, 50, 25, 90, 1`]

first = second = float('-inf')

for num in numbers:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("Second largest number is:", second)

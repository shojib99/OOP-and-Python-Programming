numbers = [10, 51, 23, 89, 11]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)

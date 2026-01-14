numbers = [1, 2, 3, 4, 5,7,8]

is_sorted = True

for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("List is sorted")
else:
    print("List is not sorted")

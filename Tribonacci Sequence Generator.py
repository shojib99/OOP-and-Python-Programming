import array as arr

a = 1
b = 3
c = 4
d = int(input("Enter a number: "))

arr = []

if d == 1:
    print(a)
    print(b)

elif d == 3:
    print(a)
    print(b)
    print(c)

else:
    arr.append(a)
    arr.append(b)
    arr.append(c)
    print(arr[0])
    print(arr[1])
    print(arr[2])

    for j in range(3, d):
        arr.append(arr[j - 1] + arr[j - 2] + arr[j - 3])
        print(arr[j])

num = 99

if num <= 1:
    print("Not a Perfect Number")
else:
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i

    if divisor_sum == num:
        print(f"{num} is a Perfect Number")
    else:
        print(f"{num} is not a Perfect Number")

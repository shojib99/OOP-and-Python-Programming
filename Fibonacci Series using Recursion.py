def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

# Example:
num = int(input("Enter number of terms: "))
print("Fibonacci sequence:")
for i in range(num):
    print(Fibonacci(i))

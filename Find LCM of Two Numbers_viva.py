a = 14
b = 20

x, y = a, b

while y != 0:
    x, y = y, x % y

gcd = x
lcm = (a * b)

print("LCM is:", lcm)

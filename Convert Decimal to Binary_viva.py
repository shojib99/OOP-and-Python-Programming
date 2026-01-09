num = 12

binary = ""

if num == 0:
    binary = "0"
else:
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2

print("Binary:", binary)

amount = int(input("Enter the amount: "))

n1000 = amount // 1000
amount %= 1000

n500 = amount // 500
amount %= 500

n200 = amount // 200
amount %= 200

n100 = amount // 100
amount %= 100

n50 = amount // 50
amount %= 50

n20 = amount // 20
amount %= 20

n10 = amount // 10
amount %= 10

n5 = amount // 5
amount %= 5

n2 = amount // 2
amount %= 2


print ("Notes breakdown:")
if n1000:
    print (f"1000 Taka: {n1000} note(s)")
if n500:
    print (f"500 Taka: {n500} note(s)")
if n200:
    print (f"200 Taka: {n200} note(s)")
if n100:
    print (f"100 Taka: {n100} note(s)")
if n50:
    print (f"50 Taka: {n50} note(s)")
if n20:
    print (f"20 Taka: {n20} note(s)")
if n10:
    print (f"10 Taka: {n10} note(s)")
if n5:
    print (f"5 Taka: {n5} note(s)")
if n2:
    print (f"2 Taka: {n2} note(s)")
if amount:
    print (f"Remaining amount: {amount} Taka (No note available)")

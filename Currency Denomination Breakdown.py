amount = int(input("Enter the amount of money: "))

notes_1000 = amount // 1000
if notes_1000 > 0:
    print(f"1000 Taka notes: {notes_1000}")
amount %= 1000

notes_500 = amount // 500
if notes_500 > 0:
    print(f"500 Taka notes: {notes_500}")
amount %= 500

notes_200 = amount // 200
if notes_200 > 0:
    print(f"200 Taka notes: {notes_200}")
amount %= 200

notes_100 = amount // 100
if notes_100 > 0:
    print(f"100 Taka notes: {notes_100}")
amount %= 100

notes_50 = amount // 50
if notes_50 > 0:
    print(f"50 Taka notes: {notes_50}")
amount %= 50

notes_20 = amount // 20
if notes_20 > 0:
    print(f"20 Taka notes: {notes_20}")
amount %= 20

notes_10 = amount // 10
if notes_10 > 0:
    print(f"10 Taka notes: {notes_10}")
amount %= 10

notes_5 = amount // 5
if notes_5 > 0:
    print(f"5 Taka notes: {notes_5}")
amount %= 5

notes_2 = amount // 2
if notes_2 > 0:
    print(f"2 Taka notes: {notes_2}")
amount %= 2

notes_1 = amount // 1
if notes_1 > 0:
    print(f"1 Taka notes: {notes_1}")
amount %= 1

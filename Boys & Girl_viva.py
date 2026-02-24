username = input().strip()

unique = ""

for ch in username:
    if ch not in unique:
        unique += ch

if len(unique) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

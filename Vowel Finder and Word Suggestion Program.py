str=input("Enter the string: ")
str=str.lower()
vowels=[ ]
for i in str:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vowels.append(i)

print("vowels: ")
print(vowels)
print("Number of vowels: ")
print(len(vowels))

list=['a','e','i','o','u']
sugstword=[ ]
for i in list:
    if i in vowels:
        sugstword.append(i)

print("Suggested words: ")
for i in sugstword:
    if i=='a':
        print("a = apple")
    if i == 'e':
        print("e = ear")
    if i=='i':
        print("i = ink")
    if i=='o':
        print("o = orange")
    if i=='u':
        print("u = universe")

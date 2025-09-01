user_input = input("Enter the string: ")
user_input = user_input.lower()

vowels = []
for char in user_input:
    if char in ['a', 'e', 'i', 'o', 'u']:
        vowels.append(char)

print("Vowels: ", vowels)
print("Number of vowels: ", len(vowels))

vowel_list = ['a', 'e', 'i', 'o', 'u']
suggested_words = []
for v in vowel_list:
    if v in vowels:
        suggested_words.append(v)

print("Suggested words: ")
for v in suggested_words:
    if v == 'a':
        print("a = apple")
    if v == 'e':
        print("e = ear")
    if v == 'i':
        print("i = ink")
    if v == 'o':
        print("o = orange")
    if v == 'u':
        print("u = universe")

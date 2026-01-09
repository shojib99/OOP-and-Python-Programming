expr = "{[()]}"

stack = []
pairs = {')': '(', '}': '{', ']': '['}

balanced = True

for ch in expr:
    if ch in pairs.values():
        stack.append(ch)
    elif ch in pairs:
        if not stack or stack.pop() != pairs[ch]:
            balanced = False
            break

if balanced and not stack:
    print("Balanced")
else:
    print("Not Balanced")

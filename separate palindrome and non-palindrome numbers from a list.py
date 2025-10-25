list1 = []
list2 = []

def Shojib(lst):
    for S in lst:
        temp = S
        rev = 0
        while S > 0:
            dig = S % 10
            rev = rev * 10 + dig
            S = S // 10
        if temp == rev:
            list1.append(temp)
        else:
            list2.append(temp)
    return list1, list2

l = [12, 131, 535, 151]
m, n = Shojib(l)
print(m, n)

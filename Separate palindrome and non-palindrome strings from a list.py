list1 = []
list2 = []

def sudipto(lst):
    n = len(lst)
    for i in range(n):
        s = lst[i]
        k = s[::-1]
        if s == k:
            list1.append(s)
        else:
            list2.append(s)
    return list1, list2

list = ["17", "131", "535", "151"]
a, b = sudipto(list)
print(a)
print(b)

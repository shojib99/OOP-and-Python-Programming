from re import A
def abc(a):
  if a==0:
    return a
  else:
      return a+abc(a-1)
print(abc(6))

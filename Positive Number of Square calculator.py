while True:
   n=input("please enter a positive number (0 to exit):")
   n=int(n)
   if n<0:
       print("we only allow positive number.please try again:")
       continue
   if n==0:

        break
   print("square of ",n,"is",n*n)

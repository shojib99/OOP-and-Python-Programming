terminate = False
while not terminate:
   operation = input("Please enter add/sub or quit to exit: ")
   if operation == "quit":
       terminate = True
       break
   if operation not in ["add", "sub"]:
       print("Unknown operation!")
       continue
   number1 = input("Please enter a number: ")
   number1 = int(number1)
   number2 = input("Please enter another number: ")
   number2 = int(number2)

   if operation == "add":
       print("Result is", number1 + number2)
       break
   if operation == "sub":
       print("Result is", number1 - number2)
       break

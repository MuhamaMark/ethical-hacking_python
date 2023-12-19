#!/bin/python3

#designing mini calculator

x =float (input("give me a number : "))
o = input("Give me an Operator: ")
y = float (input("give me another number : "))
if o == "+":
    print(x + y)
elif o == "-":
    print(x - y)
elif o == "*":
    print(x * y)
elif o == "/":
    print(x / y)
elif o == "%":
    print(x % y)
elif o == "**":
    print(x ** y)
else:
    print("Unknown Operator!")
    



 
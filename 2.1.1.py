num = float(input("What is the number? \n"))
numbr = float(round(num, 2))

if numbr < 15 and numbr > 5:
    print("The number is in between 15 and 5: True")
else:
    print("The number is in between 15 and 5: False")

if numbr < 13 and numbr > 7:
    print("The number is in between 13 and 7: True")
else:
    print("The number is in between 13 and 7: False")

if numbr < 9.99 and numbr > 9.00:
    print("The number is not 9: False")
else:
    print("The number is not 9: True")
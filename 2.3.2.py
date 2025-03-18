grade = int(input("What is your grade (percentage, no symbol)"))

if grade >= 80 and grade <= 100:
    print("You got an A")
elif grade >= 70 and grade <= 79:
    print("You got a B")
elif grade >= 60 and grade <= 69:
    print("You got a C")
elif grade >= 50 and grade <= 59:
    print("You got a D")
elif grade >= 0 and grade <= 49:
    print("You got an F")
else:
    print("Invalid grade")  
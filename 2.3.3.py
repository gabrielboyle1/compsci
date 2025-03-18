num = int(input("Number? \n"))

if num % 5 and num % 3 == 0:
    print("Divisible by both 3 and 5")
    quit()
if num % 3 == 0:
    print("Divisible by 3")
if num % 5 == 0:
    print("Divisible by 5")
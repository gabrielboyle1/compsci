guess = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
q = "What is your guess for the number? \n"
a = "32"
for i in range(10):
    guess[i] = input (q)
    if guess[i] == a:
        print("Correct!")
        break
    else:
        print("Incorrect")
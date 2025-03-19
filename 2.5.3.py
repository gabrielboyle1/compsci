import asyncio 
import tracemalloc
import random

tracemalloc.start()

guesses = [0] * 10  # Initializes list with 10 zeroes
q = "What is your guess for the number? \n"
a = random.randint(1, 100)  # Random number between 1 and 100
run = 0

async def get_guess():
    """Asks the user for input with a 10-second timeout and ensures it's a number or 'answer'."""
    try:
        guess = await asyncio.to_thread(input, q)  # Run input() in a separate thread
        if guess.lower() == "answer":  # Check before converting to int
            return "answer"
        return int(guess)  # Convert input to an integer
    except ValueError:
        print("Invalid input! Please enter a number.")
        return None  # Return None if the user enters non-numeric input
    except asyncio.TimeoutError:
        return None  # Return None if the user takes too long

async def guess():
    global run  
    while run < 10:
        try:
            user_guess = await asyncio.wait_for(get_guess(), timeout=10)  # 10s limit
            if user_guess is None:
                print(f"Time's up! The number was {a}")
                return
            
            if user_guess == "answer":  # Now it correctly detects "answer"
                print(f"The number is {a}")
                continue  # Let them guess again without losing a turn

            guesses[run] = user_guess  # Store the numeric guess

            if guesses[run] == a:
                print("Correct!")
                return  # Exit if correct
            else:
                print("Incorrect!")

            run += 1  
            print(f"You have {10 - run} tries left.")

        except asyncio.TimeoutError:
            print(f"Time's up! The number was {a}")
            return

    print(f"Game over! No more attempts left. The number was {a}")

async def main():
    await guess()

asyncio.run(main())  # Run the async function
1

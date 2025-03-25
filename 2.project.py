import asyncio 
import random

class formatting:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class question:
    question = ""
    answer = []
    responce = "0"

question1 = question()
question1.question = "What is the symbol for water?"
question1.answer = ["H2O"]
question1.responce = "0"

question2 = question()
question2.question = "What planet is known as the Red Planet?"
question2.answer = ["Mars"]
question2.responce = "0"

question3 = question()
question3.question = "Name a gas that plants absorb from the air for photosynthesis."
question3.answer = ["CO2", "Carbon Dioxide"]
question3.responce = "0"

question4 = question()
question4.question = "True or False: The human body has 206 bones."
question4.answer = ["True"]
question4.responce = "0"

question5 = question()
question5.question = "How many bones are in the adult human body?"
question5.answer = ["206"]
question5.responce = "0"

question6 = question()
question6.question = "How many hours does it take for Earth to complete one rotation?"
question6.answer = [("23", "25")]
question6.responce = "0"

question7 = question()
question7.question = "What is the chemical symbol for carbon?"
question7.answer = ["C"]
question7.responce = "0"

question8 = question()
question8.question = "What is the freezing point of water in Fahrenheit?"
question8.answer = ["32"]
question8.responce = "0"

question9 = question()
question9.question = "How many days is one loop of earth around the sun?"
question9.answer = ["365"]
question9.responce = "0"

question10 = question()
question10.question = "What is the chemical symbol for oxygen?"
question10.answer = ["O"]
question10.responce = "0"

## Calculates two random numbers (randint1 and randint2) and makes a math question
randint = random.randint
randint1 = randint(1, 100)
randint2 = randint(1, 100)
question11 = question()
question11.question = f"What is {randint1} + {randint2}?"
question11.answer = [randint1 + randint2]
question11.responce = "0"
                                              

questions = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11]
totalScore = 0  # Start at 0
correctAnswers = 0  # Counter for correct answers

for i in range(len(questions)):  
    print(questions[i].question)
    responce = input("Answer: ")
    questions[i].responce = responce  # Store response

    # Check answer
    if responce in questions[i].answer:
        print(f"{formatting.OKGREEN}{formatting.BOLD}Correct!{formatting.ENDC}")
        correctAnswers += 1  # Increase correct count
    else:
        correctStrippedAnswer = questions[i].answer[0].strip()
        print(f"{formatting.FAIL}{formatting.BOLD}Incorrect!{formatting.ENDC} The answer was {correctStrippedAnswer}.")

    # Score is based on correct answers so far
    totalScore = (correctAnswers / (i + 1)) * 100  
    totalScoreRounded = round(totalScore, 2)  # Round for display

    print(f"Your score is {totalScoreRounded}%")



import asyncio 
import random
from playsound3 import playsound

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

question2 = question() ## Must have a one word response that will accept all upper case or all lowercase of answer
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
question5.question = "How many bones are in the adult skull ?"
question5.answer = ["22"]
question5.responce = "0"

question6 = question()
question6.question = "How many hours does it take for Earth to complete one rotation?"
question6.answer = ["range:23-25"] ## Must have one question where the answer is within a range (like 5 to 13, so 9 would be correct)
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
randint1 = (randint(1, 100))
randint2 = randint(1, 100)
question11 = question()
question11.question = f"What is {randint1} + {randint2}?"
question11.answer = str([randint1 + randint2]) # type: ignore
question11.responce = "0"

question12 = question()
question12.question = "Name one unit of temperature measurement."
question12.answer = ["Celsius", "Fahrenheit", "Kelvin"]
question12.responce = "0"
                                              

questions = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12]
totalScore = 0  # Start at 0
correctAnswers = 0  # Counter for correct answers

while True:
    print("Welcome to the quiz! You may, at any time, enter Restart to restart the quiz. There are 11 questions. Good luck!")   
    for i in range(len(questions)):  
        print(questions[i].question)
        responce = input("Answer: ")
        questions[i].responce = responce  # Store response
    
        if "range:" in questions[i].answer[0]:  # Check if it's a range-based question
            minVal, maxVal = map(float, questions[i].answer[0].split(":")[1].split("-"))
            if minVal <= float(responce) <= maxVal:
                print(f"{formatting.OKGREEN}{formatting.BOLD}Correct!{formatting.ENDC}")
                playsound("X:\\My Drive\\Grade 9 - Semester 2\\Period 3 - Comp Sci\\Unit 2\\correct.wav")
            correctAnswers += 1
            continue
        elif responce in questions[i].answer:
            print(f"{formatting.OKGREEN}{formatting.BOLD}Correct!{formatting.ENDC}")
            playsound("X:\\My Drive\\Grade 9 - Semester 2\\Period 3 - Comp Sci\\Unit 2\\correct.wav")
            correctAnswers += 1  # Increase correct count
        elif responce == "Restart":
            print("Restarting quiz...")
            break
        elif i == 11:
            if responce[i][:1].lower() == "c":
                print(f"{formatting.FAIL}{formatting.BOLD}Incorrect!{formatting.ENDC} Did you mean Celsius?.")
                playsound("X:\\My Drive\\Grade 9 - Semester 2\\Period 3 - Comp Sci\\Unit 2\\incorrect.wav")
            elif responce[i][1].lower() == "f":
                print(f"{formatting.FAIL}{formatting.BOLD}Incorrect!{formatting.ENDC} Did you mean Fahrenheit?.")
                playsound("X:\\My Drive\\Grade 9 - Semester 2\\Period 3 - Comp Sci\\Unit 2\\incorrect.wav")
            elif responce[i][1].lower() == "k":
                print(f"{formatting.FAIL}{formatting.BOLD}Incorrect!{formatting.ENDC} Did you mean Kelvin?.")
                playsound("X:\\My Drive\\Grade 9 - Semester 2\\Period 3 - Comp Sci\\Unit 2\\incorrect.wav")
            else:
                print(f"{formatting.FAIL}{formatting.BOLD}Incorrect!{formatting.ENDC} The answer was {correctStrippedAnswer}.") #type: ignore
                playsound("X:\\My Drive\\Grade 9 - Semester 2\\Period 3 - Comp Sci\\Unit 2\\incorrect.wav")
        elif i == 12:
            print("You have reached the end of the quiz!")
            print(f"Your score is {totalScoreRounded}%") #type: ignore
            break
        else:
            correctStrippedAnswer = questions[i].answer[0].strip()
            print(f"{formatting.FAIL}{formatting.BOLD}Incorrect!{formatting.ENDC} The answer was {correctStrippedAnswer}.")
            playsound("X:\\My Drive\\Grade 9 - Semester 2\\Period 3 - Comp Sci\\Unit 2\\incorrect.wav")
        # Score is based on correct answers so far
        totalScore = (correctAnswers / (i + 1)) * 100  
        totalScoreRounded = round(totalScore, 2)  # Round for display

        print(f"Your score is {totalScoreRounded}%")





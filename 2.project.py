import asyncio 
from pydub import AudioSegment
from pydub.playback import play
import os 
import tracemalloc
tracemalloc.start()
cwd = os.getcwd()

questions = [
    "What is the symbol for water?",
    "What planet is known as the Red Planet?",
    "Name a gas that plants absorb from the air for photosynthesis.",
    "True or False: The human body has 206 bones.",
    "How many bones are in the adult human body?",
    "How many hours does it take for Earth to complete one rotation?",
    "What is the chemical symbol for carbon?",
    "What is the freezing point of water in Fahrenheit?",
    "How many days is one loop of earth around the sun?",
    "What is the chemical symbol for oxygen?"
]
answers = [
    "H2O",        # One-word response (case-insensitive)
    "Mars",       # Multiple-choice question answer
    ["CO2", "Carbon Dioxide"],  # Multiple correct answers
    "True",       # True or False question
    206,          # Number answer
    (23, 25),      # Answer within a range (23-25)
    "C",          # One-letter response (case-insensitive)
    32,           # Number answer
    365,          # Number answer
    "O"
]




responces = ["0"] * len(questions)


correctSound = AudioSegment.from_file(f"{cwd}/correct.wav", format="wav")
incorrectSound = AudioSegment.from_file(f"{cwd}/incorrect.wav", format="wav")

async def correct():
        print("Correct!")
        play(correctSound)

async def incorrect():
        print("Incorrect.")
        play(incorrectSound)

for i, name in enumerate(questions):
    print(questions[i])
    responces[i] = input("Answer: ")
    if responces[i] == answers[i]:
        correct() # type: ignore
    else:
        incorrect() # type: ignore

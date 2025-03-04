import random

EASY = 10
HARD = 5
attempt = 0

def set_difficulty(difficulty):
    if difficulty == "easy":
        return EASY
    elif difficulty == "hard":
        return HARD

def check_answer(guess,number):
    if guess == number:
        print("You got it!")
        return 0
    elif guess < number:
        print("Too low.")
        return -1
    elif guess > number:
        print("Too high.")
        return -1

def game():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    num = random.randint(1, 100)
    print(f"number: {num}")
    attempt = set_difficulty(level)
    guess = -1
    while attempt > 0 and guess != num:
        print("You have " + str(attempt) + " attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempt += check_answer(guess,num)
    if attempt == 0:
        print("You've run out of guesses. Refresh the page to run again.")



game()
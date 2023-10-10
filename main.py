from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
PRO_LEVEL = 2


# TODO: Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"Yay!!!You got it! The answer was {answer}.")


# TODO: Make function to set difficulty. With 3 levels of difficulties so user can pick.
def set_difficulty():
    level = input("We have 3 levels for you to pick from.\n"
                  "1. Easy peasy, when you have 10 guesses.\n"
                  "2. Something that can be 'A real struggle', when you only have 5 guesses.\n"
                  "3. 'I am a GURU', when you only have 2 guesses.\n"
                  "Please pick your level: ")
    if level == "1":
        return EASY_LEVEL_TURNS
    elif level == "2":
        return HARD_LEVEL_TURNS
    elif level == "3":
        return PRO_LEVEL
    else:
        print("You need to pick from 3 levels above.")


def game():
    print(logo)
    # TODO: Choosing a random number between 1 and 100

    print("I am thinking the number between 1 and 100.")
    answer = randint(1, 100)
    print(f"The correct answer is {answer}")

    turns = set_difficulty()

    # TODO: Repeat the functionalities if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let guess  a number:
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run put of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again!")


while True:
    play = input("Ready for the new challenge with the Number Guessing Game! Please type 'yes' to play and 'no' to "
                 "exit the game. ").lower()
    if play == "yes":
        game()
    elif play == "no":
        print("Let's level up yourself next time!!!!")
        break
    else:
        print("Invalid input.")

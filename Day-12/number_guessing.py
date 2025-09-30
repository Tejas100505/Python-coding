import random

logo = """
     __                 _                   ___                     _             
  /\ \ \_   _ _ __ ___ | |__   ___ _ __    / _ \_   _  ___  ___ ___(_)_ __   __ _ 
 /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|  / /_\/ | | |/ _ \/ __/ __| | '_ \ / _` |
/ /\  /| |_| | | | | | | |_) |  __/ |    / /_\\| |_| |  __/\__ \__ \ | | | | (_| |
\_\ \/  \__,_|_| |_| |_|_.__/ \___|_|    \____/ \__,_|\___||___/___/_|_| |_|\__, |
                                                                            |___/ 
"""

print(logo)


def number_choosed():
    numbers = list(range(1, 101))
    return random.choice(numbers)


def play_game(attempts):
    number = number_choosed()

    while attempts > 0:
        guess_number = int(input("Make a guess: "))
        
        if guess_number > number:
            print("Too high.")
        elif guess_number < number:
            print("Too low.")
        else:
            print(f"You got it! The answer was {number}.")
            return

        attempts -= 1
        if attempts > 0:
            print("Guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")
        else:
            print("You've run out of guesses, you lose.")


print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    play_game(10)
else:
    play_game(5)

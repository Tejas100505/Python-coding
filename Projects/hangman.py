import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

lives = 6
display = [0] * len(chosen_word)
for i in range (0, len(display)):
    display[i] = "_"

while ("_" in display):
    guess = input("Guess the letter: ")
    index = 0
    for i in range(0, len(chosen_word)): 
        if chosen_word[i] == guess:
            display[i] = guess
    print(display)

    if guess not in display:
        lives -= 1
        if lives == 0:
            print("You lose")

    if "_" not in display:
        print("You won")

    






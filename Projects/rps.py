import random

number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choice = random.randint(0, 2)

choices = ["Rock", "Paper", "Scissors"]

if number < 0 or number > 2:
    print("Invalid choice! Please choose 0, 1, or 2.")
else:
    print(f"You chose {choices[number]}")
    print(f"Computer chose {choices[computer_choice]}")

    if number == computer_choice:
        print("It's a draw!")
    elif (number == 0 and computer_choice == 2) or (number == 1 and computer_choice == 0) or (number == 2 and computer_choice == 1):
        print("You won!")
    else:
        print("You lose!")

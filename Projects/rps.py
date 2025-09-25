import random 

number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computers_choice = random.randint(0,2)

print(f"Your chose {number}")
print(f"Computer chose {computers_choice}")

if(number == 0 and computers_choice == 2) or (number == 1 and computers_choice == 0) or (number == 2 and computers_choice == 1):
    print("You won!")
elif(computers_choice == 0 and number == 2) or (computers_choice == 1 and number == 0) or (computers_choice == 2 and number == 1):
    print("You lose")
else:
    print("It's a draw")
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
direction = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")

if direction == "left":
    action1 = input("You came to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across\n")
    if action1 == "wait":
        action2 = input("There are three doors ahead choose one of them. Type 'red', 'yellow' or 'blue'\n")
        if action2 == "red":
            print("Game Over")
        elif action2 == "yellow":
            print("You won!")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")
            




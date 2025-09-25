logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

import os

def clear_screen():
    os.system('cls')

data = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

print("Welcome to the secret auction program")

more_bidder = "yes"
while(more_bidder == "yes"):
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    data[name] = bid
    more_bidder = input("Are there any other bidders? Type 'yes' or 'no'.")
    if more_bidder == "yes":
        clear_screen()
    else:
        find_highest_bidder(data)





print("Welcome to Tip calculator")
bill = float(input("What wass the total bill?\n"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?\n"))
people = int(input("How may people to split the bill\n"))

bill_with_tip = bill +  ((tip * bill) / 100)
bill_per_person = bill_with_tip / people

print(f"Each person should pay: ${bill_per_person:.2f}")
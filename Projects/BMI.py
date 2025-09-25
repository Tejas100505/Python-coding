print("Welcome to BMI calculator")
weight = float(input("What is your weight?\n"))
height = float(input("What is your height in meters?\n"))

bmi = round(weight / (height ** 2), 2)
print(f"Your BMI is: {bmi}")





#Add
def add(n1, n2):
    return n1+n2

#Subtract
def subtract(n1, n2):
    return n1-n2

#Multiply
def multiply(n1, n2):
    return n1*n2

#Division
def division(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}


def calculator():
    num1 = float(input("What's the first number?: "))

    for key in operations:
        print(key)
    should_continue = True

    while should_continue:
        opr = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        calculation_function = operations[opr]
        answer = calculation_function(num1, num2)

        print(f"{num1} {opr} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to statt a new operation.: ") == "y":
            num1 = answer
        else: 
            should_continue = False
            calculator()

calculator()
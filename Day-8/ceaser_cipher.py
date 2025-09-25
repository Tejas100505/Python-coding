alphabets = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

def caesar(start_text, shift_amount, direction):
    end_text = ""
    if direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabets: # in keyword is used here 
            position = alphabets.index(char)
            new_position = position + shift_amount
            end_text += alphabets[new_position]
        else: 
            end_text += char
    
    print(f"The {task}d text is {end_text}")

should_continue = True
while should_continue:
    task = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n").lower()
    shift_number = int(input("Type the shift number:\n"))

    shift_number = shift_number % 26 #bcoz if we use %26 it will reduce the shift_number and exactly same results we will get as without %26

    caesar(start_text=message, shift_amount=shift_number, direction=task)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")


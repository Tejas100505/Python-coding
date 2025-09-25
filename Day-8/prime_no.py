#Write your code below this line 👇
def prime_checker(number):
    isPrime = True

    for i in range(2, number - 1):
        if(number % i == 0):
            isPrime = False
    
    if(isPrime == True):
        print("The number is a Prime number")
    else:
        print("The number is not a Prime number")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)




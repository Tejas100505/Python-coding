programming_dictionary = {
    "Tejas": "23101A0037",
    "Ritesh": "23101A0024",
    "Yashodhan": "23101A0051"
}

#Retrieving an item from dictionary

print(programming_dictionary["Tejas"])

#Adding new items to dictionary 
programming_dictionary["Kaivalya"] = "23101A0067"
print(programming_dictionary)

#empty dictionary
empty_dictionary = {}

#Wiping ad existing dictionary
programming_dictionary = {}
print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Tejas"] = "23101A0036"
print(programming_dictionary)

#loop through a dictionary 
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key]) #to get the value 


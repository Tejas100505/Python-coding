
#Local Scope

def drink_potion():
    potion_strength = 2 # Lccal variable
    print(potion_strength)

drink_potion()

#Global Scope

player_health = 10 # Global variable

def drink_potion():
    potion_stength = 2
    print(player_health)

drink_potion()

#There is no block scope 

game_level = 3
enemies = ["skeleton", "zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0] # This variable has no scope 

print(new_enemy)


#Modifying a global variable 

enemies = 1

def increase_enemies():
    global enemies
    enemies = 2
    print(f"enemies inside funtion: {enemies}")

increase_enemies()
print(f"enemies outside funtion: {enemies}")

 



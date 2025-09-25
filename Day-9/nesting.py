#Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#Nesting a list into dictionary 

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}


#Nesting a dictionary into dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"]},
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"]
}

#Nesting a dicitonary in a list 

travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg"], 
        "total_visits": 5
    }
]





travel_log = [
    {
        "country": "France", 
        "total_visits": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany", 
        "total_visits": 5,
        "cities_visited": ["Berlin", "Hamburg"]
    }
]

def add_new_country(new_country, no_of_times_visited, city_visited):
    data = {
        "country": new_country, 
        "total visits": no_of_times_visited, 
        "cities_visited": city_visited
    }
    travel_log.append(data)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
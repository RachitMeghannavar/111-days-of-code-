# Nested list: a list inside another list
travel_log_list = [
    ["Berlin", "Stuttgart"],
    "Paris",
    ["Tokyo", "Kyoto"],
    ["Barcelona", "Madrid"],
]

# Accessing the values of nested lists
print(travel_log_list)
print(travel_log_list[0][0])
print(travel_log_list[3][1])

for cities in travel_log_list:
    print(cities)

# Nested dictionaries
travel_log_dict = {
    "france": ["Paris"],
    "spain": ["Barcelona", "Madrid"],
    "japan": ["Tokyo", "Kyoto"]
}

print(travel_log_dict["france"][0])
# get the Madrid city from the dictionary
print(travel_log_dict["spain"][1])

travel_log = {
    "France": {
      "cities_visited": ["Paris", "Lille", "Dijon"],
      "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5

    },
}

# print Lille from the dictionary
print(travel_log["France"]["cities_visited"][1])
# print how many times the user has visited germany
print(travel_log["Germany"]["total_visits"])
# and print Hamburg from the dictionary
print(travel_log["Germany"]["cities_visited"][1])
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}
fruits = ["apple", "banana", "cherry", "orange", "mango"]
print(fruits[0])
print(programming_dictionary["Bug"])

# How to create a dictionary

player_1= {
    "name": "Rachit",
    "age": 18,
    "isPlaying": False,
    "isCoding": True,
}

# Accessing the values of dictionary
print(player_1["isCoding"])
print(player_1["isPlaying"])

# Adding a new value to the dictionary
player_1["username"] = "Rachit"
print(player_1)

# Modifying the values of a dictionary
player_1["isPlaying"] = True
print(player_1["isPlaying"])
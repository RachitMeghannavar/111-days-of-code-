# Functions with input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

# Positional arguments
greet_with("Tejas","Examba")
greet_with("Rachit","Chikodi")
greet_with("Chikodi","Rachit")


# Keyword arguments
greet_with(location="Chikodi",name="Rachit")
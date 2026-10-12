# name = input("What is your name? :")
# def greet():
#   print(f"Hello, {name}")
#    print("How are you?")
#   print("how's your day going?")

#greet()
#greet()

def greet(username):
    print(f"Hello, {username}")  #argument
    print("How are you?")
    print("how's your day going?")

greet("Tejas")       # Tejas = parameter
greet("Rachit")      # Rachit = parameter

name = input("What is your name?")
greet(name)
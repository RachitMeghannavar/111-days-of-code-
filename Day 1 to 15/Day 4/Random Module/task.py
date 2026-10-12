# Random is a module so we need to import it
import random

# To get a random number between the given range
random_number=random.randrange(1,100)
print(random_number)

# To get a random integer between the given range
random_int=random.randint(1,50)
print(random_int)

# To get a random float between 0 and 1
random_float=random.random()
print(random_float)

# To get a random float between the give range
random_float2=random.uniform(0,100)
print(random_float2)

# Use random module and create a simple program to get heads or tails
random_num=random.randint(0,2)
if random_num==1:
    print("Heads")
else :
    print("Tails")
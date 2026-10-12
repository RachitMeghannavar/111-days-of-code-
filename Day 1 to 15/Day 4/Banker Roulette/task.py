friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
import random
pay = random.choice(friends)
print(f"The person to pay is: {pay}")

#without using random.choice()
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_number = random.randint(0, len(friends)-1)
print(f"The person to pay is: {friends[random_number]}")
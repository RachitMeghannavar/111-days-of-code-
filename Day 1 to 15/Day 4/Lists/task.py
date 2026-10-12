fruit1 = "Apple"
fruit2 = "Mango"
fruit3 = "Kiwi"

print(fruit1)
print(fruit2)
print(fruit3)

#Lists
fruits = ["Apple", "Mango", "Banana"]
print(fruits)

# accessing the list items
print(fruits[1])
print(fruits[-1])
print(fruits[0:2])

# editing/modifying the list items
# Changing the mango to kiwi
fruits[1] = "Kiwi"
print(fruits)

# List methods
# Adding an item to the list
# we use '.append()' to add an element to the end of the list
fruits.append("Cheery")
fruits.append("Dragon fruit")
print(fruits)

# Deleting the last element from the list
# we use '.pop()' to delete the last element from the list
# we use '.pop(index)' the mentioned index will be deleted
fruits.pop()
fruits.pop(0)
print(fruits)
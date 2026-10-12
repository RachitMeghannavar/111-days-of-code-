length=len("Hello, world")
print(length)

sentence = "Quick brown fox jumps over the lazy dog"
print(len(sentence))

#print(len(10)) this well give you an error because it's a number

#Data Types
#The types of data we can use in Python

#STRINGS- Anyting that has a character or a symbol in it eg: 'Rachit', "Chikodi" ,'PAris', ey$#%^"

name="Rachit Meghannavar"
print(name)

#Accesing letters from a string
print(name[15])
print(name[-3])

#Challenge 1: get the last letter from the name
print(name[-1])

#Getting the first 3 characters
print(name[0:3])
print(name[7:10])

#Challenge 2: get the full name
print(name[0:-1])
print(name[0:])

#Jump over letters using indexes
print(name[::2])
print(name[0:7:3])

#Concatenating strings(and integers)
name="Rachit"
print("Hello"+ " "+ name)

age="18" #if it is an integer it will give you an error
print("Hello, "+ name + " "+ age)

#INTEGERS- whole numbers is Python eg: 18,100,-10,-20000,20000
age= 18
height= 186
weight= 75


print(10+10)
print("10" + "10")

#FLOATS - numbers with decimal point
#you can perform all math operations for integers(+,-,*,/)
pi = 3.14159
width = 1.65

print(10.2 +  10.5)
print(10.2 - 10.5)
print(10.2 * 10.5)
print(10.2 / 10.5)

# BOOLEANS - anything that could be true/false
#weight =45.5 #this in  not an integer
#writting big numbers
#55,00,000->55_00_000
print(55_00_000)
print(5500000)

#you can perform all math operations for integers(+,-,*,/)
print(10+10)
print(10-10)
print(10*10)
print(10/10)
car_drive = age > 17
print(car_drive)

#TESTING THE DATA TYPE
car = "Tesla Model y"
model = 2024
displaySize = 15.4
carSelfDrive = True

print(type(car))
print(type(model))
print(type(displaySize))
print(type(carSelfDrive))




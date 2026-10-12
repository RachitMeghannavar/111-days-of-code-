# list comprehension (easier way to create a new list)
numbers_2 = [i for i in range(1,11)]
print(numbers_2)

even_numbers = [i for i in range(100) if i % 2== 0]
print(even_numbers)

names = ['Alex', 'Bob', 'Charlie', 'David', 'Eve']
short_names = [name for name in names if len(name) < 5]
print(short_names)

capital_names = [name.upper() for name in names if len(name) > 5]
print(capital_names)

# create a list with all the odd number from 1-100
odd_numbers = [i for i in range(100) if i % 2 != 0]
print(odd_numbers)

# Dictionary Comprehension
import random
student_scores = {
    student: random.randint(1,100) for student in names
}
print(student_scores)
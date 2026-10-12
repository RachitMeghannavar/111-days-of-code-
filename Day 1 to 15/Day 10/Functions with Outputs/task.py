# Normal function
def add(n1, n2):
    print(n1 + n2)

add(10,20)

# Function with output
def add_2(n1, n2):
    return n1 + n2

sum_2 = add_2(10, 20)
print(sum_2 + 10)
print(f"The sum was {sum_2} ")

# Create a function called format_name() that takes two inputs: f_name and `l_name
def format_name():
    f_name = (input("What is your first name? ")).title()
    l_name = (input("What is your last name? ")).title()
    return (f"{f_name} {l_name}")
print(format_name())
# Use the title() function to modify the f_name and l_name parameters into Title Case.
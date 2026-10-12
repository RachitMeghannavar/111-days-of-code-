import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
# print(operations["+"](10 ,20))

def calculater():
    print(art.logo)
    should_continue = True
    num_1 = float(input("Please enter your first number: "))
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation = input("Please enter your operation:")
        num_2 = float(input("Please enter your second number: "))
        answer = operations[operation](num_1, num_2)
        print(f"{num_1} {operation} {num_2} = {answer}")
        choice = input(f"Type 'y' to continue with the {answer}, or type 'n' to start new calculation.: ")
        if choice == "y":
            num_1 = answer
        else:
            should_continue = False
            print("\n" * 20 )
            calculater()
calculater()
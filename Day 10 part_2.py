def add(n1 , n2):
    return n1 + n2

def subtract(n1 , n2):
    return n1 - n2

def multiply(n1 , n2):
    return n1 * n2

def divide(n1 , n2):
    return n1 / n2

def module(n1 , n2):
    return n1 % n2

def power(n1 , n2):
    return n1 ** n2

operations = {
    "+": add,
    "-":subtract,
    "*":multiply,
    "/":divide,
    "%":module,
    "**":power
}

def calculator():
    should_continue = True
    num1 = float(input("Enter the first number: "))

    while should_continue:
        for letter in operations:
            print(letter)
        operation_letter = input("Pick an operation: ")
        num2 = float(input("Enter the second number: "))
        answer = (operations[operation_letter](num1,num2))
        print(f"{num1} {operation_letter} {num2} = {answer}")


        choice = input("Type 'y' to continue calculating "
                       "with {answer} or type 'n' to start a new calculation: ").lower()
        if choice == "Y":
            num1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()


calculator()

























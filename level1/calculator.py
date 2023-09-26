# A simple python calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Invalid number!"
    return x / y

while True:
    operator = input("Enter the operation (+, -, *, /) or 'exit' to finish the program: ")

    if operator == "exit":
        break

    if operator not in "+-*/":
        print("Invalid operation.")
        continue

    num1 = float(input("Enter the First number: "))
    num2 = float(input("Enter the Second number: "))

    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)

    print(f"Result: {result}")

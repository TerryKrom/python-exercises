# calculate the factorial of a number

def factorial(number):
    if number < 0:
        return "Invalid number!"
    elif number == 0 or number == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, number + 1):
            factorial *= i
        return factorial

number = int(input("Enter a number: "))
res = factorial(number)
print("The factorial of {} is: !{}".format(number, res))
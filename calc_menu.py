# Final Assignment: Calculator
# Code Reviewer: Markus Lindberg och Eric Granström

from calculations import add, subtract, divide, \
    multiply  # istället för import * kan skriva add, subtract, divide, multiply

operation = float(input("Choose one of the following operators: "
                        "\n 1. Addition \n 2. Subtraction \n 3. Division \n 4. Multiply"))

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))


def calc_menu():
    if operation == 1:
        print(num1, "+", num2, "=",
              add(num1, num2))

    elif operation == 2:
        print(num1, "-", num2, "=",
              subtract(num1, num2))

    elif operation == 3:
        print(num1, "/", num2, "=",
              divide(num1, num2))

    elif operation == 4:
        print(num1, "*", num2, "=",
              multiply(num1, num2))

    else:
        print("Invalid input")


calc_menu()

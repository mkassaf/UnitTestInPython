from calculatorApp import *

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    try:
        print("The answer is :: " + calculate(choice, num1, num2))
    except Exception as e:
        print(e)
    # check if user wants another calculation
    # break the while loop if answer is no
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if isExit(next_calculation):
        break
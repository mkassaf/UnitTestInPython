# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y



def calculate(choice, num1, num2 ):
    # check if choice is one of the four options
    result = ""
    if choice in ('1', '2', '3', '4'):

        if choice == '1':
            result = add(num1, num2)

        elif choice == '2':
            result = subtract(num1, num2)

        elif choice == '3':
            result = num1, "*", num2, "=", multiply(num1, num2)

        elif choice == '4':
            result = num1, "/", num2, "=", divide(num1, num2)
    else:
        result = "Invalid Input"
    
    return result

def isExit(next_calculation):
    if next_calculation == "no":
        return True
    return False   

def Run():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        # take input from the user
        choice = input("Enter choice(1/2/3/4): ")

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(calculate(choice, num1, num2))
        # check if user wants another calculation
            # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if isExit(next_calculation):
            break


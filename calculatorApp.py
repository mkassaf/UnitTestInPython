# Simple calculator

def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        return val
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            return val
        except ValueError:
            print(input + " input is not a number!")
            raise ValueError(input + " input is not a number!")


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
    if y == 0:
        print("You can't divide by zero!")
        raise ZeroDivisionError("You can't divide by zero!")
    else:
        return x / y



def calculate(choice, num1, num2 ):
    # check if choice is one of the four options
    if not num1 or not num2:
        print("inputs can not be null")
        raise ValueError("inputs can not be null")  
    num1 = check_user_input(num1)
    num2 = check_user_input(num2)
    result = ""
    if choice in ('1', '2', '3', '4'):

        if choice == '1':
            result = add(num1, num2)

        elif choice == '2':
            result = subtract(num1, num2)

        elif choice == '3':
            result = num1, "*", num2, "=", multiply(num1, num2)

        elif choice == '4':
            if num2 == 0:
                print("You can't divide by zero!")
                raise ZeroDivisionError("You can't divide by zero!")
            result = num1, "/", num2, "=", divide(num1, num2)
    else:
        raise Exception("Invalid choice!")

    return result

def isExit(next_calculation):
    if next_calculation == "no":
        return True
    return False   


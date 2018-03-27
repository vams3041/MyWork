def add(num1, num2):
    print("adding")
    return num1 + num2


def subtract(num1, num2):
    print("sub")
    return num1 - num2


def multiply(num1, num2):
    print("multi")
    return num1 * num2


def divide(num1, num2):
    print("div")
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Handled div by zero. Returning zero.")
        return 0


def runOperation(operation, firstNumber, secondNumber):
    if operation == '+':
        x = add(firstNumber, secondNumber)
    elif operation == '-':
        x = subtract(firstNumber, secondNumber)
    elif operation == '*':
        x = multiply(firstNumber, secondNumber)
    elif operation == '/':
        x = divide(firstNumber, secondNumber)
    else:
        x = "Not a valid entry"
    print("Result = ", x)


def main():
    validInput = False
    while not validInput:
        try:
            firstNumber = int(input("Enter first number "))
            secondNumber = int(input("Enter second number"))
            operation = input("what do you want to do (1 = add,2 = subtract,3 = multiply,4 = divide) ? "
                                  "Enter number: ")
            validInput = True
        except ValueError:
            print("Invalid Input. The program will now exit")
        except:
            print("Unknown error")
    runOperation(operation, firstNumber, secondNumber)


if __name__ == "__main__":
    main()
# A very simple Calculator program 
def add(x, y):
    return x + y


def minus(x, y):
    return x - y


def times(x, y):
    return x * y

def divide(x, y):
    return x / y


def main():
    
    while True:
        action = input("What would you like to do(+, -, *, /):\n")
        if action != "+" and action != "-" and action != "*" and action != "/":
            print("Enter a valid operator.")
        else:
            break
    while True:
        try:
            num1 = float(input("Enter first number:\n"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            num2 = float(input("Enter second number:\n"))
            break
        except ValueError:
            print("Please enter a valid number.")
    if action == "+":
        print(f"Answer: {add(num1, num2)}")
    elif action == "-":
        print(f"Answer: {minus(num1, num2)}")
    elif action == "/":
        try:
            print(f"Answer: {divide(num1, num2)}")
        except ZeroDivisionError:
            print("Error. You cant divide with a Zero")
    else:
        print(f"Answer: {times(num1, num2)}")


while True:               #To continue looping the program
    main()
    print("\n")


  

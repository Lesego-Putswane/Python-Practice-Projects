print("_____Welcome to Segos simple calculator_____\n")

def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter an operator you'd like to use (+, -, *, /): ")

    # implementing conditionals as per operators
    if operator == "+":
        # additions
        result = num1 + num2
    elif operator == "-":
        # subtraction
        result = num1 - num2
    elif operator == "*":
        # multiplication
        result = num1 * num2
    elif operator == "/":
        # division
        if num2 == 0:
            # handling zero division
            return "Division by 0 is invalid! Please enter number greater than 0."
        else:
            result = num1 / num2
    else:
        return "Invalid operator provided!"
    
    # refining the result to print out integer if result is an integer
    if result.is_integer():
        return f"{num1} {operator} {num2} = {int(result)}"
    else:
        return result

# loop that that controls repetition    
while True:
    output = calculator()
    print(output)

    while True:
        recalculate = input("\nPerform another calculation? yes(y) / no(n): ").lower()

        if recalculate in ["yes","y"]:
            break
        elif recalculate in ["no","n"]:
            print("See you next time!")
            exit()
        else:
            print("Invalid option please type 'yes/y' or 'no/n'!")

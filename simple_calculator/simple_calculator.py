print("_____Welcome to Segos simple calculator_____\n")

# getting user inputs
def get_numbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter an operator you'd like to use (+, -, *, /): ")

    return num1, num2, operator

# implementing conditionals as per operators
def calculator(num1, num2, operator):
    if operator == "+":
        # additions
        return num1 + num2
    elif operator == "-":
        # subtraction
        return num1 - num2
    elif operator == "*":
        # multiplication
        return num1 * num2
    elif operator == "/":
        # division
        if num2 == 0:
            # handling zero division
            return "Division by 0 is invalid!"
        else:
            return num1 / num2
    else:
        return "Invalid operator provided!"

# refining the result to print out integer if result is an integer   
def output_format(num1, num2, operator, result):
    if isinstance(result, float):
        if result.is_integer():
            return f"{num1} {operator} {num2} = {int(result)}"
        else:
            return f"{num1} {operator} {num2} = {result}"
    else:
        return result

# loop that that controls repetition
def recalculate():   
    while True:
        num1, num2, operator = get_numbers()
        result = calculator(num1, num2, operator)
        output = output_format(num1, num2, operator, result)
        print(output)

        while True:
            again = input("\nPerform another calculation? yes(y) / no(n): ").lower()
            
            if again in ["yes","y"]:
                break
            elif again in ["no","n"]:
                print("See you next time!")
                return
            else:
                print("Invalid input!")

recalculate()
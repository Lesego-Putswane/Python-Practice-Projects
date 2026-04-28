def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter an operator you'd like to use (+, -, *, /): ")

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Division by 0 is invalid! Please enter number greater than 0."
        else:
            return num1 / num2
    else:
        return "Invalid operator provided! Please enter +, -, *, / "
    
print(calculator())
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
        return "Invalid operator provided! Please enter +, -, *, / "
    
    # refining the result to print out integer if result is an integer
    if result.is_integer():
        return int(result)
    else:
        return result
    
print(calculator())
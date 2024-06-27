# match_case_calculator.py

# Function to perform operations
def calculate(num1, num2, operator):
    result = None
    # Match Case statement to perform operations based on operator
    match operator:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Cannot divide by zero."

    return result

# Main program
if __name__ == "__main__":
    # Prompting user for input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Choose the operation (+, -, *, /): ")

    # Calling calculate function
    result = calculate(num1, num2, operator)

    # Displaying the result
    if isinstance(result, str):  # If result is a string (error message)
        print(result)
    else:
        print(f"The result is {result}.")

# match_case_calculator.py

def main():
    # Prompting user for input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ")

    # Using match case to perform operation based on user input
    result = None
    error_message = "Cannot divide by zero."
    
    match operation:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            if num2 == 0:
                print(error_message)
            else:
                result = num1 / num2
        case _:
            print("Invalid operation. Please choose from '+', '-', '*', '/'.")

    # Displaying the result
    if result is not None:
        if operation == '/':
            if result is not None:
                print(f"The result is {result:.2f}.")
        else:
            print(f"The result is {result}.")

if __name__ == "__main__":
    main()

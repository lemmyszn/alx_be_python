def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        return "Error: Both numerator and denominator must be numeric."
                       
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    return f"Result: {result}"

import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

        numerator = sys.argv[1]
        denominator = sys.argv[2]

        result = safe_divide(numerator, denominator)
        print(result)

    if __name__ == "__main__":
        main()


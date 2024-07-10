def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        return "Error: Both numerator and denominator must be numeric."

    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

    return f"The result of the division is {result:.1f}"

# Example usage (uncomment to test)
# print(safe_divide(10, 2))
# print(safe_divide(10, 0))
# print(safe_divide("a", 2))


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

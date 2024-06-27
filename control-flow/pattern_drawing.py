# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Validate the input to ensure it's a positive integer
while size <= 0:
    print("Please enter a positive integer.")
    size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop to iterate through each row
while row < size:
    # Use for loop to print asterisks for each column in the row
    for _ in range(size):
        print("*", end="")
    # Print a newline character after each row
    print()
    # Move to the next row
    row+= 1 
    


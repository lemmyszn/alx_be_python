# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  # Ensure this line is present

def convert_to_celsius(fahrenheit):
    # Use the global conversion factor
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    # Use the global conversion factor
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        # Prompt the user to enter a temperature
        temperature = float(input("Enter the temperature to convert: "))
        
        # Prompt the user to specify the unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

        # Convert and display the temperature based on the input unit
        if unit == 'F':
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature:.1f}°F is {converted_temperature:.1f}°C")
        elif unit == 'C':
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}°C is {converted_temperature:.1f}°F")
        else:
            print("Invalid temperature unit. Please enter 'C' or 'F'.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()





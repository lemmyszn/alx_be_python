FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_OFFSET = 32
CELSIUS_TO_FAHRENHEIT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - FAHRENHEIT_TO_CELSIUS_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + CELSIUS_TO_FAHRENHEIT_OFFSET
    return fahrenheit

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

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





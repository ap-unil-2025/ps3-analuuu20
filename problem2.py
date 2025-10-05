"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""
#def celsius_to_farenheit

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

#def fahrenheit_to_celsius(fahrenheit):

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) × 5/9
    """
    celsius = (fahrenheit - 32) *(5/9)
    return celsius

#temperature_converter():

def temperature_converter():
    """
    Interactive temperature converter.
    Ask user for temperature and unit, then display conversion.
    """
    temp_input = input("Enter temperature value: ").strip()
    try:
        temp_value = float(temp_input)
    except ValueError:
        print("Invalid temperature value. Please enter a number.")
        return

    unit = input("Enter unit (C or F): ").strip().upper()
    if unit == "C":
        converted = celsius_to_fahrenheit(temp_value)
        print(f"{temp_value:.2f}°C is {converted:.2f}°F")
    elif unit == "F":
        converted = fahrenheit_to_celsius(temp_value)
        print(f"{temp_value:.2f}°F is {converted:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")

print("Temperature Converter")
print("-" * 30)

# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    print("Running tests...")

    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"

    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"

    print("All tests passed!")
    print()

    # Run interactive converter
    temperature_converter()
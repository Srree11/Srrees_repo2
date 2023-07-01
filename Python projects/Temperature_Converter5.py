def convert_temperature():
    """Converts temperature from Celsius to Fahrenheit or vice versa"""
    while True:
        try:
            temperature = float(input("Enter temperature: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    while True:
        conversion_type = input("Convert to (F)ahrenheit or (C)elsius? ").upper()
        if conversion_type == 'F':
            result = (temperature * 9/5) + 32
            print(f"{temperature}°C is {result}°F")
            break
        elif conversion_type == 'C':
            result = (temperature - 32) * 5/9
            print(f"{temperature}°F is {result}°C")
            break
        else:
            print("Invalid input. Please enter 'F' or 'C'.")

# Example usage
convert_temperature()
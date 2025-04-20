def unit_converter(fahrenheit):
    degrees_celsius = (fahrenheit - 32) * 5.0 / 9.0
    print(f"{fahrenheit}°F is {degrees_celsius:.2f}°C")

try:
    tempInFahrenheit = float(input("Enter a temperature in Fahrenheit: "))
    unit_converter(tempInFahrenheit)
except ValueError:
    print("❌ Please enter a valid number.")

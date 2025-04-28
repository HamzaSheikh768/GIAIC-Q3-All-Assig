# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

#____________________________ Example usage
temp = TemperatureConverter.celsius_to_fahrenheit(25)
print(f"25°C in Fahrenheit: {temp}")
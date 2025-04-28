def main():
    # User se Fahrenheit me temperature lena
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Fahrenheit ko Celsius me convert karna
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

    # Output print karna
    print(f"Temperature: {degrees_fahrenheit}F = {round(degrees_celsius, 2)}C")


# Function ko execute karne ke liye
if __name__ == '__main__':
    main()

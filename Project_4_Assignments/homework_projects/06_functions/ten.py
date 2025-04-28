def print_ones_digit(num):
    # Print the ones digit by getting the remainder when dividing by 10
    print("The ones digit is", num % 10)

def main():
    # Take input from the user
    num = int(input("Enter a number: "))
    # Call the function to print the ones digit
    print_ones_digit(num)

if __name__ == '__main__':
    main()

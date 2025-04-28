def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(1, num + 1):  # Iterate through numbers from 1 to num inclusive
        if num % i == 0:  # If num is divisible by i without a remainder
            print(i)  # Print the divisor

def main():
    num = int(input("Enter a number: "))  # Get user input for the number
    print_divisors(num)  # Call the function to print divisors of the number

if __name__ == '__main__':
    main()  # Run the main function

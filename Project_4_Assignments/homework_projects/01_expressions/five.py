def main():
    # User se do numbers lena
    dividend = int(input("Please enter an integer to be divided: "))  # Pehla number
    divisor = int(input("Please enter an integer to divide by: "))   # Dusra number

    # Quotient (result of division)
    quotient = dividend // divisor  # Integer division (no decimal part)

    # Remainder
    remainder = dividend % divisor  # Modulo operation to get remainder

    # Output the result
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))


# Function ko call karna
if __name__ == '__main__':
    main()

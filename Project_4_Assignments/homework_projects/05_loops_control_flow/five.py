def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))
    
    # Loop to double the value until it reaches 100 or greater
    while curr_value < 100:
        # Double the current value
        curr_value = curr_value * 2
        print(curr_value)

# Python boilerplate
if __name__ == '__main__':
    main()

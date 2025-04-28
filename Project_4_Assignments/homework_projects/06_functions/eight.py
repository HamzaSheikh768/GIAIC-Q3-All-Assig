def print_multiple(message: str, repeats: int):
    # Print the message 'repeats' number of times
    for i in range(repeats):
        print(message)

def main():
    message = input("Please type a message: ")  # Get the message from the user
    repeats = int(input("Enter a number of times to repeat your message: "))  # Get the repeat count from the user
    print_multiple(message, repeats)  # Call the function to print the message

if __name__ == '__main__':
    main()  # Run the main function

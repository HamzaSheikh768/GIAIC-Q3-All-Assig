def greet(name: str):
    print("Greetings", name + "!")  # Print the greeting message

def main():
    name = input("What's your name? ")  # Get user's name
    greet(name)  # Call the greet function

if __name__ == '__main__':
    main()

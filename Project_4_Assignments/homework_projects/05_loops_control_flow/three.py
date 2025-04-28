AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    # Print the affirmation message to the user
    print("Please type the following affirmation: " + AFFIRMATION)

    # Get the user's input
    user_feedback = input()

    # Keep prompting the user until they type the affirmation correctly
    while user_feedback != AFFIRMATION:
        print("That was not the affirmation.")
        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()

    # Once they type it correctly, display a success message
    print("That's right! :)")

# Python boilerplate
if __name__ == '__main__':
    main()

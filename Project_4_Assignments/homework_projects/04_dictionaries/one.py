def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create an empty phonebook dictionary

    while True:
        name = input("Name: ")
        if name == "":  # Stop if the user enters an empty string
            break
        number = input("Number: ")
        phonebook[name] = number  # Add the name and number to the dictionary

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))  # Print name and corresponding number


def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":  # Stop if the user enters an empty string
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")  # Name not found
        else:
            print(phonebook[name])  # Print the number if the name is found


def main():
    phonebook = read_phone_numbers()  # Collect phone numbers from the user
    print_phonebook(phonebook)  # Print the phonebook
    lookup_numbers(phonebook)  # Allow the user to lookup phone numbers


# Python boilerplate
if __name__ == '__main__':
    main()

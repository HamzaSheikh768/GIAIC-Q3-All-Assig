ADULT_AGE = 18  # Age considered as an adult

def is_adult(age: int):
    return age >= ADULT_AGE  # Return True if age is 18 or above, else False

def main():
    age = int(input("How old is this person?: "))  # Get user input
    print(is_adult(age))  # Print True or False based on age

if __name__ == "__main__":
    main()

MINIMUM_HEIGHT : int = 50  # arbitrary units :)

def main():
    # Get the user's height
    height = float(input("How tall are you? "))
    
    # Check if the user is tall enough to ride
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()

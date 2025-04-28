def main():
    # Step 1: User se input lo
    curr_value = int(input("Enter a number: "))

    # Step 2: Double karte raho jab tak value < 100 ho
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

# Required line to call main function
if __name__ == '__main__':
    main()

def main():
    # Loop through numbers from 10 to 19
    for i in range(10, 20):
        if is_odd(i):  # Check if the number is odd
            print(f"{i} odd")
        else:  # If it's not odd, it's even
            print(f"{i} even")
            
def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns True.
    """
    remainder = value % 2  # 0 if value is divisible by 2, 1 if it isn't
    return remainder == 1  # True if it's odd (remainder is 1)

if __name__ == '__main__':
    main()

def in_range(n: int, low: int, high: int) -> bool:
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    if low <= n <= high:  # Simplified condition
        return True
    return False  # No need for `else`, since the function returns either way

def main():
    # Get user input
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    # Call the function and print result
    print(in_range(n, low, high))

if __name__ == '__main__':
    main()

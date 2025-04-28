def add_many_numbers(numbers) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    total_so_far: int = 0
    for number in numbers:
        total_so_far += number  # Add each number to the total
    
    return total_so_far

def main():
    # Define a list of numbers
    numbers = [1, 2, 3, 4, 5]
    # Call the function to sum the numbers
    sum_of_numbers = add_many_numbers(numbers)
    # Print the result
    print(sum_of_numbers)

if __name__ == '__main__':
    main()

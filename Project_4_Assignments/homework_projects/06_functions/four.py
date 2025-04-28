def double(num: int):
    return num * 2

def main():
    num = int(input("Enter a number: "))  # Ask the user to input a number
    num_times_2 = double(num)  # Call the double function
    print("Double that is", num_times_2)  # Print the result

if __name__ == '__main__':
    main()

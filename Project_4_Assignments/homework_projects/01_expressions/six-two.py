# Useful constants to help make the math easier and cleaner!
DAYS_PER_YEAR = 365    # Number of days in a year
HOURS_PER_DAY = 24     # Number of hours in a day
MIN_PER_HOUR = 60      # Number of minutes in an hour
SEC_PER_MIN = 60       # Number of seconds in a minute

def main():
    # Calculate the number of seconds in a year using the constants
    seconds_in_year = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    # Output the result in a nice format
    print(f"There are {seconds_in_year} seconds in a year!")

# Run the program
if __name__ == '__main__':
    main()

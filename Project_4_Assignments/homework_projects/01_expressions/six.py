# Importing random module to simulate random rolls
import random

# Number of sides on each die to roll
NUM_SIDES = 6

def main():
    # Rolling both dice
    die1 = random.randint(1, NUM_SIDES)  # First die roll
    die2 = random.randint(1, NUM_SIDES)  # Second die roll
    
    # Total of both dice
    total = die1 + die2
    
    # Printing the results
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)


# This is required to run the main() function
if __name__ == '__main__':
    main()

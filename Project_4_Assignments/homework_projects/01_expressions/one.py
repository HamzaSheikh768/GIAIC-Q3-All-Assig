import random

# Number of sides on each die
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total.
    """
    die1 = random.randint(1, NUM_SIDES)  # First die roll
    die2 = random.randint(1, NUM_SIDES)  # Second die roll
    total = die1 + die2  # Sum of both dice
    print("Total of two dice:", total)

def main():
    die1 = 10  # Local variable in main()
    print("die1 in main() starts as: " + str(die1))

    # Roll dice 3 times
    roll_dice()
    roll_dice()
    roll_dice()

    print("die1 in main() is: " + str(die1))  # Scope demonstration

# Required to call the main function
if __name__ == '__main__':
    main()

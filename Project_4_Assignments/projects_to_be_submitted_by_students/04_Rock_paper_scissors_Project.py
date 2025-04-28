import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    options = ["rock", "paper", "scissors"]

    # User input
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    # Computer random choice
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    # Result checking
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("You win!")
    elif user_choice in options:
        print("You lose!")
    else:
        print("Invalid input! Please choose rock, paper, or scissors.")

# Run the game
play_game()

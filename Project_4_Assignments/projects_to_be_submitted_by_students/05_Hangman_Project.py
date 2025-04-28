import random

# Word list
words = ["python", "programming", "hangman", "streamlit", "project"]

# Select a random word
word = random.choice(words)
guessed_letters = []
tries = 6

print("🎮 Welcome to Hangman Game!")
print("_ " * len(word))

while tries > 0:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!")
    else:
        tries -= 1
        print(f"Wrong guess! Tries left: {tries}")

    # Show the word progress
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word)

    # Check if the user has guessed the word
    if "_" not in display_word:
        print("🎉 You won! The word was:", word)
        break
else:
    print("😢 You lost! The word was:", word)

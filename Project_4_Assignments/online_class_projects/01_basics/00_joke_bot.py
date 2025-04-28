import random

# Constants
PROMPT: str = "What do you want? "
JOKES: list = [
    "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk.",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "I told my computer I needed a break, and it said: 'Why? You barely do any work!'",
    "Debugging: Being the detective in a crime movie where you are also the murderer.",
    "Why did the developer go broke? Because he used up all his cache."
]
SORRY: str = "Sorry I only tell jokes."

def main():
    user_input = input(PROMPT)

    if user_input == "Joke":
        print(random.choice(JOKES))
    else:
        print(SORRY)

if __name__ == "__main__":
    main()

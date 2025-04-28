# Mad Libs Game - AI-101 Project 1

def main():
    print("Welcome to the Mad Libs Game!")
    print("Fill in the blanks below:\n")

    # Getting user inputs
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb (past tense): ")
    adverb = input("Enter an adverb: ")
    place = input("Enter a place: ")

    # Mad libs story
    story = f"""
    One day, I went to the {place} with my {noun}.
    It was a very {adjective} day.
    We {verb} all day and laughed {adverb}.
    It was the best day ever!
    """

    print("\nHere is your Mad Libs story:")
    print(story)

# Run the main function
if __name__ == "__main__":
    main()

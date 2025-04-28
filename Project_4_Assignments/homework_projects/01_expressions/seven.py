# Sentence starter constant
SENTENCE_START = "Panaversity is fun. I learned to program and used Python to make my "

def main():
    # User inputs for adjective, noun, and verb
    adjective = input("Please type an adjective and press enter. ")
    noun = input("Please type a noun and press enter. ")
    verb = input("Please type a verb and press enter. ")

    # Constructing and printing the final sentence
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")
    
# Calling main function to run the program
if __name__ == '__main__':
    main()

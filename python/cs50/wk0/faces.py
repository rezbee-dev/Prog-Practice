# https://cs50.harvard.edu/python/psets/0/faces/
# - implement a function called convert that accepts a str as input and 
#   - returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and
#   - returns any :( converted to 🙁 (otherwise known as a slightly frowning face). 
#   - All other text should be returned unchanged.
# - implement a function called main that prompts the user for input, calls convert on that input, and prints the result.
# - You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.

# Test Cases
# Input: Hello :), output: Hello 🙂
# Input: Goodbye :(, output: Goodbye 🙁
# Input: Hello :) Goodbye :(, output: Hello 🙂 Goodbye 🙁

import sys

def convert(word: str) -> str:

    if word == ":)":
        return "\U0001F642"
    elif word == ":(":
        return "\U0001F641"
    else:
        return word.capitalize()
    
def convert_sentence(sentence: str) -> str:
    if len(sentence) == 1:
        return sentence
    else:
        new_sentence = []
        for word in sentence.split(" "):
            new_sentence.append(convert(word))
        
        return " ".join(new_sentence)

def main() -> int:
    
    try:
        contents = input("Input: \n")
        
        if len(contents) == 0:
            print("No input found!")

        print(convert_sentence(contents))
    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
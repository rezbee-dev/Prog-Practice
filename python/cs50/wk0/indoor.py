# https://cs50.harvard.edu/python/psets/0/
# - In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. 
# - Punctuation and whitespace should be outputted unchanged. 
# - You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.

# Test Cases
# Input: HELLO, output: hello
# Input: THIS IS CS50, output: this is cs50
# Input: 50, output 50

import sys

def lower_caser(word: str) -> str:

    if word.isalpha():
        return word.lower()
    elif len(word) > 1:
        new_word = []
        for l in list(word):
            if l.isalpha():
                l = l.lower()
            new_word.append(l)
        return "".join(new_word)

    return word

def main() -> int:
    
    try:
        contents = input("Can I take your order please? \n")
        new_contents = []
        
        if len(contents) == 0:
            print("No input found!")

        for word in contents.split():
            new_contents.append(lower_caser(word))

        print(" ".join(new_contents))
    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
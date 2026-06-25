# https://cs50.harvard.edu/python/psets/0/playback/
# - In a file called playback.py, implement a program in Python that prompts the user for input and 
#    - then outputs that same input, replacing each space with ... (i.e., three periods).

# Test Cases
# Input: THIS IS CS50, output: This...is...CS50
# Input: This is our week on functions, output: This...is...our...week...on...functions
# Input: Let's implement a function called hello, output: Let's...implement...a...function...called...hello



import sys

def ellipsis_adder(sentence: str) -> str:
    words = sentence.split(" ")

    if len(words) <= 1:
        return sentence
    else:
        new_sentence = []
        for i, word in enumerate(words):
            if i == 0:
                new_sentence.append(word.capitalize())
            elif i < len(words)-1:
                if not word.isalpha():
                    new_sentence.append(word.upper())
                else:
                    new_sentence.append(word.lower())

        return "...".join(new_sentence) + "..." + words[-1]
        

def main() -> int:
    try:
        contents = input("Input: \n")
        
        if len(contents) == 0:
            print("No input found!")

        print(ellipsis_adder(contents))
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
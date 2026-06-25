# https://cs50.harvard.edu/python/psets/0/einstein/
# -  implement a program in Python that prompts the user for mass as an integer (in kilograms)
#   - then outputs the equivalent number of Joules as an integer (E = mc^2 where c = 300000000)
#   - Assume that the user will input an integer.

# Test Cases
# Input: 1, output: 90000000000000000
# Input: 14, output: 1260000000000000000
# Input: 50, output: 4500000000000000000

import sys

C = 300000000

def convert(m: int) -> int:
    return m * pow(C, 2)
    

def main() -> int:
    
    try:
        contents = input("Input: \n")
        
        if len(contents) == 0:
            print("No input found!")

        print(convert(int(contents)))
    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
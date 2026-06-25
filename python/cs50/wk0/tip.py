# https://cs50.harvard.edu/python/psets/0/tip/
# - dollars_to_float() 
#   - should accept a str as input (formatted as $##.##, wherein each # is a decimal digit)
#   - remove the leading $
#   - return the amount as a float. 
#   - For instance, given $50.00 as input, it should return 50.0.
# - percent_to_float() 
#   - should accept a str as input (formatted as ##%, wherein each # is a decimal digit)
#   - remove the trailing %
#   - return the percentage as a float. 
#   - For instance, given 15% as input, it should return 0.15.
# - Assume that the user will input values in the expected formats.

# Test Cases
# Input: $50.00, 15%, output: Leave $7.50    
# Input: $100.00, 18%, output: Leave $18.00   
# Input: $15.00, 25%, output: Leave $3.75

import sys

def dollars_to_float(d):
    amt = float(d[1:])
    return amt

def percent_to_float(p):
    amt = int(p[:-1])
    return float(amt/100)
    

def main() -> int:
    
    try:
        dollars = dollars_to_float(input("How much was the meal? "))
        percent = percent_to_float(input("What percentage would you like to tip? "))
        tip = dollars * percent
        print(f"Leave ${tip:.2f}")
    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
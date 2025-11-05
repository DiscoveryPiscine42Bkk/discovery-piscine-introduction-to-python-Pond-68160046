#!/usr/bin/env python3
# The Shebang line makes the script directly executable.

# 1. Prompt the user for a number and convert the input string to an integer.
try:
    number = int(input())
except ValueError:
    # Basic error handling for non-numeric input.
    exit()

# 2. Use conditional logic (if, elif, else) to check the number's sign.
# The tests must be performed in a specific order to cover all cases correctly.

if number < 0:
    # Case 1: If the number is negative (less than 0).
    print("This number is negative.")
elif number > 0:
    # Case 2: If the number is positive (greater than 0).
    # We use 'elif' because we already checked for negative numbers.
    print("This number is positive.")
else:
    # Case 3: If the number is neither negative nor positive, it must be zero.
    print("This number is both positive and negative.")
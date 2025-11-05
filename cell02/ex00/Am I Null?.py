#!/usr/bin/env python3
# The line above is the Shebang, which tells the system to execute the script using python3.

# 1. Prompt the user for a number and store the input.
# The input is initially a string, so we must convert it to an integer (int())
# for proper numerical comparison.
try:
    number = int(input())
except ValueError:
    # Handle non-integer input gracefully, though usually not strictly required by these exercises.
    print("Invalid input. Please enter a whole number.")
    exit()

# 2. Use conditional logic (if/else) to check the number.
# The equality check uses the double equals sign (==).
if number == 0:
    # If the number is equal to zero, display the required message.
    print("This number is equal to zero.")
else:
    # If the number is NOT equal to zero, display the required message.
    print("This number is different from zero.")
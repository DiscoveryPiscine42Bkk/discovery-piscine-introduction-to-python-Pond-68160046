#!/usr/bin/env python3
# The Shebang line makes the script directly executable.

# 1. Import the math module to access the ceiling function.
import math

# 2. Prompt for and get user input.
user_input_str = input("Give me a number: ")

try:
    # 3. Convert the input string to a floating-point number (float).
    user_float = float(user_input_str)
    
    # 4. Use math.ceil() to calculate the smallest integer greater than or equal to user_float.
    # The result of math.ceil() is a float, so we convert it to an integer (int) for display
    # to match the output examples (e.g., '42' instead of '42.0').
    rounded_up_number = int(math.ceil(user_float))
    
    # 5. Display the result.
    print(rounded_up_number)
    
except ValueError:
    # Handle cases where the user enters non-numeric input.
    print("Error: Invalid number entered.")
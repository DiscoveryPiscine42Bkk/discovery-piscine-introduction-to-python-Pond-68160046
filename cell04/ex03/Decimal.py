#!/usr/bin/env python3
# The Shebang line makes the script directly executable.

# 1. Prompt for and get user input.
user_input_str = input("Give me a number: ")

try:
    # 2. Convert the input string to a floating-point number (float).
    # This correctly handles inputs like '42', '42.00', and '42.42'.
    user_float = float(user_input_str)
    
    # 3. Check if the float is equal to its integer representation.
    # float(42.00) == int(42.00)  -> 42.0 == 42  -> True (It's an integer)
    # float(42.42) == int(42.42)  -> 42.42 == 42 -> False (It's a decimal/float)
    if user_float == int(user_float):
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
        
except ValueError:
    # Handle cases where the user enters non-numeric input (e.g., text)
    print("Error: Invalid number entered.")
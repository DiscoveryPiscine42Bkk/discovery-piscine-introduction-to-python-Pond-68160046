#!/usr/bin/env python3
import sys

# The number of user parameters is len(sys.argv) - 1.
# We need exactly 1 parameter, so len(sys.argv) must be 2.

if len(sys.argv) == 2:
    # Case 1: Exactly one parameter is provided (at index 1)
    # Get the parameter, convert it to uppercase, and print.
    input_string = sys.argv[1]
    uppercase_string = input_string.upper()
    print(uppercase_string)
else:
    # Case 2: Zero, two, or more parameters are provided
    print("none")
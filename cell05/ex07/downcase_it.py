#!/usr/bin/env python3
import sys

# We require exactly 1 user parameter, meaning len(sys.argv) must be 2.

if len(sys.argv) == 2:
    # Case 1: Exactly one parameter is provided (at index 1)
    # Get the parameter, convert it to lowercase, and print.
    input_string = sys.argv[1]
    lowercase_string = input_string.lower()
    print(lowercase_string)
else:
    # Case 2: Zero, two, or more parameters are provided
    print("none")
#!/usr/bin/env python3
import sys

# We require exactly 1 user parameter, meaning len(sys.argv) must be 2.

if len(sys.argv) != 2:
    # Case 1: Incorrect number of parameters (0 or 2+)
    print("none")
else:
    # Case 2: Exactly one parameter is provided
    required_parameter = sys.argv[1]
    
    # Prompt the user for input using the specified string.
    # The input() function reads the user's line.
    user_input = input("What was the parameter? ")
    
    # Compare the command-line argument with the user's input
    if user_input == required_parameter:
        print("Good job!")
    else:
        print("Nope, sorry...")
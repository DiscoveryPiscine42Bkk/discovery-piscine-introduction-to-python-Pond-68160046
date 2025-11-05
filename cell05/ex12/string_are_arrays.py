#!/usr/bin/env python3
import sys

# We require exactly 1 user parameter, meaning len(sys.argv) must be 2.

if len(sys.argv) != 2:
    # Case 1: Incorrect number of parameters (0 or 2+)
    print("none")
else:
    # Case 2: Exactly one parameter is provided
    input_string = sys.argv[1]
    
    # Convert the string to lowercase to handle both 'Z' and 'z'
    lower_string = input_string.lower()
    
    z_count = 0
    
    # Iterate over the string, treating it like an array of characters
    for char in lower_string:
        if char == 'z':
            # Print 'z' for every occurrence and increment the count
            print('z')
            z_count += 1
            
    # After checking the whole string, verify if any 'z' was found
    if z_count == 0:
        # Case 3: Parameter count was 1, but no 'z' characters were found
        print("none")
#!/usr/bin/env python3
import sys

# Get the list of actual parameters (excluding the script name at index 0)
params = sys.argv[1:]

# Check if the number of parameters is less than 2
if len(params) < 2:
    print("none")
else:
    # Reverse the order of the parameters
    # The .reverse() method reverses the list in-place
    params.reverse()
    
    # Iterate through the reversed list and print each element on a new line
    for param in params:
        print(param)
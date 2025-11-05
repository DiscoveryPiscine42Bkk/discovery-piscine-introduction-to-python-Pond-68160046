#!/usr/bin/env python3
import sys

# The sys.argv list contains the script name at index 0.
# The first actual parameter is at index 1.

# Check if the total length of arguments is 1, which means only the script name
# is present, and therefore, there are 0 user-supplied parameters.
if len(sys.argv) == 1:
    # Case 1: No parameters provided
    print("none")
else:
    # Case 2: One or more parameters provided
    # The first parameter is always at index 1
    print(sys.argv[1])
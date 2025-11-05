#!/usr/bin/env python3
import sys

# Get the list of actual parameters (excluding the script name at index 0)
params = sys.argv[1:]

if not params:
    # Case 1: No parameters provided
    print("none")
else:
    # Case 2: One or more parameters provided
    for param in params:
        # Check if the parameter already ends with "ism"
        if not param.endswith("ism"):
            # If it doesn't end with "ism", append it and print
            print(param + "ism")
        # If it does end with "ism", the parameter is automatically skipped
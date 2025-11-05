#!/usr/bin/env python3
import sys

# Step 1: Define the required method
def downcase_it(s):
    """Takes a string and returns its lowercase version."""
    return s.lower()

# Get the list of actual parameters (excluding the script name at index 0)
params = sys.argv[1:]

if not params:
    # Step 3: Case 1: No parameters provided
    print("none")
else:
    # Step 4: Case 2: One or more parameters provided
    # Loop through all parameters and apply the method
    for param in params:
        result = downcase_it(param)
        print(result)
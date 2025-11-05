#!/usr/bin/env python3
import sys

# Get the list of actual parameters (excluding the script name at index 0)
params = sys.argv[1:]
num_parameters = len(params)

if num_parameters == 0:
    # Case 1: No parameters provided
    print("none")
else:
    # Case 2: One or more parameters provided
    
    # 1. Display the total count
    print(f"parameters: {num_parameters}")
    
    # 2. Display each parameter and its length
    for param in params:
        param_length = len(param)
        print(f"{param}: {param_length}")
#!/usr/bin/env python3
import sys

# --- Method Definitions ---

def shrink(s):
    """Takes a string and displays the first 8 characters using slicing."""
    # Slicing from the start up to index 8 (exclusive)
    print(s[:8])

def enlarge(s):
    """Takes a string, pads it with 'Z' characters to reach a total length of 8, and displays it."""
    current_length = len(s)
    
    # Calculate how many 'Z' characters are needed
    z_needed = 8 - current_length
    
    # Create the padding string using multiplication
    padding = 'Z' * z_needed
    
    # Concatenate and display the resulting 8-character string
    print(s + padding)

# --- Main Program Logic ---

# Get the list of actual parameters (excluding the script name at index 0)
params = sys.argv[1:]

if not params:
    # Case 1: Less than 1 parameter (0 parameters)
    print("none")
else:
    # Case 2: One or more parameters provided
    for param in params:
        param_length = len(param)
        
        if param_length > 8:
            # Over 8 characters: call shrink
            shrink(param)
        elif param_length < 8:
            # Under 8 characters: call enlarge
            enlarge(param)
        else: # param_length == 8
            # Exactly 8 characters: display directly
            print(param)
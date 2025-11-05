#!/usr/bin/env python3
import sys

# sys.argv is a list containing the script name and all arguments.
# Example: If the command is './parameters.py hello world', 
# sys.argv is ['/parameters.py', 'hello', 'world'] and len(sys.argv) is 3.

# The number of actual parameters passed by the user is the length of 
# sys.argv minus 1 (to exclude the script name itself).
num_parameters = len(sys.argv) - 1

# Display the required output, followed by a newline.
print(f"Number of parameters: {num_parameters}")
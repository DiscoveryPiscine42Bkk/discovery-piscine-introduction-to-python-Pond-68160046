#!/usr/bin/env python3
import sys

# We require exactly 2 user parameters, meaning len(sys.argv) must be 3.

if len(sys.argv) != 3:
    # Case 1: Incorrect number of parameters
    print("none")
else:
    try:
        # Convert parameters to integers
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])

        # Determine the start and stop for the range, making it inclusive
        start = min(num1, num2)
        # The range stop is exclusive, so we add 1 to include the maximum number
        stop_exclusive = max(num1, num2) + 1

        # Generate the range (array) of numbers
        # The result is cast to a list for the final output format.
        result_array = list(range(start, stop_exclusive))

        # Display the array using the print function
        print(result_array)

    except ValueError:
        # Optional: Handle case where parameters are not valid integers
        # Based on the prompt, only the parameter count check is mandatory, 
        # but robust code would handle this. We'll stick to the core requirement.
        print("none") # Or handle error as per environment rules
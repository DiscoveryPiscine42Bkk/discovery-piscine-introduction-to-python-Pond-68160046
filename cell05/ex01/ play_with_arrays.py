#!/usr/bin/env python3
# The Shebang line makes the script directly executable.

# 1. Define the original array (list in Python).
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# 2. Create an empty list for the new array.
new_array = []

# 3. Iterate over the original array using a for loop.
for number in original_array:
    # Add 2 to the current number
    modified_number = number + 2
    # Append the modified number to the new array
    new_array.append(modified_number)

# 4. Display both arrays with the required labels.
print(f"Original array: {original_array}")
print(f"New array: {new_array}")
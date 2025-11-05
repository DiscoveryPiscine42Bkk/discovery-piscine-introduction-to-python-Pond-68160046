#!/usr/bin/env python3

# NOTE: Assuming the array is provided via standard input 
# or a similar mechanism in the environment. 
# We use the example array for a runnable demonstration of the core logic.
# In a real shell pipe, you might need to process input first.
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# Filter: select elements > 5
# Process: add 2 to the selected elements
processed_array = [
    number + 2 
    for number in original_array 
    if number > 5
]

# Output: [10, 11, 50, 10, 24]
print(processed_array)
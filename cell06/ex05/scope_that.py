#!/usr/bin/env python3
import sys

# NOTE: The actual array input method (e.g., from stdin/file) is not specified. 
# We'll hardcode the example array for a runnable demonstration. 
# In a real environment, you might use 'eval(sys.stdin.read())' to read the array.

original_array = [2, 8, 9, 48, 8, 22, -12, 2] 

# 1. & 2. Filtering (x > 5) and Processing (x + 2) combined using list comprehension
processed_with_duplicates = [
    number + 2
    for number in original_array if number > 5
]
# processed_with_duplicates is now [10, 11, 50, 10, 24]

# 3. De-duplicate: Convert the list to a set to automatically remove duplicates,
# then convert back to a list for output.
unique_results_list = list(set(processed_with_duplicates))

# Display the final array. 
# The order might vary from the example output ([24, 10, 11, 50]) because sets are unordered.
print(unique_results_list)
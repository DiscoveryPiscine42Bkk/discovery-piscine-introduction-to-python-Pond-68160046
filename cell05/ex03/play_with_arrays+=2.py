# Assuming 'original_array' is read from input
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# --- Combined Filtering and Processing (Same as Ex 02) ---
processed_with_duplicates = [
    # 2. Process: add 2
    number + 2
    # 1. Filter: only if number > 5
    for number in original_array if number > 5
]
# processed_with_duplicates is now [10, 11, 50, 10, 24]

# --- 3. De-duplicate using a set ---
# Convert the list to a set to automatically remove duplicates.
unique_results_set = set(processed_with_duplicates)

# Convert back to a list for final output (the order is not guaranteed)
final_output_list = list(unique_results_set)

# This will print [10, 11, 50, 24] or [24, 10, 11, 50] depending on Python version/hashing
print(final_output_list)
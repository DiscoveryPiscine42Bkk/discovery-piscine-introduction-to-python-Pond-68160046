# Assuming the original array/list is named 'original_array'
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# 1. Filtering: Create a new list with elements > 5
filtered_array = []
for number in original_array:
    if number > 5:
        filtered_array.append(number)

# 2. Processing (Adding 2 to each element in the filtered array)
processed_array = []
for number in filtered_array:
    # Apply the previous program's logic (e.g., add 2)
    processed_array.append(number + 2)

# Output should be [10, 11, 50, 10, 24]
print(processed_array)
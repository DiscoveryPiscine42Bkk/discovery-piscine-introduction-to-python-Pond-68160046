#!/usr/bin/env python3
# The Shebang line makes the script directly executable.

# 1. Outer Loop: Controls the multiplier (the 'Table de X' number).
# Initialize the multiplier (i) to 0.
i = 0
while i <= 10:
    # This list will hold the calculated products for the current table (e.g., Table de 5: [0, 5, 10, ...])
    row_products = []
    
    # 2. Inner Loop: Controls the multiplicand (the numbers 0 through 10 in the list).
    # Initialize the multiplicand (j) to 0.
    j = 0
    while j <= 10:
        # Calculate the product of the current two numbers.
        product = i * j
        # Add the product to the list for the current row.
        row_products.append(str(product))
        
        # Increment the inner loop variable (j) to move to the next column.
        j += 1
        
    # 3. Output the current row after the inner loop finishes (j is now 11).
    # We join the list of product strings with a single space separator.
    print(f"Table de {i}: {' '.join(row_products)}")
    
    # 4. Increment the outer loop variable (i) to move to the next row/table.
    i += 1
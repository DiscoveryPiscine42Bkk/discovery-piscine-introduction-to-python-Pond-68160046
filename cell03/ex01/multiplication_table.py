#!/usr/bin/env python3
# The Shebang line makes the script directly executable.

# 1. Prompt for and get user input, converting to an integer.
# We are only prompting for the number, as seen in the example output.
try:
    multiplier = int(input("Enter a number\n"))
except ValueError:
    exit()

# 2. Use a for loop to iterate from 0 up to (and including) 9.
# The range(10) function generates numbers from 0 up to (but not including) 10.
for i in range(10):
    # Calculate the product.
    product = i * multiplier
    
    # 3. Display the result in the required format: "i x multiplier = product"
    print(f"{i} x {multiplier} = {product}")
#!/usr/bin/env python3
# The Shebang line makes the script directly executable.

# 1. Prompt for and get user input, converting to an integer.
print("Enter a number less than 25")
try:
    current_number = int(input())
except ValueError:
    exit()

# 2. Check the initial condition: if the number is greater than 25.
if current_number > 25:
    print("Error")
else:
    # 3. Use a while loop to display numbers from the input up to 25.
    # The loop continues as long as the current number is less than or equal to 25.
    while current_number <= 25:
        print(f"Inside the loop, my variable is {current_number}")
        # Increment the variable to move towards the loop's end condition (current_number <= 25).
        current_number += 1
#!/usr/bin/env python3
# The Shebang line makes the script directly executable.

# 1. Prompt for and get the first number, converting it to an integer.
try:
    num1 = int(input("Enter the first number: "))
except ValueError:
    exit()

# 2. Prompt for and get the second number, converting it to an integer.
try:
    num2 = int(input("Enter the second number: "))
except ValueError:
    exit()

# 3. Calculate the result of the multiplication.
result = num1 * num2

# 4. Display the equation (e.g., "42 x 42 = 1764").
print(f"{num1} x {num2} = {result}")

# 5. Determine and display whether the result is positive, negative, or zero.
# NOTE: The prompt requires "The result is positive and negative." for zero,
# matching the logic from a previous exercise.
if result < 0:
    print("The result is negative.")
elif result > 0:
    print("The result is positive.")
else:
    # This executes when result == 0
    print("The result is positive and negative.")
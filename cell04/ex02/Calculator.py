#!/usr/bin/env python3
# The Shebang line makes the script directly executable.

# 1. Prompt for and get the first number, converting it to a float to handle division.
num1_str = input("Give me the first number: ")

# 2. Prompt for and get the second number, converting it to a float.
num2_str = input("Give me the second number: ")

try:
    # Convert input strings to floating-point numbers (floats) for accurate division results.
    num1 = float(num1_str)
    num2 = float(num2_str)

    # Display the thank you message
    print("Thank you!")

    # 3. Perform and display the four basic operations.
    
    # Addition (+)
    print(f"{num1} + {num2} = {num1 + num2}")
    
    # Subtraction (-)
    print(f"{num1} - {num2} = {num1 - num2}")
    
    # Division (/)
    # Note: Python's '/' operator performs floating-point division.
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        # Handling division by zero to prevent an error
        print(f"{num1} / {num2} = Division by Zero Error")
        
    # Multiplication (*)
    print(f"{num1} * {num2} = {num1 * num2}")
    
except ValueError:
    # Handle cases where the user enters non-numeric input
    print("Error: Please enter valid numerical values.")
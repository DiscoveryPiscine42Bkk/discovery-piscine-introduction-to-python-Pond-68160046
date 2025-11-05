#!/usr/bin/env python3
# The Shebang line makes the script directly executable.

# 1. Prompt for user input and store it.
# The user's input is initially a string.
age_str = input("Please tell me your age: ")

try:
    # 2. Convert the input string to an integer.
    current_age = int(age_str)
    
    # 3. Perform the three calculations.
    age_in_10 = current_age + 10
    age_in_20 = current_age + 20
    age_in_30 = current_age + 30
    
    # 4. Display the current age and the three future ages with the required formatting.
    print(f"You are currently {current_age} years old.")
    print(f"In 10 years, you'll be {age_in_10} years old.")
    print(f"In 20 years, you'll be {age_in_20} years old.")
    print(f"In 30 years, you'll be {age_in_30} years old.")

except ValueError:
    # Basic error handling in case the user enters non-numeric input
    print("Invalid age entered. Please enter a whole number.")
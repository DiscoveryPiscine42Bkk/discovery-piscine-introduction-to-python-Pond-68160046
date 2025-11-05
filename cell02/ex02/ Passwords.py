#!/usr/bin/env python3
# The Shebang line makes the script directly executable.

# 1. Define the variable containing the correct password.
CORRECT_PASSWORD = "Python is awesome" # Using ALL CAPS for a constant variable is a common Python convention.

# 2. Prompt the user for input.
# We don't need to convert to an integer here, as passwords are strings.
user_input = input()

# 3. Use conditional logic to check if the user input matches the correct password.
if user_input == CORRECT_PASSWORD:
    # If the strings are exactly the same, grant access.
    print("ACCESS GRANTED")
else:
    # Otherwise, deny access.
    print("ACCESS DENIED")
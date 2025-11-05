#!/usr/bin/env python3

# Step 1-3: Define the method 'greetings' with a default parameter and type checking
def greetings(name="noble stranger"):
    """
    Displays a welcome message with the provided name. 
    Uses 'noble stranger' as default. Checks if the argument is a string.
    """
    
    # Check if the argument is a string
    if isinstance(name, str):
        # Print the welcome message for valid strings
        print(f"Hello, {name}.")
    else:
        # Print the error message for non-string arguments
        print("Error! It was not a name.")

# Step 4: Test the method as shown in the example

# Test case 1: String argument
greetings('Alexandra')

# Test case 2: Called without an argument (uses default)
greetings()

# Test case 3: Non-string argument (integer 42)
greetings(42)
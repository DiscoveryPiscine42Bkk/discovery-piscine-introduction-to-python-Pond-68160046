#!/usr/bin/env python3
# The Shebang line makes the script directly executable.

# 1. Start an infinite loop (it will run forever until explicitly told to stop).
while True:
    # 2. Accept user input with the specified prompt.
    user_input = input("What you gotta say? : ").strip()
    
    # 3. Check for the termination condition.
    if user_input.upper() == "STOP":
        # If the input is "STOP" (case-insensitive check using .upper()), 
        # exit the loop using the 'break' statement.
        break
    else:
        # 4. If the input is not "STOP", display the required response.
        # Note: The response uses the initial prompt again for subsequent inputs.
        print(f"I got that! Anything else? : {user_input}")

# The program exits cleanly after the loop breaks.
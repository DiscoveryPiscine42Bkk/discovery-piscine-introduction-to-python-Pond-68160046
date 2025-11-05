#!/usr/bin/env python3
# The Shebang line makes the script directly executable.

# 1. Prompt the user for a string. The prompt is implied by the output example.
user_string = input()

# 2. Use the .swapcase() string method to swap the case of all letters.
# The method returns a new string with the cases exchanged.
swapped_string = user_string.swapcase()

# 3. Display the resulting string.
print(swapped_string)
# 1. Ask the user for their first name and store the input.
# The .strip() method is used to remove any leading/trailing whitespace
# the user might accidentally include.
first_name = input("Hey, what's your first name? : ").strip()

# 2. Ask the user for their last name and store the input.
last_name = input("And your last name? : ").strip()

# 3. Finally display the greeting and the combined full name.
# An f-string is the easiest way to format the output.
print(f"Well, pleased to meet you, {first_name} {last_name}.")
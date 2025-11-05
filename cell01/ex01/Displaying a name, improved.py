# Define the first_name and last_name variables (from Exercise 00).
first_name = "Wil"
last_name = "42"

# Concatenate your last name and first name, and assign the result to whole_name.
# The exercise output "Wil 42$" shows the FIRST name then the LAST name,
# so we will concatenate them in that order, ensuring a space is included.
whole_name = first_name + " " + last_name

# Display the whole_name variable, followed by a new line.
print(whole_name)

# Note: The output "Wil 42$" in the image is a bit ambiguous as it says
# to concatenate 'last name and first name' but shows 'First Last' output.
# If the required output was "42 Wil", the concatenation would be:
# whole_name = last_name + " " + first_name
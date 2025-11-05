#!/usr/bin/env python3

def array_of_names(persons_dict):
    """
    Takes a dictionary {first_name: last_name} and returns a list 
    of capitalized full names (e.g., "First Last").
    """
    full_names_array = []
    
    # Iterate through the dictionary items (key=first_name, value=last_name)
    for first_name, last_name in persons_dict.items():
        # Capitalize the first letter of both names
        # .capitalize() is suitable for single words
        capitalized_first = first_name.capitalize()
        capitalized_last = last_name.capitalize()
        
        # Combine them into the full name string
        full_name = f"{capitalized_first} {capitalized_last}"
        
        # Append the full name to the list
        full_names_array.append(full_name)
        
    return full_names_array

# --- Program Test ---

# Define the dictionary as per the example
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

# Call the function and display the returned array
print(array_of_names(persons))
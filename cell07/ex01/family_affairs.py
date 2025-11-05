#!/usr/bin/env python3

def find_the_redheads(family_dict):
    """
    Takes a dictionary {name: color} and returns a list of names 
    where the color is 'red', using the filter function.
    """
    
    # Define a helper function (or lambda) for the filter
    def is_redhead(item):
        # item is a tuple: (name, color)
        # We check if the color (item[1]) is 'red'
        return item[1] == "red"

    # Use filter() on the dictionary's items() to get only the redhead tuples.
    # The filter object contains elements like ('florian', 'red'), ('david', 'red').
    redheads_items = filter(is_redhead, family_dict.items())
    
    # Extract just the name (the first element of each tuple)
    redheads_names = [name for name, color in redheads_items]
    
    return redheads_names

# --- Program Test ---

# Define the dictionary as per the example
dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

# Call the function and display the returned list
print(find_the_redheads(dupont_family))
# persons_of_interest.py

def famous_births(persons_data):
    """
    Sorts a dictionary of persons by their 'date_of_birth' and 
    prints their name, profession (hardcoded as 'great scientist'), and birth year.
    
    The input dictionary 'persons_data' has keys (e.g., 'ada') that map to 
    another dictionary with keys ':name' and ':date_of_birth'.
    """
    
    # 1. Extract the values (the nested dictionaries) from the input dictionary.
    # We'll work with a list of dictionaries for easier sorting.
    people_list = list(persons_data.values())

    # 2. Sort the list of people dictionaries.
    # We use the 'sort' method with a 'lambda' function as the key.
    # The lambda function tells Python to use the value associated with the 
    # ':date_of_birth' key for comparison during the sort.
    # The 'int()' conversion ensures they are sorted numerically, not alphabetically.
    # Note: If ':date_of_birth' was a proper date string (e.g., "YYYY-MM-DD"), 
    # we wouldn't need 'int()', but for just the year, it's safer.
    try:
        people_list.sort(key=lambda person: int(person[':date_of_birth']))
    except ValueError:
        # Handle cases where the date_of_birth might not be an integer
        print("Error: Birth dates must be convertible to integers for sorting.")
        return

    # 3. Display each entry in the sorted order.
    # The required output format is: "Name is a great scientist born in Year."
    for person in people_list:
        name = person[':name']
        birth_year = person[':date_of_birth']
        print(f"{name} is a great scientist born in {birth_year}.")

# --- Example Usage (from the exercise) ---
# Your method definition here

women_scientists = {
    "ada": {":name": "Ada Lovelace", ":date_of_birth": "1815"},
    "cecilia": {":name": "Cecilia Payne", ":date_of_birth": "1900"},
    "lise": {":name": "Lise Meitner", ":date_of_birth": "1878"},
    "grace": {":name": "Grace Hopper", ":date_of_birth": "1906"}
}

famous_births(women_scientists)

# --- End Example ---
#!/usr/bin/env python3
import sys
import re

# We need exactly 2 user parameters, meaning len(sys.argv) must be 3.

if len(sys.argv) != 3:
    # Case 1: Incorrect number of parameters (0, 1, or 3+)
    print("none")
else:
    # Parameter 1: The keyword to search for
    keyword = sys.argv[1]
    # Parameter 2: The text to be searched
    text = sys.argv[2]
    
    # Use re.findall() to find all non-overlapping occurrences of the keyword 
    # in the text. This returns a list of matches.
    # Note: By default, re.findall() is case-sensitive. Based on the examples 
    # ("the" in "the quick brown..."), case-sensitivity seems required.
    matches = re.findall(keyword, text)
    
    count = len(matches)
    
    if count > 0:
        # Case 2: Keyword was found one or more times
        print(count)
    else:
        # Case 3: Keyword was not found (count is 0)
        print("none")
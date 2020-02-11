"""
CSE212 
(c) BYU-Idaho
04-Teach - Problem 1 - Solution

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def unique_letters(text):
    """ 
    Determine if there are any duplicate letters in the text provided
    This solution using a set and results in O(n) performance.
    """
    found = set()
    for letter in text:
        # Look in set to see if letter was seen before
        if letter in found:
            return False
        # Otherwise we will add it to the set and move on
        found.add(letter)
    # If we made it this far then all letters were unique
    return True

test1 = "abcdefghjiklmnopqrstuvwxyz"  # Expect True because all letters unique
print(unique_letters(test1))

test2 = "abcdefghjiklanopqrstuvwxyz"  # Expect False because 'a' is repeated
print(unique_letters(test2))
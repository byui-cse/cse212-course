"""
CSE212 
(c) BYU-Idaho
05-Teach - Problem 1 - Solution

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def unique_letters(text):
    """ 
    Determine if there are any duplicate letters in the text provided.
    This solution should use a set and result in O(n) performance.
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

# An alternative solution:
def unique_letters2(text):
    """ 
    Determine if there are any duplicate letters in the text provided.
    This solution should use a set and result in O(n) performance.
    """
    unique = set()
    for letter in text:
        unique.add(letter)
    # The above three lines can be simplified to just: unique = set(text)

    # If the text has only unique letters, then the unique set should
    # be the same size of the text string.
    return len(unique) == len(text)

    # We could simplify this function to a single line:
    # return len(set(text)) == len(text)


test1 = "abcdefghijklmnopqrstuvwxyz"  # Expect True because all letters unique
print(unique_letters(test1))

test2 = "abcdefghijklanopqrstuvwxyz"  # Expect False because 'a' is repeated
print(unique_letters(test2))

test3 = "" 
print(unique_letters(test3))          # Expect True because its an empty string
"""
CSE212 
(c) BYU-Idaho
03-Prove - Problem 1

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def mystery_1(text):
    stack = []
    for letter in text:
        stack.append(letter)

    result = ""
    while len(stack) > 0:
        result += stack.pop()
    
    return result

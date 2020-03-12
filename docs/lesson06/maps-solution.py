#############
# Problem 1 #
#############

class Translator:
    """
    This class provides the capability of a translator.  A
    Python Dictionary is used to keep track of the mapping 
    of words from one language to another language.
    """

    def __init__(self):
        """ 
        Initialize the Python Dictionary
        """
        self.words = dict() 

    def add_word(self, from_word, to_word):
        """
        Add the translation from 'from_word' to 'to_word'
        For example, in a english to german dictionary:

        my_translator.add_word("book","buch")
        """
        self.words[from_word] = to_word 

    def translate(self, from_word):
        """
        Traslate a word and return the result.  If the word 
        can not be translated then "???" is returned.  
        For example, in an english to german dictionary:

        german_word = my_translator.translate("book")
        """
        if from_word not in self.words:  
            return "???"
        return self.words[from_word]

# Sample Test Cases (may not be comprehensive)
english_to_german = Translator()
english_to_german.add_word("House","Haus")
english_to_german.add_word("Car","Auto")
english_to_german.add_word("Plane","Flugzeug")
print(english_to_german.translate("Car")) # Auto
print(english_to_german.translate("Plane")) # Flugzeug
print(english_to_german.translate("Train")) # ???

#############
# Problem 2 #
#############

def summarize_degrees(filename):
    """
    Read a census file and summarize the degrees (education)
    earned by those contained in the file.  The summary
    should be stored in a dictionary where the key is the
    degree earned and the value is the number of people that 
    have earned that degree.  The degree information is in
    the 4th column of the file.  There is no header row in the
    file.
    """
    degrees = dict()
    with open(filename) as file_in:
        for line in file_in:
            fields = line.split(",") 
            degree = fields[3]       

            if degree in degrees: 
                degrees[degree] += 1
            else:
                degrees[degree] = 1
    return degrees

# Sample Test Cases

print(summarize_degrees("docs/lesson06/census.csv"))
# Results may be in a different order:
# {'Bachelors': 5355, 'HS-grad': 10501, '11th': 1175, 
# 'Masters': 1723, '9th': 514, 'Some-college': 7291, 
# 'Assoc-acdm': 1067, 'Assoc-voc': 1382, '7th-8th': 646, 
# 'Doctorate': 413, 'Prof-school': 576, '5th-6th': 333, 
# '10th': 933, '1st-4th': 168, 'Preschool': 51, 
# '12th': 433}   

#############
# Problem 3 #
#############

def convert_word_to_dictionary(word):
    """
    This function converts a word to a dictionary.  The key
    is a letter (all in upper case) and the value is the number
    of times the number appears in the word.
    """
    word_letters = dict()
    for letter in word:
        letter_upper = letter.upper()
        if letter_upper != " ":
            if letter_upper in word_letters:
                word_letters[letter_upper] += 1
            else:
                word_letters[letter_upper] = 1
    return word_letters


def is_anagram(word1, word2):
    """
    Determine if 'word1' and 'word2' are anagrams.  An anagram
    is when the same letters in a word are re-organized into a 
    new word.  A Python dictionary is used to solve the problem.

    Examples:
    is_anagram("CAT","ACT") would return True
    is_anagram("DOG","GOOD") would return False because GOOD has 2 O's
    """
    word1_letters = convert_word_to_dictionary(word1)
    word2_letters = convert_word_to_dictionary(word2)

    return word1_letters == word2_letters

# Sample Test Cases (may not be comprehensive)
print(is_anagram("A Decimal Point", "Im a Dot in Place"))  # True
print(is_anagram("tom marvolo riddle", "i am lord voldemort")) # True
print(is_anagram("Eleven plus Two", "Twelve Plus One")) # True
print(is_anagram("AABBCCDD", "ABCD")) # False
print(is_anagram("COW","DOG")) # False

#############
# Problem 4 #
#############

class Maze:
    """
    Defines a maze using a dictionary.  The dictionary is provided by the
    user when the Maze object is created.  The dictionary will contain the
    following mapping:

    (x,y) : (left, right, up, down)

    'x' and 'y' are integers and represents locations in the maze.
    'left', 'right', 'up', and 'down' are boolean are represent valid directions

    If a direction is False, then we can assume there is a wall in that direction.
    If a direction is True, then we can proceed.  

    If there is a wall, then display "Can't go that way!".  If there is no wall,
    then the 'curr_x' and 'curr_y' values should be changed.
    """

    def __init__(self, maze_map):
        """
        Initialize the map.  We assume that (1,1) is a valid location in
        the maze.
        """
        self.maze_map = maze_map
        self.curr_x = 1
        self.curr_y = 1

    def move_left(self):
        """
        Check to see if you can move left.  If you can, then move.  If you
        can't move, then display "Can't go that way!"
        """
        allowed = self.maze_map[(self.curr_x, self.curr_y)]
        if allowed[0]:
            self.curr_x -= 1
        else:
            print("Can't go that way!")

    def move_right(self):
        """
        Check to see if you can move right.  If you can, then move.  If you
        can't move, then display "Can't go that way!"
        """        
        allowed = self.maze_map[(self.curr_x, self.curr_y)]
        if allowed[1]:
            self.curr_x += 1
        else:
            print("Can't go that way!")

    def move_up(self):
        """
        Check to see if you can move up.  If you can, then move.  If you
        can't move, then display "Can't go that way!"
        """
        allowed = self.maze_map[(self.curr_x, self.curr_y)]
        if allowed[2]:
            self.curr_y -= 1
        else:
            print("Can't go that way!")

    def move_down(self):
        """
        Check to see if you can move down.  If you can, then move.  If you
        can't move, then display "Can't go that way!"
        """
        allowed = self.maze_map[(self.curr_x, self.curr_y)]
        if allowed[3]:
            self.curr_y += 1
        else:
            print("Can't go that way!")
    
    def show_status(self):
        print("Current location (x={} , y={})".format(self.curr_x, self.curr_y))

# Sample Test Cases 
map = {(1,1) : (False, True, False, True),
        (1,2) : (False, True, True, False),
        (1,3) : (False, False, False, False),
        (1,4) : (False, True, False, True),
        (1,5) : (False, False, True, True),
        (1,6) : (False, False, True, False),
        (2,1) : (True, False, False, True),
        (2,2) : (True, False, True, True),
        (2,3) : (False, False, True, True),
        (2,4) : (True, True, True, False),
        (2,5) : (False, False, False, False),
        (2,6) : (False, False, False, False),
        (3,1) : (False, False, False, False),
        (3,2) : (False, False, False, False),
        (3,3) : (False, False, False, False),
        (3,4) : (True, True, False, True), 
        (3,5) : (False, False, True, True),
        (3,6) : (False, False, True, False),
        (4,1) : (False, True, False, False),
        (4,2) : (False, False, False, False),
        (4,3) : (False, True, False, True),
        (4,4) : (True, True, True, False),
        (4,5) : (False, False, False, False),
        (4,6) : (False, False, False, False),
        (5,1) : (True, True, False, True),
        (5,2) : (False, False, True, True),
        (5,3) : (True, True, True, True),
        (5,4) : (True, False, True, True),
        (5,5) : (False, False, True, True),
        (5,6) : (False, True, True, False),
        (6,1) : (True, False, False, False),
        (6,2) : (False, False, False, False),
        (6,3) : (True, False, False, False),
        (6,4) : (False, False, False, False),
        (6,5) : (False, False, False, False),
        (6,6) : (True, False, False, False)}

maze = Maze(map)
choice = None
while choice != "exit":
    maze.show_status()
    choice = input("up/down/left/right/exit >")
    if choice == "up":
        maze.move_up()
    elif choice == "down":
        maze.move_down()
    elif choice == "left":
        maze.move_left()
    elif choice == "right":
        maze.move_right()
    elif choice == "exit":
        print("Goodbye!")
    else:
        print("Invalid Choice.")
    print()

#############
# Problem 5 #
#############

import requests  # Need to run 'pip install requests'

def earthquake_daily_summary():
    """
    This function will read JSON (Javascrip Object Notation) data from the 
    United States Geological Service (USGS) consisting of earthquake data.
    The data will include all earthquakes in the current day.
    
    JSON data is organized into a dictionary.  After reading the data using
    the 'requests' library, this function will print out a list of all
    earthquake locations ('place' attribute) and magnitudes ('mag' attribute).
    Additional information about the format of the JSON data can be found 
    at this website:  

    https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson_detail.php
    """    
    req = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson")
    data = req.json()
    earthquakes = []
    for feature in data["features"]:
        properties = feature["properties"]
        print("{} - Mag {}".format(properties["place"], properties["mag"]))

# Sample Test Cases 
earthquake_daily_summary()








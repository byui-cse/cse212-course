def earthquake_daily_summary():
    import requests  # Need to run 'pip install requests'
    req = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson")
    data = req.json()
    earthquakes = []
    for feature in data["features"]:
        properties = feature["properties"]
        print("{} - Mag {}".format(properties["place"], properties["mag"]))

earthquake_daily_summary()

def convert_word_to_dictionary(word):
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
    word1_letters = convert_word_to_dictionary(word1)
    word2_letters = convert_word_to_dictionary(word2)

    return word1_letters == word2_letters

print(is_anagram("A Decimal Point", "Im a Dot in Place"))  # True
print(is_anagram("tom marvolo riddle", "i am lord voldemort")) # True
print(is_anagram("Eleven plus Two", "Twelve Plus One")) # True
print(is_anagram("AABBCCDD", "ABCD")) # False
print(is_anagram("COW","DOG")) # False

class Translator:

    def __init__(self, from_lang, to_lang):
        self.from_lang = from_lang
        self.to_lang = to_lang
        self.words = dict()  # Add more code here as needed

    def add_word(self, from_word, to_word):
        self.words[from_word] = to_word  # Implement

    def translate(self, from_word):
        if from_word not in self.words:  # Implement
            return "???"
        return self.words[from_word]

english_to_german = Translator("English","German")
english_to_german.add_word("House","Haus")
english_to_german.add_word("Car","Auto")
english_to_german.add_word("Plane","Flugzeug")
print(english_to_german.translate("Car")) # Auto
print(english_to_german.translate("Plane")) # Flugzeug
print(english_to_german.translate("Train")) # ???

def summarize_degrees(filename):
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

print(summarize_degrees("docs/lesson06/census.csv"))
# Results may be in a different order:
# {'Bachelors': 5355, 'HS-grad': 10501, '11th': 1175, 
# 'Masters': 1723, '9th': 514, 'Some-college': 7291, 
# 'Assoc-acdm': 1067, 'Assoc-voc': 1382, '7th-8th': 646, 
# 'Doctorate': 413, 'Prof-school': 576, '5th-6th': 333, 
# '10th': 933, '1st-4th': 168, 'Preschool': 51, 
# '12th': 433}   

class Maze:

    def __init__(self, maze_map):
        self.maze_map = maze_map
        self.curr_x = 1
        self.curr_y = 1

    def move_left(self):
        allowed = self.maze_map[(self.curr_x, self.curr_y)]
        if allowed[0]:
            self.curr_x -= 1
        else:
            print("Can't go that way!")

    def move_right(self):
        allowed = self.maze_map[(self.curr_x, self.curr_y)]
        if allowed[1]:
            self.curr_x += 1
        else:
            print("Can't go that way!")

    def move_up(self):
        allowed = self.maze_map[(self.curr_x, self.curr_y)]
        if allowed[2]:
            self.curr_y -= 1
        else:
            print("Can't go that way!")

    def move_down(self):
        allowed = self.maze_map[(self.curr_x, self.curr_y)]
        if allowed[3]:
            self.curr_y += 1
        else:
            print("Can't go that way!")
    
    def show_status(self):
        print("Current location (x={} , y={})".format(self.curr_x, self.curr_y))

# (x,y) : (left, right, up, down)
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